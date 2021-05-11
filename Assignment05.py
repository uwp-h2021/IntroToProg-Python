# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# HJong, 5/7/2021, Created new script
# HJong, 5/8/2021, Defined variables in Data Section and Step 1 in Processing Section
# HJong, 5/8/2021, Completed Step 2 through 7 in Processing Section
# HJong, 5/9/2021, Added else statement to capture escape user input option
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # A string object that represents a file
objFile = None  # An object to contain the data in the file
strData = ""    # A row of text data from the file
dicRow = {}     # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []   # A list that acts as a 'table' of rows
strMenu = ""    # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, 'r')
for row in objFile:
    lstRow = row.split(',')
    dicRow = {'task': lstRow[0], 'priority': lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print('Current data are:\n')
        for row in lstTable:
            print(row['task']+','+row['priority'])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input('Please enter a new task name: ')
        prior = input('Please enter priority of this task: ')
        dicRow = {'task': task, 'priority': prior}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        task = input('Please enter the task to delete: ')
        for row in lstTable:
            if task in row.values():
                lstTable.remove(row)
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, 'w')
        for item in lstTable:
            objFile.write(item['task']+','+item['priority']+'\n')
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input('Press enter key to exit!')
        break  # and Exit the program
    # Step 8 - Capture user selection outside of [1-5]
    else:
        print('Please enter [1 to 5]:\n')
        continue
