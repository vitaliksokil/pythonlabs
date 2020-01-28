class Employee:
    def __init__(self):
        self._salary = 0
        self._tax = 0
        self._surname = ''
        self._id = 0

    def salary_calculation(self):
        pass

    def tax_calculation(self):
        pass

    def get_surname(self):
        return self._surname

    def get_id(self):
        return self._id


class EmployeeHour(Employee):
    def __init__(self, id, surname, hourly_rate):
        super().__init__()
        self._surname = surname
        self._id = id
        self.__hourly_rate = hourly_rate

    def salary_calculation(self):
        self._salary = int(20.8 * 8 * self.__hourly_rate)
        return self._salary

    def tax_calculation(self):
        if not self._salary:
            print(
                'There is no salary!!! You should create salary by using function salary_calculation and then calculate taxes!!!')
            return 0
        self._tax = int(self._salary * 0.18 + self._salary * 0.015)
        return self._tax


class EmployeeFixed(Employee):
    def __init__(self, id, surname, fixed_salary):
        super().__init__()
        self._surname = surname
        self._id = id
        self.__fixed_salary = fixed_salary

    def salary_calculation(self):
        self._salary = int(self.__fixed_salary)
        return self._salary

    def tax_calculation(self):
        if not self._salary:
            print(
                'There is no salary!!! You should create salary by using function salary_calculation and then calculate taxes!!!')
            return 0
        self._tax = int(self._salary * 0.18 + self._salary * 0.015)
        return self._tax


class EmployeeIE(Employee):
    def __init__(self, id, surname, hours, money_per_hour):
        super().__init__()
        self._surname = surname
        self._id = id
        self.__hours = hours
        self.__money_per_hour = money_per_hour

    def salary_calculation(self):
        self._salary = int(self.__hours * self.__money_per_hour)
        self._salary += int(self._salary * 0.1)
        return self._salary

    def tax_calculation(self):
        if not self._salary:
            print(
                'There is no salary!!! You should create salary by using function salary_calculation and then calculate taxes!!!')
            return 0
        self._tax = int(self._salary * 0.05 + 704)
        return self._tax


class EmployeeSelf(Employee):
    def __init__(self, id, surname, lines_number, money_per_line):
        super().__init__()
        self._surname = surname
        self._id = id
        self.__lines_number = lines_number
        self.__money_per_line = money_per_line

    def salary_calculation(self):
        self._salary = int(self.__lines_number * self.__money_per_line)
        return self._salary

    def tax_calculation(self):
        if not self._salary:
            print(
                'There is no salary!!! You should create salary by using function salary_calculation and then calculate taxes!!!')
            return 0
        self._tax = int(self._salary * 0.18 + self._salary * 0.015 + 704)
        return self._tax


def print_emp(employees):
    print('-' * 80)
    print('ID\t|\tSurname \t|\tSalary\t|\tTax\t|\t')
    print('-' * 80)
    sum_tax = 0
    for i in employees:
        print(i.get_id(), '\t|\t', i.get_surname(), ' \t|\t', i.salary_calculation(), '\t|\t', i.tax_calculation(),
              '\t|\t')
        sum_tax += i.tax_calculation()

    print('-' * 80)
    print('', '\t|\t', '\t', ' \t|\t', '', '\t|', 'sum tax:', sum_tax,
          '|\t')
    print('-' * 80)


emp1 = EmployeeHour(1, 'Smith', 20)
emp2 = EmployeeFixed(2, 'Jones', 3000)
emp3 = EmployeeIE(3, 'Wilson', 160, 20)
emp4 = EmployeeSelf(4, 'Evans', 5000, 1)

employees = [emp1, emp2, emp3, emp4]
print_emp(employees)
employees.sort(key=lambda emp: (emp.salary_calculation(), emp.get_surname()), reverse=True)
print_emp(employees)
