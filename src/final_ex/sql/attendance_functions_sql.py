# from final_ex.attendance import Employee
from datetime import datetime, date, timedelta
import csv
import MySQLdb

db = None
# db.query('SELECT * FROM employees;')
# result = db.store_result()  # storing the entire result in python variable
# print(result.fetch_row(maxrows=0, how=1))  # maxrows=0, present all the table, 0 means unlimited


employee_fields = ['employee_id', 'name', 'age', 'phone']
# attendance_fields = ['record_id', 'employee_id', 'timestamp']


def init(hostname, port, user_name, password, scheme):
    global db
    db = MySQLdb.connect(host=hostname, port=port, user=user_name, passwd=password, db=scheme)

#
# def get_employee_from_file(employee_id, file_name='employees.csv'):
#     try:
#         with open(file_name, 'r', newline='') as employees_file:
#             reader = csv.DictReader(employees_file, fieldnames=employee_fields, dialect='excel')
#             for employee in reader:
#                 if employee['employee_id'] == employee_id:
#                     return employee
#     except IOError:
#         print("file is not available")
#     return None


def get_employee_from_db(employee_id):
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM employees WHERE employee_id = %s;', (employee_id,))
    result = cursor.fetchone()
    if result:
        return result
    else:
        return None


def get_employees_from_file(file_name='employees.csv'):
    employees = {}
    try:
        with open(file_name, 'r', newline='') as employees_file:
            next(employees_file)
            reader = csv.DictReader(employees_file, fieldnames=employee_fields, dialect='excel')
            for employee in reader:
                employees[employee['employee_id']] = employee
    except IOError:
        print("file is not available")
    return employees


def get_employees_from_db():
    employees = {}
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM employees;')
    result = cursor.fetchall()
    for employee in result:
        employees[employee['employee_id']] = employee
    return employees


def add_employee():
    employee_id = ''
    while len(employee_id) != 6 or (any(not c.isdigit() for c in employee_id)):
        employee_id = input("Please enter employee id, employee id should contain 6 digits:")
        if len(employee_id) != 6:
            print("Please make sure to use only 6 digits id number!")
        if any(not c.isdigit() for c in employee_id):
            print("Please make sure to enter only digits!")
    if get_employee_from_db(employee_id) is not None:
        print("This employee_id already exists")
        return

    name = ''
    while name == '' or any(c.isdigit() for c in name):
        name = input("Please enter employee name:")
        if name == '':
            print("Please make sure to enter employee name!")
        if any(c.isdigit() for c in name):
            print("Please make sure that the employee name does not contain any digits")

    age = 0
    while age < 18:
        try:
            age = int(input("Please enter employee age, employee age should contain only digits:"))
            if age < 18:
                print("Please make sure to enter employee correct age!")
        except ValueError:
            print("Please make sure to enter only digits!")
            age = 0

    phone = ''
    while len(phone) != 10 or any(not c.isdigit() for c in phone):
        phone = input("Please enter employee phone, employee phone should contain 10 digits:")
        if len(phone) != 10:
            print("Please make sure to use only 10 digits phone number!")
        if any(not c.isdigit() for c in phone):
            print("Please make sure to enter only digits!")

    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO employees (`employee_id`, `name`, `age`, `phone`) "
                       "VALUES (%s, %s, %s, %s);", (employee_id, name, age, phone))
        db.commit()
    except Exception as e:  # change exception to specific exception
        db.rollback()
        print(e)


def add_employees_from_file():
    file_name = input("Please enter the file name you would like to load:")
    new_employees = get_employees_from_file(file_name)
    for employee in new_employees:
        if get_employee_from_db(new_employees[employee]['employee_id']) is None:
            # add empty list, append each employee, iterate over new employees list in the try, and insert them. commit afterwards.
            cursor = db.cursor()
            try:
                cursor.execute("INSERT INTO employees (`employee_id`, `name`, `age`, `phone`) "
                               "VALUES (%s, %s, %s, %s);",
                               (new_employees[employee]['employee_id'], new_employees[employee]['name'],
                                new_employees[employee]['age'], new_employees[employee]['phone']))
                db.commit()
            except Exception as e:  # change exception to specific exception
                db.rollback()
                print(e)


def delete_employee():
    employee_id = 0
    while len(str(employee_id)) != 6 or (any(not c.isdigit() for c in employee_id)):
        employee_id = input("Please enter the employee id you would like to delete:")
        if len(str(employee_id)) != 6:
            print("Please make sure to use only 6 digits id number!")
        if any(not c.isdigit() for c in employee_id):
            print("Please make sure to enter only digits!")
    if get_employee_from_db(employee_id) is None:
        print("This employee_id does not exist")
        return

    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM employees WHERE employee_id = %s;", (employee_id,))
        db.commit()
    except Exception as e:  # change exception to specific exception
        db.rollback()
        print(e)


def delete_employees_from_file():
    file_name = input("Please enter the file name you would like to load:")
    employees = get_employees_from_db()
    employees_to_delete = get_employees_from_file(file_name)
    for employee in employees_to_delete:
        # add empty list, append each employee, iterate over employees to delete list in the try, and delete them. commit afterwards.
        if employee in employees:
            cursor = db.cursor()
            try:
                cursor.execute("DELETE FROM employees WHERE employee_id = %s;", (employees[employee]['employee_id'],))
                db.commit()
            except Exception as e:
                db.rollback()
                print(e)


def mark_attendance():
    employee_id = ''
    while len(employee_id) != 6 or get_employee_from_db(employee_id) is None or (any(not c.isdigit() for c in employee_id)):
        employee_id = input("Please enter your employee id:")
        if len(str(employee_id)) != 6:
            print("Please make sure to use only 6 digits id number!")
        if get_employee_from_db(employee_id) is None:
            print("This id does not exist! Please enter your employee id!")
        if any(not c.isdigit() for c in employee_id):
            print("Please make sure to enter only digits!")

    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO employees_attendance (`employee_id`, `timestamp`) "
                       "VALUES (%s, %s);", (employee_id, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))  # try without the string conversion, use CURTIME() instead of dapython datetime
        db.commit()
    except Exception as e:  # change exception to specific exception
        db.rollback()
        print(e)


def employee_report():
    employee_id = ''
    while len(employee_id) != 6 or get_employee_from_db(employee_id) is None or (any(not c.isdigit() for c in employee_id)):
        employee_id = input("Please enter employee id:")
        if len(str(employee_id)) != 6:
            print("Please make sure to use only 6 digits id number!")
        if get_employee_from_db(employee_id) is None:
            print("This id does not exist! Please enter employee id!")
        if any(not c.isdigit() for c in employee_id):
            print("Please make sure to enter only digits!")

    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM employees_attendance WHERE employee_id = %s;", (employee_id,))
        result = cursor.fetchall()
        for line in result:
            print(line['timestamp'])
    except Exception as e:  # change exception to specific exception
        print(e)


def monthly_report():
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    today = date.today()
    first = today.replace(day=1)
    last_month = (first - timedelta(days=1)).strftime('%Y-%m')
    try:
        cursor.execute("SELECT * FROM employees_attendance WHERE cast(timestamp as char) LIKE %s;", (last_month + "%",))  # use between in the SQL query
        result = cursor.fetchall()
        for line in result:
            print(line['employee_id'], line['timestamp'])
    except Exception as e:
        print(e)


def late_report():
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM employees_attendance WHERE date_format(timestamp, '%H:%i:%s') > '09:30:00';")
        result = cursor.fetchall()
        for line in result:
            print(line['employee_id'], line['timestamp'])
    except Exception as e:
        print(e)


def report_at_specific_time():
    start_date = ''
    end_date = ''
    while start_date == '':
        start_date = input("Please enter start date in the following format YYYY-MM-DD:")
        try:
            datetime.strptime(start_date, '%Y-%m-%d')
        except ValueError:
            print('invalid date')
            start_date = ''
    while end_date == '':
        end_date = input("Please enter end date in the following format YYYY-MM-DD:")
        try:
            datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            print('invalid date')
            end_date = ''

    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM employees_attendance WHERE date_format(timestamp, '%%Y-%%m-%%d') "
                       "BETWEEN %s and %s;", (start_date, end_date,))
        result = cursor.fetchall()
        for line in result:
            print(line['employee_id'], line['timestamp'])
    except Exception as e:
        print(e)
