"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


# creating list of users
f = open('users.txt', 'r')
users = []
for line in f.readlines():
    user_info = line.split()
    users.append([user_info[0], user_info[1]])
f.close()


# creating data of messages
file_messages = open('messages.txt', 'r')
messages = file_messages.read()
file_messages.close()


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()



login = ''

def registration(client):
    global users

    client.send(bytes("Create your login(name): ", "utf8"))
    login = client.recv(BUFSIZ).decode("utf8")
    client.send(bytes("Create your password: ", "utf8"))
    password = client.recv(BUFSIZ).decode("utf8")
    f = open('users.txt', 'a')
    f.write(login + ' ' + password + '\n')
    users.append([login, password])
    f.close()
    client.send(bytes("Your account has been created successfully", "utf8"))



def authorization(client):
    global login

    # authorization
    while True:
        client.send(bytes("Enter your login(if you don't have an account, type {register}): ", "utf8"))
        login = client.recv(BUFSIZ).decode("utf8")
        if login.encode('utf8') == bytes('{register}', 'utf8'):
            registration(client)
        else:
            for user in users:
                if login == user[0]:
                    while True:
                        client.send(bytes("Enter your password: ", "utf8"))
                        password = client.recv(BUFSIZ).decode("utf8")
                        if password == user[1]:
                            return 1
                        else:
                            client.send(bytes("Incorrect password!!! Try again!!!", "utf8"))
            else:
                client.send(bytes("Incorrect login!!! Try again!!!", "utf8"))


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    if authorization(client):
        global login
        global messages

        name = login
        welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
        client.send(bytes(welcome, "utf8"))
        msg = "%s has joined the chat!" % name
        broadcast(bytes(msg, "utf8"))

        # sending existing messages
        client.send(bytes(messages, 'utf8'))

        clients[client] = name
        while True:
            msg = client.recv(BUFSIZ)
            if msg != bytes("{quit}", "utf8"):
                m = name + ': ' + msg.decode('utf8') + '\n'
                messages += m
                broadcast(msg, name + ": ")
            else:
                # client.send(bytes("{quit}", "utf8"))
                client.close()
                del clients[client]
                broadcast(bytes("%s has left the chat." % name, "utf8"))
                break

    file_messages = open('messages.txt', 'w')
    file_messages.write(messages)
    file_messages.close()



def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


clients = {}
addresses = {}

HOST = '127.0.0.1'
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()



