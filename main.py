'''
Module to read a list of strings from a CSV file
and create a SQL string dynamically.
'''

import csv
import os
import sqlparse

def read_csv_to_list(file_name):
    """
    Read in a CSV file and return a list of strings
    """
    output_array = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            output_array.append(row[0])
        return output_array

def add_service_to_sql_string(service_string):
    """
    Insert service name into SQL string and return string
    """
    return f" BEGIN \
     IF NOT EXISTS (SELECT * FROM Services \
     WHERE Name = \"{service_string}\" AND Verified = 1) \
     BEGIN INSERT INTO Services (Name, Verified) \
     VALUES (\"{service_string}\", 1) \
     END \
     END "

def create_sql_string(list_of_services):
    """
    Loop over list of service strings and return one
    long SQL string
    """
    output_string = ""
    for service in list_of_services:
        output_string += add_service_to_sql_string(service)
    return output_string

def save_to_sql_file(sql_string, output_file_name):
    """
    Save SQL string to .sql file
    """
    try:
        os.remove(output_file_name)
    except OSError:
        pass
    with open(output_file_name, "w") as text_file:
        text_file.write(sqlparse.format(sql_string, reindent=True, keyword_case='upper'))

def main():
    """
    Main function which results in writing SQL file
    """
    file_name = "listOfServices.csv"
    service_list = read_csv_to_list(file_name)
    sql_string = create_sql_string(service_list)
    save_to_sql_file(sql_string, "output.sql")

if __name__ == "__main__":
    main()
