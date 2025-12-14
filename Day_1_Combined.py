# Hi I'm starting 30 Days Challenge to skill up myself in Python.
# Day 1: Variables and Data Types in Python 
# Author: TANISH SAXENA
# Date: 2024-06-15

def main():
     # Variable assignment
    SQL_Commands = "DDL, DML, TCL, DCL" # String variable
    Day = 1 # Integer variable
    is_info = True # Boolean variable
    list_of_contents = SQL_Commands.split(", ") # List variable
    print(list_of_contents) # Printing the list of SQL command types
    for command in list_of_contents: # Iterating through each SQL command type
        print(f" SQL Command Type: {command}") # Printing each SQL command type
        # Describing the use of each SQL command type
        if command == "DDL":
            use = "Data Definition Language: Used to define database/table structure or schecma, {Create, Drop, Alter} "
            print(use)
        elif command == "DML":
            use = "Data Manipulation Language: Used to manipulate the dat within the database, {Insert, Upadte, Delete, Select}"
            print(use)
        elif command == "TCL":
            use = "Transaction Control Language: Used to manage the transactions in the database, {Commit, Rollback, Savepoint}"
            print(use)
        elif command == "DCL":
            use = "Data Control Language: Used to control the access of data within the database, {Grant, Revoke}"
            print(use)
        else:
            print("Invalid SQL Command Type")
    
if __name__ == "__main__":

    main()

