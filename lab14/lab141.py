class Model:
    def __init__(self):
        self.todolist = []

    def add_task(self, new_task):
        self.todolist.append(new_task)
        print('Successfully added!!!')

    def delete_task(self, task_num):
        if task_num in range(0, len(self.todolist)):
            self.todolist.pop(task_num)
            print('Successfully deleted!!!')
        else:
            print('No task with such index')

    def edit_task(self, task_num):
        if task_num in range(0, len(self.todolist)):
            current_task = self.todolist[task_num]
            print('Your current task is: ')
            print(current_task)
            new_task = input('Enter a new task to it\'s place: ')
            self.todolist[task_num] = new_task
        else:
            print('No task with such index')

    def mark_as_done(self, task_num):
        if task_num in range(0, len(self.todolist)):
            if 'DONE' in self.todolist[task_num]:
                print('This task is already done!!!')
            else:
                self.todolist[task_num] += '\t\tDONE'
        else:
            print('No task with such index')


class View:
    def output_menu(self):
        print('1.Add new task\n2.Delete task\n3.Edit task\n4.Mark task as done\n5.Exit')

    def output(self, todolist):
        print('_' * 50)
        for i in range(0, len(todolist)):
            print(i, '.', todolist[i])
        print('_' * 50)


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
                new_task = input('Enter your task: ')
                self.model.add_task(new_task)
            elif choice == 2:
                try:
                    task_num = int(input('Enter number of task you want to delete: '))
                except ValueError:
                    print('Incorrect input!!!')
                    continue
                self.model.delete_task(task_num)
            elif choice == 3:
                try:
                    task_num = int(input('Enter number of task you want to edit: '))
                except ValueError:
                    print('Incorrect input!!!')
                    continue
                self.model.edit_task(task_num)
            elif choice == 4:
                try:
                    task_num = int(input('Enter number of task you want to mark as done: '))
                except ValueError:
                    print('Incorrect input!!!')
                    continue
                self.model.mark_as_done(task_num)
            elif choice == 5:
                program = False
            else:
                print('Incorrect input!!!')
                continue

            self.view.output(self.model.todolist)


def main():
    controller = Controller()
    controller.run()


if __name__ == '__main__':
    main()
