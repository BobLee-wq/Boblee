#Import required modules

from ctuClass import * 
from colorama import Fore, Back, Style, init

init()

#Create place holder values fore shopName, Location, Customers, Sales and Returns
Shop1 = ctuStock("Default", "Default", 0, 0, 0)
Shop2 = ctuStock("Default", "Default", 0, 0, 0)
Shop3 = ctuStock("Default", "Default", 0, 0, 0)
Shop4 = ctuStock("Default", "Default", 0, 0, 0)

#Set a number for current stock
stock_shop1 = {"Computer":100, "RaspPi":100, "Monitor":100}
stock_shop2 = {"Computer":100, "RaspPi":100, "Monitor":100}
stock_shop3 = {"Computer":100, "RaspPi":100, "Monitor":100}
stock_shop4 = {"Computer":100, "RaspPi":100, "Monitor":100}

#Create a while loop to allow proccess to repeat
#Create first menu
while True:
    print(Fore.GREEN + "|___WELCOME TO CTU TECHNOLOGIES___|" + Fore.RESET)
    print("1. Shop Managementv\n 2. Sales\n 3.Returns")
    print("2. Sales")
    print("3. Returns")
    print("4. Stock")
    print("99. Exit")

#Create an initial input to start the process
    choice = input(Fore.LIGHTBLUE_EX + "Enter your choice: " + Fore.RESET)
#create if,elif and else statements for every possible circumstance or picked option
    if choice == "1":
        print("1. Change shop Name")
        print("2. Change shop location")
        print("3. Display current shops")
        print("4. Display all shops information")
        print("0. Back")

        choice_2 = input(Fore.LIGHTBLUE_EX + "Select an option from the numbers above: " + Fore.RESET) 
#Create options to change shopNames
        if choice_2 == "1":
            print("Current shop names: ")
            print("1." ,Shop1.shopName)
            print("2." ,Shop2.shopName)
            print("3." ,Shop3.shopName)
            print("4." ,Shop4.shopName)

            option_1 = input(Fore.LIGHTBLACK_EX + "Select a number from the list above: " + Fore.RESET)
           
            if option_1 == "1":
                name_change = input(Fore.CYAN + "Type new shop name: " + Fore.RESET)
                Shop1.shopName = name_change
                print("Shop name has been changed successfully to", name_change)
                print("Updated shop names: ")
                print("1." ,Shop1.shopName)
                print("2." ,Shop2.shopName)
                print("3." ,Shop3.shopName)
                print("4." ,Shop4.shopName)
            
            elif option_1 =="2":
                name_change = input(Fore.CYAN + "Type new shop name: " + Fore.RESET)
                Shop2.shopName= name_change
                print("Shop name has been changed successfully to ", name_change)
                print("Updated shop names: ")
                print("1." ,Shop1.shopName)
                print("2." ,Shop2.shopName)
                print("3." ,Shop3.shopName)
                print("4." ,Shop4.shopName)

            elif option_1 == "3":
                name_change = input(Fore.CYAN + "Type new shop name: " + Fore.RESET)
                Shop3.shopName = name_change
                print("Shop name has been changed successfully to ", name_change)
                print("Updated shop names: ")
                print("1." ,Shop1.shopName)
                print("2." ,Shop2.shopName)
                print("3." ,Shop3.shopName)
                print("4." ,Shop4.shopName)
                
            elif option_1 == "4":
                name_change = input(Fore.CYAN + "Type new shop name: " + Fore.RESET)
                Shop4.shopName = name_change
                print("Shop name has been changed successfully to ", name_change)
                print("Updated shop names: ")
                print(Shop1.shopName)
                print(Shop2.shopName)
                print(Shop3.shopName)
                print(Shop4.shopName)
            
                      
            elif option_1 == "0":
                print(Fore.BLUE + "Going back..." + Fore.RESET)
                pass
            else:
                print(Fore.RED + "Invalid input!!!" + Fore.RESET)

        elif choice_2 == "2":
                print("Current shop Locations: ")
                print("1." ,Shop1.shopName ,Shop1.shopLocation)
                print("2." ,Shop2.shopName ,Shop2.shopLocation)
                print("3." ,Shop3.shopName ,Shop3.shopLocation)
                print("4." ,Shop4.shopName ,Shop4.shopLocation)
                    
                option_2 = input(Fore.CYAN + "select location to change: " + Fore.RESET)
                if option_2 == "1":

                    LocName_change = input(Fore.CYAN + "Change shop location(Free State,Gauteng,KZN,Limpopo,Default): " + Fore.RESET)
                    Shop1.shopLocation = LocName_change
                    print("Shop Location has been changed successfully to: ", LocName_change)
                    print("Updated shop Locations: ")
                    print("1." ,Shop1.shopName ,Shop1.shopLocation)
                    print("2." ,Shop2.shopName ,Shop2.shopLocation)
                    print("3." ,Shop3.shopName ,Shop3.shopLocation)
                    print("4." ,Shop4.shopName ,Shop4.shopLocation)

                elif option_2 == "2":

                    LocName_change = input(Fore.CYAN + "Change shop location(Free State,Gauteng,KZN,Limpopo,Default): " + Fore.RESET)
                    Shop2.shopLocation = LocName_change
                    print("Shop Location has been changed successfully to: ", LocName_change)
                    print("Updated shop Locations: ")
                    print("1." ,Shop1.shopName ,Shop1.shopLocation)
                    print("2." ,Shop2.shopName ,Shop2.shopLocation)
                    print("3." ,Shop3.shopName ,Shop3.shopLocation)
                    print("4." ,Shop4.shopName ,Shop4.shopLocation)

                elif option_2 == "3":

                    LocName_change = input(Fore.CYAN + "Change shop location(Free State,Gauteng,KZN,Limpopo,Default): " + Fore.RESET)
                    Shop3.shopLocation = LocName_change
                    print("Shop Location has been changed successfully to: ", LocName_change)
                    print("Updated shop Locations: ")
                    print("1." ,Shop1.shopName ,Shop1.shopLocation)
                    print("2." ,Shop2.shopName ,Shop2.shopLocation)
                    print("3." ,Shop3.shopName ,Shop3.shopLocation)
                    print("4." ,Shop4.shopName ,Shop4.shopLocation)

                elif option_2 == "4":

                    LocName_change = input(Fore.CYAN + "Change shop location(Free State,Gauteng,KZN,Limpopo,Default): " + Fore.RESET)
                    Shop4.shopLocation = LocName_change
                    print("Shop Location has been changed successfully to: ", LocName_change)
                    print("Updated shop Locations: ")
                    print("1." ,Shop1.shopName ,Shop1.shopLocation)
                    print("2." ,Shop2.shopName ,Shop2.shopLocation)
                    print("3." ,Shop3.shopName ,Shop3.shopLocation)
                    print("4." ,Shop4.shopName ,Shop4.shopLocation)                        

                else:
                    print(Fore.RED + "Invalid option" + Fore.RESET)

        elif choice_2 == "3":
                print("1." ,Shop1.shopName ,Shop1.shopLocation)
                print("2." ,Shop2.shopName ,Shop2.shopLocation)
                print("3." ,Shop3.shopName ,Shop3.shopLocation)
                print("4." ,Shop4.shopName ,Shop4.shopLocation)   

        elif choice_2 == "4":
#Create a final system to print out the changed information
            print(Fore.BLACK + "----------------------------------------------------" + Fore.RESET)
            print("Shop Name: ",Shop1.shopName)
            print("Shop Location: ",Shop1.shopLocation) 
            print("Sales: ",Shop1.sales) 
            print("Returns: ",Shop1.returns) 
            print("Customers: ",Shop1.customers)
            print(Fore.BLACK + "----------------------------------------------------" + Fore.RESET)

            print("Shop Name: ",Shop2.shopName)
            print("Shop Location: ",Shop2.shopLocation)
            print("Sales: ",Shop2.sales)
            print("Returns: ",Shop2.returns)
            print("Customers: ",Shop2.customers)
            print(Fore.BLACK + "----------------------------------------------------" + Fore.RESET)

            print("Shop Name: ",Shop3.shopName)
            print("Shop Location: ",Shop3.shopLocation)
            print("Sales: ",Shop3.sales)
            print("Returns: ",Shop3.returns)
            print("Customers: ",Shop3.customers)
            print(Fore.BLACK + "----------------------------------------------------" + Fore.RESET)

            print("Shop Name: " ,Shop4.shopName)
            print("Shop Location: ",Shop4.shopLocation)
            print("Sales: ",Shop4.sales)
            print("Returns: ",Shop4.returns)
            print("Customers: ",Shop4.customers)
            print(Fore.BLACK + "----------------------------------------------------" + Fore.RESET)

            
        elif choice_2 == "0":
            pass
        
        else:
            print(Fore.RED + "Invalid input!!!" + Fore.RESET)
#Create code to edit stock intake and out take
    elif choice == "2":
        print("1. Computer")
        print("2. RaspPi")
        print("3. Monitor")
        print("4. Back")

        option_3 = input(Fore.LIGHTBLUE_EX + "Select an item from the above options: " + Fore.RESET) 
        
        if option_3 == "1":
            print("You have selected Computer.")
            comp_num = input("How many computers would you like to purchase?: ")
            print("you have ordered", comp_num, "Computers.")
            
            print("1." ,Shop1.shopName, Shop1.shopLocation)
            print("2." ,Shop2.shopName, Shop2.shopLocation)
            print("3." ,Shop3.shopName, Shop3.shopLocation)
            print("4." ,Shop4.shopName, Shop4.shopLocation)

            shop_choice = input(Fore.LIGHTBLUE_EX + "From wich location would you like to order from?: " + Fore.RESET)
            
            
            if shop_choice == "1":
                stock_shop1["Computer"] = stock_shop1["Computer"] - int(comp_num)
                Shop1.customers = Shop1.customers + 1
                Shop1.sales = Shop1.sales + int(comp_num)
                print("Your order has been processed successfully to shop" , shop_choice, "!!!")

            elif shop_choice == "2":
                stock_shop2["Computer"] = stock_shop2["Computer"] - int(comp_num)
                Shop2.customers = Shop2.customers + 1
                Shop2.sales = Shop2.sales + int(comp_num)
                print("Your order has been processed successfully to shop" , shop_choice, "!!!")
                
            elif shop_choice == "3":
                stock_shop3["Computer"] = stock_shop3["Computer"] - int(comp_num)
                Shop3.customers = Shop3.customers + 1
                Shop3.sales = Shop3.sales + int(comp_num)
                print("Your order has been processed successfully to shop" , shop_choice, "!!!")

            elif shop_choice == "4":
                stock_shop4["Computer"] = stock_shop4["Computer"] - int(comp_num)
                Shop4.customers = Shop4.customers + 1
                Shop4.sales = Shop4.sales + int(comp_num)
                print("Your order has been processed successfully to shop" , shop_choice, "!!!")    

        elif option_3 == "2":
            print("you have selected RaspPi.")
            RaspPi_num = input(Fore.LIGHTBLUE_EX + "How many RaspPi's would you like to purchase?: " + Fore.RESET)
            print("you have ordered", RaspPi_num, "RaspPi's.")

            print("1." ,Shop1.shopName, Shop1.shopLocation)
            print("2." ,Shop2.shopName, Shop2.shopLocation)
            print("3." ,Shop3.shopName, Shop3.shopLocation)
            print("4." ,Shop4.shopName, Shop4.shopLocation)

            shop_choice = input(Fore.LIGHTBLUE_EX + "From wich location would you like to order from?: " + Fore.RESET)
            
            if shop_choice == "1":
                stock_shop1["RaspPi"] = stock_shop1["RaspPi"] - int(RaspPi_num)
                Shop1.customers = Shop1.customers + 1
                Shop1.sales = Shop1.sales + 1
                print("Your order has been processed successfully to shop" , shop_choice, "!!!")

            elif shop_choice == "2":
                stock_shop2["RaspPi"] = stock_shop2["RaspPi"] - int(RaspPi_num)
                Shop2.customers = Shop2.customers + 1
                Shop2.sales = Shop2.sales + 1
                print("Your order has been processed successfully to shop" , shop_choice, "!!!")
                
            elif shop_choice == "3":
                stock_shop3["RaspPi"] = stock_shop3["RaspPi"] - int(RaspPi_num)
                Shop3.customers = Shop3.customers + 1
                Shop3.sales = Shop3.sales + 1
                print("Your order has been processed successfully to shop" , shop_choice, "!!!")

            elif shop_choice == "4":
                stock_shop4["RaspPi"] = stock_shop4["RaspPi"] - int(RaspPi_num)
                Shop4.customers = Shop4.customers + 1
                Shop4.sales = Shop4.sales + 1
                print("Your order has been processed successfully to shop" , shop_choice, "!!!")

            else:
                print(Fore.RED + "Invalid input!" + Fore.RESET)
                break

        elif option_3 == "3":
            print("you have selected monitor.")
            Mon_num = input(Fore.LIGHTBLUE_EX + "How many monitors would you like to purchase?: " + Fore.RESET)
            print("you have ordered", Mon_num, " monitors.")

            print("1." ,Shop1.shopName, Shop1.shopLocation)
            print("2." ,Shop2.shopName, Shop2.shopLocation)
            print("3." ,Shop3.shopName, Shop3.shopLocation)
            print("4." ,Shop4.shopName, Shop4.shopLocation)
#Allows user to choose where their item comes from
            shop_choice = input(Fore.LIGHTBLUE_EX + "From wich location would you like to order from?: " + Fore.RESET)
            
            if shop_choice == "1":
                stock_shop1["Monitor"] = stock_shop1["Monitor"] - int(Mon_num)
                Shop1.customers = Shop1.customers + 1
                Shop1.sales = Shop1.sales + 1
                print("Your order has been processed successfully to shop" , shop_choice, "!!!")

            elif shop_choice == "2":
                stock_shop2["Monitor"] = stock_shop2["Monitor"] - int(Mon_num)
                Shop2.customers = Shop2.customers + 1
                Shop2.sales = Shop2.sales + 1
                print("Your order has been processed successfully to shop" , shop_choice, "!!!")
                
            elif shop_choice == "3":
                stock_shop3["Monitor"] = stock_shop3["Monitor"] - int(Mon_num)
                Shop3.customers = Shop3.customers + 1
                Shop3.sales = Shop3.sales + 1
                print("Your order has been processed successfully to shop" , shop_choice, "!!!")

            elif shop_choice == "4":
                stock_shop4["Monitor"] = stock_shop4["Monitor"] - int(Mon_num)
                Shop4.customers = Shop4.customers + 1
                Shop4.sales = Shop4.sales + 1
                print("Your order has been processed successfully to shop" , shop_choice, "!!!")

            else:
                print(Fore.RED + "Invalid Input!" + Fore.RESET)
                break

        elif option_3 == "4":
            print(Fore.BLUE + "Going back..." + Fore.RESET)
            pass
        
        else:
            print(Fore.RED + "Invalid Input!" + Fore.RESET)
            break
#Create code that focuses on the math of the returns in each store
    elif choice == "3":
        print("1. Computer")
        print("2. RaspPi")
        print("3. Monitor")
        print("4. Exit")

        prompt = input(Fore.LIGHTBLUE_EX + "What item would you like to return?: " + Fore.RESET)
        prompt_2 = input(Fore.LIGHTBLUE_EX + "How much of the item would you like to return?: "  + Fore.RESET)

        print("1." ,Shop1.shopName, Shop1.shopLocation)
        print("2." ,Shop2.shopName, Shop2.shopLocation)
        print("3." ,Shop3.shopName, Shop3.shopLocation)
        print("4." ,Shop4.shopName, Shop4.shopLocation)
        prompt_3 = input(Fore.LIGHTBLUE_EX + "Which store would you like to return the product/products to?: " + Fore.RESET)

        if prompt == "1":
            if prompt_3 == "1":
                print(Fore.BLUE + "Returning to shop 1..." + Fore.RESET)
                Shop1.returns = Shop1.returns + 1
                Shop1.sales = Shop1.sales - int(prompt_2)

            elif prompt_3 == "2":
                print(Fore.BLUE + "Returning to shop 2..." + Fore.RESET)
                Shop2.returns = Shop2.returns + 1
                Shop2.sales = Shop2.sales - int(prompt_2)

            elif prompt_3 =="3":
                print(Fore.BLUE + "Returning to shop 3..." + Fore.RESET)
                Shop3.returns = Shop3.returns + 1
                Shop3.sales = Shop3.sales - int(prompt_2)

            elif prompt_3 == "4":
                print(Fore.BLUE + "Returning to shop 4..." + Fore.RESET)
                Shop4.returns = Shop4.returns + 1
                Shop4.sales = Shop4.sales - int(prompt_2)

        if prompt == "2":
            if prompt_3 == "1":
                print(Fore.BLUE + "Returning to shop 1..." + Fore.RESET)
                Shop1.returns = Shop1.returns + 1
                Shop1.sales = Shop1.sales - int(prompt_2)

            elif prompt_3 == "2":
                print(Fore.BLUE + "Returning to shop 2..." + Fore.RESET)
                Shop2.returns = Shop2.returns + 1
                Shop2.sales = Shop2.sales - int(prompt_2)

            elif prompt_3 =="3":
                print(Fore.BLUE + "Returning to shop 3..." + Fore.RESET)
                Shop3.returns = Shop3.returns + 1
                Shop3.sales = Shop3.sales - int(prompt_2)

            elif prompt_3 == "4":
                print(Fore.BLUE + "Returning to shop 4..." + Fore.RESET)
                Shop4.returns = Shop4.returns + 1
                Shop4.sales = Shop4.sales - int(prompt_2)

        if prompt == "3":
            if prompt_3 == "1":
                print(Fore.BLUE + "Returning to shop 1..." + Fore.RESET)
                Shop1.returns = Shop1.returns + 1
                Shop1.sales = Shop1.sales - int(prompt_2)

            elif prompt_3 == "2":
                print(Fore.BLUE + "Returning to shop 2..." + Fore.RESET)
                Shop2.returns = Shop2.returns + 1
                Shop2.sales = Shop2.sales - int(prompt_2)

            elif prompt_3 =="3":
                print(Fore.BLUE + "Returning to shop 3..." + Fore.RESET)
                Shop3.returns = Shop3.returns + 1
                Shop3.sales = Shop3.sales - int(prompt_2)

            elif prompt_3 == "4":
                print(Fore.BLUE + "Returning to shop 4..." + Fore.RESET)
                Shop4.returns = Shop4.returns + 1
                Shop4.sales = Shop4.sales - int(prompt_2)

        if prompt == "4":
            print(Fore.BLUE + "Exiting..." + Fore.RESET)
            exit()
#Code to display and add stock. it must also do the math to add to current stock
    elif choice == "4":
        print("1. Display stock")
        print("2. Add Stock")
        print("0. Back")

        stock_input = input(Fore.LIGHTBLUE_EX + "Select the number of what you would you like to do: " + Fore.RESET)
        if stock_input == "1":
            print("Stock for shop 1: " + str(stock_shop1) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")
            print("Stock for shop 2: " + str(stock_shop2) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")
            print("Stock for shop 3: " + str(stock_shop3) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")
            print("Stock for shop 4: " + str(stock_shop4) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")

        elif stock_input == "2":
            print("1." ,stock_shop1)
            print("2." ,stock_shop2)
            print("3." ,stock_shop3)
            print("4." ,stock_shop4)

            stock_prompt = input(Fore.LIGHTBLUE_EX + "Which store would you like to re-Stock?: " + Fore.RESET)
            stock_prompt_2 = input(Fore.LIGHTBLUE_EX + "Which product would you like to add stock to? 1.Computer ,2.RaspPi, 3.Monitor: " + Fore.RESET)
            stock_prompt_3 = input(Fore.LIGHTBLUE_EX + "How much of the chosen item would you like to add to the stock?: " + Fore.RESET)

            if stock_prompt == "1":
                if stock_prompt_2 == "1":
                    stock_shop1["Computer"] = stock_shop1["Computer"] + int(stock_prompt_3)
                    print("Stock for shop 1 has been updated to: " + str(stock_shop1) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")
                
                elif stock_prompt_2 == "2":
                    stock_shop1["RaspPi"] = stock_shop1["RaspPi"] + int(stock_prompt_3)
                    print("Stock for shop 1 has been updated to: " + str(stock_shop1) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")

                elif stock_prompt_2 == "3":
                    stock_shop1["Monitor"] = stock_shop1["Monitor"] + int(stock_prompt_3)
                    print("Stock for shop 1 has been updated to: " + str(stock_shop1) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")

            if stock_prompt == "2":
                if stock_prompt_2 == "1":
                    stock_shop2["Computer"] = stock_shop2["Computer"] + int(stock_prompt_3)
                    print("Stock for shop 2 has been updated to: " + str(stock_shop2) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")
                
                elif stock_prompt_2 == "2":
                    stock_shop2["RaspPi"] = stock_shop2["RaspPi"] + int(stock_prompt_3)
                    print("Stock for shop 2 has been updated to: " + str(stock_shop1) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")

                elif stock_prompt_2 == "3":
                    stock_shop2["Monitor"] = stock_shop2["Monitor"] + int(stock_prompt_3)
                    print("Stock for shop 2 has been updated to: " + str(stock_shop2) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")    

            if stock_prompt == "3":
                if stock_prompt_2 == "1":
                    stock_shop3["Computer"] = stock_shop3["Computer"] + int(stock_prompt_3)
                    print("Stock for shop 3 has been updated to: " + str(stock_shop3) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")
                
                elif stock_prompt_2 == "2":
                    stock_shop3["RaspPi"] = stock_shop3["RaspPI"] + int(stock_prompt_3)
                    print("Stock for shop 3 has been updated to: " + str(stock_shop3) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")

                elif stock_prompt_2 == "3":
                    stock_shop3["Monitor"] = stock_shop3["Monitor"] + int(stock_prompt_3)
                    print("Stock for shop 3 has been updated to: " + str(stock_shop3) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")

            if stock_prompt == "4":
                if stock_prompt_2 == "1":
                    stock_shop4["Computer"] = stock_shop4["Computer"] + int(stock_prompt_3)
                    print("Stock for shop 4 has been updated to: " + str(stock_shop4) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")
                
                elif stock_prompt_2 == "2":
                    stock_shop4["RaspPi"] = stock_shop4["RaspPi"] + int(stock_prompt_3)
                    print("Stock for shop 4 has been updated to: " + str(stock_shop4) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")

                elif stock_prompt_2 == "3":
                    stock_shop4["Monitor"] = stock_shop4["Monitor"] + int(stock_prompt_3)
                    print("Stock for shop 4 has been updated to: " + str(stock_shop4) + " At R2500  per Computer, R100 per RaspPi, and R800 per Monitor")
        elif stock_input == "0":
            print(Fore.BLUE + "Going back..." + Fore.RESET)
            pass
#Closing statement for the stock code.
    elif choice == "99":
        print(Fore.GREEN + "Thank you for using our service, please come again!!!" + Fore.RESET)
        break
    else:
        print(Fore.RED + "Invalid input!!!" + Fore.RESET)