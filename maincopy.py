import pandas as pd
import webbrowser
import numpy as np

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
    print("4) Summarize client sales")
    print("5) Quit")
    print()

    choice = int(input("Choose an option between 1 and 4: "))
    print("----------------------------------------")



    ############## ENTER CLIENT INFORMATION  ###########

    if choice == 1:
        print("CLIENT CREATION")
        print("")

        #ask for user information
        client_name=input("What is the name of the client ?")
        client_date_of_birth=input("What is the date of birth of the client ?")
        client_city_of_birth=input("What is the city of birth of the client ?")
        client_email= input("What is the email of the client ?")

        #add user inputs in the class Client
        client = Client(client_name, client_date_of_birth, client_city_of_birth, client_email)

        #display client informations
        print("\n")
        print("Client name : ",client.client_name)
        print("Client date of birth : ", client.client_date_of_birth)
        print("Client city of birth : ", client.client_city_of_birth)
        print("Client email : ", client.client_email)
        print("\n")
        print("The client has been created and saved")
        print("\n")
        
        #create a list with each detail of the client
        client_details = [client_name,client_date_of_birth,client_city_of_birth,client_email]
        # open file in appending mode
        with open("clients.txt", "a") as file:
          #write each detail of the client in the file
            for details in client_details:
                file.write(details)
                file.write(",")
          #skip line for the next client
            file.write("\n")
            file.close()


    
    ############### READ CLIENT INFORMATION #############

    elif choice == 2:
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


    
    ######## EXCEL CLIENT AND SALES ANALYSIS #######

    elif choice == 3:
        print("Excel client and sales analysis")
        print()
        #counter to exit sub menu when equal to 1
        i=0
        while i<1:

            print("1) Show client")
            print("2) Show sales")
            print("3) Show Excel file clients and sales")
            print("4) Quit")
            print()

            choice_excel = int(input("Choose an option between 1 and 4: "))
            print("----------------------------------------")

            if choice_excel == 1:
                # Open the sheet "clients" of the clients_sales.xlsx file using Pandas and display the column of the clients
                data_client = pd.read_excel("clients_sales.xlsx", "clients")
                print(data_client)

            elif choice_excel == 2:
                # Open the sheet "sales" of the clients_sales.xlsx file using Pandas and display the column of the sales
                data_sales = pd.read_excel("clients_sales.xlsx", "sales")
                print(data_sales)

            elif choice_excel == 3:
              
              print()
              print("RETRIEVE CLIENTS SALES INFORMATION")
              print()

              # counter to exit sub section when equal to "n"
              new_entry="y"
              while new_entry == "y":
                
                
                data_client = pd.read_excel("clients_sales.xlsx", "clients")
                data_sales = pd.read_excel("clients_sales.xlsx", "sales")

                client_name=input("What is the name of the client ?")

                #Get the index instead of the number
                client_index=data_client.loc[(data_client["name"] == client_name)].index

                #make sure the client exists
                if client_name in data_client:

                  #Get the number using the index
                  client_number = data_client.iloc[client_index]["client number"].values[0] #This is the number

                  #get the data frame for the client in question through the client number
                  client_info=(data_sales.loc[data_sales["Client number"] == client_number])

                  #get the number of product bought by the client through searching in the client_info dataframe
                  number_of_products_bought=(client_info["Client number"].count())

                  #get the average of sales of the client through searching in the client_info dataframe
                  avg_sales=round(client_info["Sales"].mean(),2)

                  #get the maximum spent for a sale by the client through searching in the client_info dataframe
                  max_sales=round(client_info["Sales"].max(),2)
                  
                  #get the sum of sales of the client through searching in the client_info dataframe
                  sum_sales=round(client_info["Sales"].sum(),2)

                  print("The client has bought :", number_of_products_bought, "products.")
                  print("Here is the mean of its sales ", avg_sales)
                  print("Here is the maximum spent for a sale ", max_sales)
                  print("Here is the sum of sales ", sum_sales)
                  print("\n")    

                  new_entry=input("Would you like to continue  ? (y/n) ")
                  print("\n")

                #display a message if the name does not exist or if the user mispelled it
                else:
                  print("\n")
                  print("This name is not found in the client file. Please enter a valid client name.")
                  print("\n")
            
            #end the counter and go back to the main menu
            else:
                i+=1

    ######## OPTIONNAL QUESTION #######
    elif choice == 4:

      data_sales = pd.read_excel("clients_sales.xlsx", "sales")
      
      print("---------- THE SUM OF SALES PER CLIENT NUMBER (ROWS) PER REGION (COLUMNS)----------")
      
      #Creation of a pivot table of the sum of sales per client number (rows) per region (columns)
      sum_sales_per_client_per_region = pd.pivot_table(data_sales, values="Sales", index=["Client number"], columns=["Region"],aggfunc=np.sum)
      print(sum_sales_per_client_per_region.round(2))
      print("\n")

      print("---------- THE SUM OF SALES PER CLIENT NUMBER PER DATE (ROWS) PER REGION (COLUMNS)----------") 
      
      #Creation of a pivot table of the sum of sales per client number per date (rows) per region (columns)
      sum_sales_per_client_per_date_per_region = pd.pivot_table(data_sales, values="Sales", index=["Client number","Date"], columns=["Region"],aggfunc=np.sum)
      print(sum_sales_per_client_per_date_per_region.round(2))

      # Export to an Excel file
      with pd.ExcelWriter("SUMMARIZE_CLIENTS_SALES.xlsx") as writer:
        sum_sales_per_client_per_region.to_excel(writer,sheet_name= "per_region")
        sum_sales_per_client_per_date_per_region.to_excel(writer,sheet_name="per_date")

      print("----------THE FILE SUMMARIZE_CLIENTS_SALES.XLSX HAS BEEN GENERATED----------")


    ########### THANK YOU ##########
    elif choice == 5:
        print("Thanks for the excel and python courses, best of luck with your second job :)")
        webbrowser.open("https://www.lademoducomedien.com/acteur/5471_hedayati-amir")

    else:
        print("End of the program")
        exit()
        
