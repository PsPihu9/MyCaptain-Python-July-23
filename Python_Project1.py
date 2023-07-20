'''
@author: Prashansa Shah 
@description: First Project in Python
'''
# Task - Enter Student information, Pre-process the collected data, Write all the pre-processed data into a File

import csv

# creating function to add student's information to csv file
def add_std_csv(std_info):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["First Name","Last Name","Roll No","Class"])

        writer.writerow(std_info)


if __name__ == '__main__':

    condition=True                                  # intializing loop condition as True
    std_no = 1

    while (condition):
        # inputting all information in a string
        raw_std_info = input("Enter information for student #{} in the format (First_Name Last_Name Roll_No Class):".format(std_no))
        
        # splitting all raw data and saving in the form of a list
        std_info = raw_std_info.split(' ')
        print("You have entered: \nFirst Name: {}\nLast Name: {}\nRoll No.: {}\nClass: {}".format(std_info[0],std_info[1],std_info[2],std_info[3]))
        
        # checking exit condition for the loop
        check = input("Is the information entered correct? (Y/N)")
        if check == 'Y':
            add_std_csv(std_info)
            check_next = input("Do you want to enter another student's information? (Y/N)")
            if check_next == 'Y':
                std_no+=1
            elif check_next == 'N':
                condition = False
        elif check == 'N':
            print("Please re-enter correct information:")
    
    
    

