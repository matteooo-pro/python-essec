################################################################################
# GROUP MEMBERS : LEA PEDRONI & MATTEO PROCOPPE
################################################################################

import pandas as pd
import webbrowser

class Client:

    #CLASS CREATION TO BE ABLE TO STORE THE USER INPUT
    def __init__(self, client_name, client_date_of_birth, client_city_of_birth, client_email):
        self.client_name = client_name
        self.client_date_of_birth = client_date_of_birth
        self.client_city_of_birth = client_city_of_birth
        self.client_email = client_email

    def print_client_info(self):
        print(self.client_name, self.client_date_of_birth, self.client_city_of_birth,self.client_email)

while (True):
    print("----------------------------------------")
    print("Welcome to the client and sales analysis")
    print()
    print("1) Create a new client in Txt file")
    print("2) Show all the clients in Txt file")
    print("3) Show Excel file clients and sales")
    print("4) Quit")
    print()

    choix = int(input("Choose an option between 1 and 4: "))
    print("----------------------------------------")

    if choix == 1:
        print("CLIENT CREATION")
        print("")

        #ask for user information
        client_name=input("What is the name of the client ?")
        client_date_of_birth=input("What is the date of birth of the client ?")
        client_city_of_birth=input("What is the city of birth of the client ?")
        client_email= input("What is the email of the client ?")

        #add user inputs in the class Client
        client = Client(client_name, client_date_of_birth, client_city_of_birth, client_email)

        print("\n")
        print("Client name : ",client.client_name)
        print("Client date of birth : ", client.client_date_of_birth)
        print("Client city of birth : ", client.client_city_of_birth)
        print("Client email : ", client.client_email)
        print("\n")
        print("The client has been created and saved")
        print("\n")

        # open file in appending mode
        file = open("clients.txt", "a")
        # write the client's information in the file
        file.write(client.client_name)
        file.write(",")
        file.write(client.client_date_of_birth)
        file.write(",")
        file.write(client.client_city_of_birth)
        file.write(",")
        file.write(client.client_email)
        # write a new line
        file.write("\n")
        file.close()

    elif choix == 2:
        print(" ")
        print("CLIENT INFORMATION")

        def read_file_lines(file_name):
            # open the file in read mode
            my_file = open(file_name, "r")
            #print the lines
            for line in my_file:
                print(line)
            my_file.close()

        read_file_lines("clients.txt")

    elif choix == 3:
        # Replace the pass instruction with your code
        pass

    elif choix == 5:
        print("Thanks for the excel and pyhton courses, best of luck with your second job :)")
        webbrowser.open("https://www.lademoducomedien.com/acteur/5471_hedayati-amir")

    else:
        exit()