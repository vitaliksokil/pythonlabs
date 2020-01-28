from http import HTTPStatus
from http.server import HTTPServer, SimpleHTTPRequestHandler
import mysql.connector
import json
import ast
import re

mydb = mysql.connector.connect(user='root', password='',
                               host='127.0.0.1',
                               database='todo',
                               port=3307)
mycursor = mydb.cursor(dictionary=True)


class Serv(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers',
                         'Origin, X-Requested-With, Content-Type, Accept, Authorization')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE, OPTIONS')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_PUT(self):
        content_len = int(self.headers['content-length'])
        body = self.rfile.read(content_len)
        edited_task = ast.literal_eval(body.decode('utf-8'))
        sql_stmt = "UPDATE `todo`.`tasks` set task = '" + str(edited_task['task']) + "', done = " \
                   + str(edited_task['done']) + " WHERE id = " + str(edited_task['id'])
        mycursor.execute(sql_stmt)
        mydb.commit()
        # Begin the response
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        return

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.end_headers()

    def do_POST(self):
        if self.path == '/add':
            content_len = int(self.headers['content-length'])
            post_body = self.rfile.read(content_len)
            new_task = ast.literal_eval(post_body.decode('utf-8'))['new_task']
            sql_stmt = "INSERT INTO `todo`.`tasks` (`task`) VALUES ('" + new_task + "')"
            mycursor.execute(sql_stmt)
            mydb.commit()
            # Begin the response
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            return
        elif self.path == '/delete':
            content_len = int(self.headers['content-length'])
            body = self.rfile.read(content_len)
            id = ast.literal_eval(body.decode('utf-8'))['id']
            sql_stmt = "DELETE FROM `todo`.`tasks` WHERE id = " + str(id)
            mycursor.execute(sql_stmt)
            mydb.commit()
            # Begin the response
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            return

    def do_GET(self):
        if self.path == '/':
            self.path = '/frontend/index.html'
        elif self.path == '/get-todo':
            # returns all tasks
            query = 'SELECT * FROM tasks'
            mycursor.execute(query)
            lst = mycursor.fetchall()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(json.dumps(lst), 'utf8'))
            return
        elif re.match(r'/get-item\?id=\d+', self.path):
            try:
                ID = int(self.path.split('?id=')[1])
            except ValueError:
                self.send_response(HTTPStatus.INTERNAL_SERVER_ERROR)
                return
            query = 'SELECT * FROM tasks WHERE id = ' + str(ID)
            mycursor.execute(query)
            data = mycursor.fetchone()
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            self.wfile.write(bytes(json.dumps(data), 'utf8'))
            return
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = 'File not found'
            self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


httpd = HTTPServer(('localhost', 8080), Serv)
print('Serving on port 8080...\nGo to http://127.0.0.1:8080\nTo stop serving press CTRL + C')
httpd.serve_forever()
mydb.close()
