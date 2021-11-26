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
        #counter to exit sub section when equal to 1
        i=0
        while i<1:

            print("Excel client and sales analysis")
            print()
            print("1) Show client")
            print("2) Show sales")
            print("3) Show Excel file clients and sales")
            print("4) Quit")
            print()

            choix2 = int(input("Choose an option between 1 and 4: "))
            print("----------------------------------------")

            if choix2 == 1:
                # Open the sheet "clients" of the clients_sales.xlsx file using Pandas and display the column of the clients
                data_client = pd.read_excel("clients_sales.xlsx", "clients")
                print(data_client)

            elif choix2 == 2:
                # Open the sheet "sales" of the clients_sales.xlsx file using Pandas and display the column of the sales
                data_sales = pd.read_excel("clients_sales.xlsx", "sales")
                print(data_sales)

            #Lea, choix==3 ne fontionne pas, ce qui est entre les ###
            ###
            elif choix2 == 3:
                print()
                print("RETRIEVE CLIENTS SALES INFORMATION")
                print()

                client_name=input("What is the name of the client ?")
                data_client = pd.read_excel("clients_sales.xlsx", "clients")
                data_sales = pd.read_excel("clients_sales.xlsx", "sales")

                client_number=data_client.loc[(data_client["name"] == client_name),["client number"]]

                result_client_number=str(client_number)
                print(result_client_number)

                product_bought=data_sales.loc[(data_sales["client number"==result_client_number])]
                print("The client has bought ", product_bought, " products")
            ###

            else:
                i+=1

    elif choix == 5:
        print("Thanks for the excel and pyhton courses, best of luck with your second job :)")
        webbrowser.open("https://www.lademoducomedien.com/acteur/5471_hedayati-amir")

    else:
        exit()