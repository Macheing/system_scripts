#!/usr/bin/env python3
import csv

# read employees data from csv file.
def read_employees(csv_file_location):
	with open(csv_file_location) as file:
		csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
		employee_file = csv.DictReader(file, dialect = 'empDialect')
		employee_list = []
		for data in employee_file:
			employee_list.append(data)

		return employee_list

employee_list = read_employees('employees.csv')
x = '===='
print(x*10,'Employees and Department list', x*10)
print(employee_list)
print()

# process employees' data 
def process_data(employee_list):
	department_list = []
	for employee_data in employee_list:
		 department_list.append(employee_data['Department'])
		
	department_data = {}
	for department_name in set(department_list):
		department_data[department_name] = department_list.count(department_name)

	return department_data

dictionary = process_data(employee_list)

print(x*10,' Total Number of Employees per Department ', x*10)
print(dictionary)
print()

# write report to a file
def write_report(dictionary,report_file):
	with open(report_file, 'w+') as report:
		for key in sorted(dictionary):
			report.write(str(key) + ':' + str(dictionary[key]) + '\n')

		report.close()
write_report(dictionary,'report_file.txt')