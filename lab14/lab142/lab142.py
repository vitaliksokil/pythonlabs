class Model:
    class Subscriber:
        def __init__(self, id, name, surname, number):
            self.id = id
            self.name = name
            self.surname = surname
            self.number = number

    def __init__(self):
        self.filename = 'subscribers.txt'
        self.phone_book = self.get_subscribers()

    def create_id(self):
        last_subscriber = self.phone_book[-1]
        new_id = int(last_subscriber.id) + 1
        return new_id

    def get_subscribers(self):
        f = open(self.filename, 'r')
        phone_book = []
        for line in f:
            ID, name, surname, number = line.split()
            subscriber = self.Subscriber(int(ID), name, surname, number)
            phone_book.append(subscriber)
        f.close()
        return phone_book

    def add_subscriber(self, name, surname, number):
        f = open(self.filename, 'a')
        new_subscriber = self.Subscriber(self.create_id(), name, surname, number)
        f.write(str(
            new_subscriber.id) + ' ' + new_subscriber.name + ' ' + new_subscriber.surname + ' ' + new_subscriber.number + '\n')
        self.phone_book.append(new_subscriber)
        print('Successfully added!!!')
        f.close()

    def delete_subscriber(self, ID):
        is_found = False
        for i in range(0, len(self.phone_book)):
            if self.phone_book[i].id == ID:
                self.phone_book.pop(i)
                is_found = True
                break
        if is_found:
            f = open(self.filename, 'w')
            for i in self.phone_book:
                f.write(str(i.id) + ' ' + i.name + ' ' + i.surname + ' ' + i.number + '\n')
            f.close()
            print('Subscriber was successfully deleted')
        else:
            print('There is no subscriber with such id!!!')

    def search_by_name(self, name):
        for i in self.phone_book:
            if name in i.name:
                print(i.id, ' ', i.name, ' ', i.surname, ' ', i.number)
                break
        else:
            print('There is no subscriber with name: ', name)

    def search_by_number(self, number):
        for i in self.phone_book:
            if number in i.number:
                print(i.id, ' ', i.name, ' ', i.surname, ' ', i.number)
                break
        else:
            print('There is no subscriber with number: ', number)


class View:
    def output_menu(self):
        print('1.Add new subscriber\n2.Delete subscriber\n3.Search\n4.Show phone book\n5.Exit')

    def output(self, phone_book):
        print('_' * 150)
        print('ID', '\t|\t',
              'Name', ' ' * (30 - len('Name')), '|\t',
              'Surname', ' ' * (30 - len('Surname')), '|',
              'Number', ' ' * (30 - len('Number')), '|')
        print('_' * 150)
        for i in range(0, len(phone_book)):
            print(phone_book[i].id, '\t|\t',
                  phone_book[i].name, ' ' * (30 - len(phone_book[i].name)), '|\t',
                  phone_book[i].surname, ' ' * (30 - len(phone_book[i].surname)), '|',
                  phone_book[i].number, ' ' * (30 - len(phone_book[i].number)), '|')
        print('_' * 150)


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        program = True
        while program:
            self.view.output_menu()
            try:
                choice = int(input())
            except ValueError:
                print('Incorrect input!!!')
                continue
            if choice == 1:

                name = input('Enter subscriber name: ')
                surname = input('Enter subscriber surname: ')
                number = input('Enter subscriber number: ')

                self.model.add_subscriber(name, surname, number)
            elif choice == 2:
                try:
                    ID = int(input('Enter id of subscriber you want to delete: '))
                except ValueError:
                    print('Incorrect input!!!')
                    continue
                self.model.delete_subscriber(ID)
            elif choice == 3:
                try:
                    search_by = int(input('Search by: \n1.Name\n2.Number\n'))
                    if search_by == 1:
                        name = input('Enter name: ')
                        self.model.search_by_name(name)
                    elif search_by == 2:
                        number = input('Enter number: ')
                        self.model.search_by_number(number)
                    else:
                        print('Incorrect value!!!')
                except ValueError:
                    print('Incorrect input!!!')
                    continue
            elif choice == 4:
                self.view.output(self.model.phone_book)
            elif choice == 5:
                program = False
            else:
                print('Incorrect input!!!')
                continue


def main():
    controller = Controller()
    controller.run()


if __name__ == '__main__':
    main()
