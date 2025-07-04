from person import Person 
from student import Student
from employee import Employee
from menuOption import MenuOption  
import pandas as pd

print("*** hello to my final project in python ***")

def printMenu():
    print("1. save a new entry: ")
    print("2. Search by ID: ")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. save all data ")
    print("9. Exit")
     
def checkNumber(text: str, num: int):
    if not num.isdigit():
        print("Error: " + text + " must be a number and " + num + " is not a number")
        return False
    return True

def saveNewEntry(data_dict: dict, id_list: list, ages_dict: dict):    
    id_input = input("ID: ")
    if not checkNumber("id", id_input):
        return
    id_input = int(id_input)
    if id_input in data_dict:
        print("Error: ID is already exists: " + str(data_dict[id_input]))
    id_list.append(id_input)
    name_input = input("name: ")
    age_input = input("Age: ")
    if not checkNumber("Age", age_input):
        return
    age_input = int(age_input)
    ages_dict["age"] += age_input  
    role_input = input("plaese enter number 1 if person is employee, enter number 2 if person student and number 3 if other ")
    if not checkNumber("nume choic ", role_input):
        return
    role_input = int(role_input)
    if role_input == 1 : 
        employee_work_input = input("enter the field of work ")
        employee_salary_input = input("enter the salary ")
        if not checkNumber("employee salary ", employee_salary_input):
            return
        employee_salary_input = int(employee_salary_input)
        new_entry = Employee(id_input, name_input, age_input, employee_work_input, employee_salary_input)
        data_dict[id_input] = new_entry  
        
    if role_input == 2 :
        field_study_input = input("Enter field of study ")
        year_study_input = input("Enter year of study ")
        if not checkNumber("year study ", year_study_input):
            return
        score_avg_input = input("Enter score avg ")
        if not checkNumber("score avg ", score_avg_input):
            return
        new_entry = Student(id_input, name_input, age_input, field_study_input, year_study_input, score_avg_input)
        data_dict[id_input] = new_entry
        
    if role_input == 3 :
        new_entry = Person(id_input, name_input, age_input)
        data_dict[id_input] = new_entry 
    print("ID " + str(id_input) + " saved successfuly")
        
def searchById(data_dict: dict): #choice 2
    search_id = input("please enter the ID you look for: ")
    if not checkNumber("id",search_id):
        return
    search_id = int(search_id)
    if search_id in data_dict:
        data_dict[search_id].printMySelf()
    else:
        print("Error: " + str(search_id)  + " is not saved")
        return

def printagesAverage(ages_dict: dict, data_dict: dict): #choice 3
    sum = ages_dict["age"] 
    if sum == 0:
        print("Erorr: you dont save any entry yet ")
    else:
        average = sum / len(data_dict)
        print("the average is: ", average)

def printAllNames(data_dict: dict): #choice 4 
    for index, person in enumerate(data_dict.values()):
        print(str(index) +". " + person.getName()) 

def printAllIds(data_dict: dict): #choice 5
    for index, id in enumerate(data_dict):
        print(str(index) + ". " + str(id))
# printAllIds(data_dict)

def printAllEntries(data_dict: dict):   #choice 6
    for index, person in enumerate(data_dict.values()):
        print(str(index) +". ") , person.printMySelf()

def printEntryByIndex(data_dict:dict, id_list: list): #choice 7
    index_input = input("please enter the index of the entry you want to print: ")
    if not checkNumber("index",index_input):
        return
    index_input = int(index_input)
    if index_input > len(data_dict)-1: 
        print("Error: index out of range. the maximum index allowd is: " + str(len(data_dict)-1)) 
    else:
        id_value = id_list[index_input]
        data_dict[id_value].printMySelf()

def saveAllData(data_dict: dict): # choice 8
    csv_filename = input("What is your output file name ? ")   
    data_list = []
    for person in data_dict.values():
        data_list.append(person.to_dict())
    df = pd.DataFrame(data_list)
    df.to_csv(csv_filename,index=False)
    print(df)
        
def main():
    id_list = []
    data_dict = {}
    ages_dict = {"age": 0 }
    try:
        while True:
            try:
                printMenu()
                choice = input("please enter your choice: ")
                # if not checkNumber("choice", choice):
                #     return
                choice = int(choice)
                if choice == MenuOption.SAVE.value:
                    saveNewEntry(data_dict, id_list, ages_dict)
                elif choice == MenuOption.SEARCH_ID.value:
                    searchById (data_dict)
                elif choice == MenuOption.PRINT_AGES_AVG.value :
                    printagesAverage(ages_dict, data_dict)
                elif choice == MenuOption.PRINT_NAMES.value  :
                    printAllNames(data_dict)
                elif choice == MenuOption.PRINT_IDS.value :
                    printAllIds(data_dict)
                elif choice == MenuOption.PRINT_ALL.value :
                    printAllEntries(data_dict)
                elif choice == MenuOption.PRINT_BY_IDX.value :
                    printEntryByIndex(data_dict, id_list)
                elif choice == MenuOption.SAVE_DATA.value :
                    saveAllData(data_dict)
                elif choice == MenuOption.EXIT.value : 
                    exe_input = input("are you sure ? (y/n) ")
                    while True:
                        if exe_input == "n":
                            printMenu()
                            break
                        if exe_input == "y":
                            print("goodbye!")
                            return
                else: 
                    raise ValueError("Invalid option. Please choose number between 1 and 9.")
                    # except ValueError:
                    #     print("Caught a ValueError")
                input("Press Enter to Continue ")
            except ValueError:
                print(" Error: invalid input. Please enter a number between 1 and 9.")   
    except KeyboardInterrupt:
        print(" Exiting the program. Goodbye!")
main()