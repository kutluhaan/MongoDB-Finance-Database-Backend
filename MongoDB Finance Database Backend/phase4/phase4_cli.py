from mongobackend import *

def new_user(user_name):
    user = {
        "portfolios": {},
        "name": user_name
    }
    return user

def new_port(port_name):
    new_port = {
        "name": port_name,
        "content" : {
            "natural_resources": {},
            "exchanges": {},
            "stocks": {}
        }
    }
    
    return new_port

    

if __name__ == "__main__":
    database = connect()
    all_collections = database.list_collection_names()
    print("Would you like to create a collection (1)")
    print("or choose and login to an existing one? (2)")
    print("(0 to exit)")
    collection_choice = int(input("\nYour choice: "))
    while True:
        if collection_choice == 2 and all_collections:
            break
        elif collection_choice == 2 and not all_collections:
            print("\nNo collections available!")
        elif collection_choice == 1:
            new_collection_name = input("\nEnter the name of your new collection: ")
            create_collection(database,new_collection_name)
        elif collection_choice == 0:
            print("Thank you for using our application.")
            exit()
        else:
            print("Invalid input, try again.")
        print("\nWould you like to create a collection (1)")
        print("or choose and login to an existing one? (2)")
        print("(0 to exit)")
        collection_choice = int(input("\nYour choice: "))

    print("Please choose your preferred platform.")
    i = 1
    for collect in all_collections:
        print(str(i) + " - " + str(collect))
        i += 1

    chosen_coll_index = int(input("Chosen collection number: "))
    colName = all_collections[chosen_coll_index - 1]

    all_users = get_collection(db=database, collection_name=colName)

    print("\nWelcome to your portfolio testing platform!")
    print("Would you like to register a new account (1)")
    print("or choose and login to an existing one? (2)")
    print("(0 to exit)")
    username_choice = int(input("\nYour choice: "))
    while True:
        if username_choice == 2 and all_collections:
            username = input("\nPlease enter your username: ")
            if is_user(database, colName, username):
                break
            else:
                print("This user doesn't exist!")
        elif username_choice == 2 and not all_collections:
            print("\nNo collections available!")
        elif username_choice == 1:
            new_username = input("\nEnter your preferred username: ")
            
            user = new_user(user_name=new_username)
            
            if new_username not in all_users:
                insert_user(database, colName, user)
            else:
                print("\n")
        elif username_choice == 0:
            print("Thank you for using our application.")
            exit()
        else:
            print("Invalid input, try again.")
        print("\nWould you like to register a new account (1)")
        print("or choose and login to an existing one? (2)")
        print("(0 to exit)")
        username_choice = int(input("\nYour choice: "))

    option = -1

    while option != 0 and is_connected(database):
        print("What would you like to do? (Type a number 0-6)")
        print("    1 - Create a new portfolio.")
        print("    2 - List all contents of a portfolio.")
        print("    3 - Filter and list the contents of a portfolio.")
        print("    4 - Insert an entry.")
        print("    5 - Delete an entry.")
        print("    6 - Update an entry.")
        print("    0 - Exit the application.", end="\n\n")

        portfolioList = get_user_portfolio_names(database, colName, username)

        option = int(input("Your choice: "))
        print("")

        if option == 0:
            print("Thanks for using the platform. Good luck!")
            exit()
        elif option == 1:
            print("What would you like to call your new portfolio?")
            portfolioName = input()
            print("")
            new_portfolio = new_port(port_name=portfolioName)
            insert_portfolio(database, colName, username, new_portfolio)
        elif option == 2:
            if portfolioList:
                print("Which portfolio would you like to list? (Type a number 1-" + str(len(portfolioList)) + ")" )
                deneme = 1
                for portfolio in portfolioList:
                    print(str(deneme) + " - " + str(portfolio))
                    deneme += 1
                portfolioNum = int(input("Portfolio number: "))
                read_with_filter(db=database, collection_name=colName, user_name=username, portfolio_name=portfolioList[portfolioNum - 1], query="portfolio")
            else:
                print("You have no portfolios available!")
        elif option == 3:
            if not portfolioList:
                print("You have no portfolios available!")
            else:
                print("Which portfolio would you like to see? (Type a number 1-" + str(len(portfolioList)) + ")" )
                deneme = 1
                for portfolio in portfolioList:
                    print(str(deneme) + " - " + str(portfolio))
                    deneme += 1
                portfolioNum = int(input("Portfolio number: "))
                print("What type of asset would you like to see? (Type a number 1-3)")
                print("    1 - Stock")
                print("    2 - Foreign Exchange")
                print("    3 - Precious Resources")
                assetType = int(input("Asset type: "))
                if assetType == 1:
                    read_with_filter(database,colName,username,portfolioList[portfolioNum-1],"stocks")
                elif assetType == 2:
                    read_with_filter(database, colName, username, portfolioList[portfolioNum - 1], "exchanges")
                elif assetType == 3:
                    read_with_filter(database, colName, username, portfolioList[portfolioNum - 1], "natural_resources")
                else:
                    print("\nThat filter doesn't exist!")
        elif option == 4:
            if not portfolioList:
                print("You have no portfolios available!")
            else:
                print("Which portfolio would you like to add an asset to? (Type a number 1 - " + str(len(portfolioList)) + ")" )
                deneme = 1
                for portfolio in portfolioList:
                    print(str(deneme) + " - " + str(portfolio))
                    deneme += 1
                portfolioNum = int(input("Portfolio number: "))
                print("What type of asset would you like to insert? (Type a number 1-3)")
                print("    1 - Stock")
                print("    2 - Foreign Exchange")
                print("    3 - Precious Resources")
                assetType = int(input("Asset type: "))
                assetName = input("Asset name:")
                assetAmount = input("Asset amount (in Turkish Lira ₺):")
                if assetType == 1:
                    insert_stock(database, colName, username, portfolioList[portfolioNum-1], {"name": assetName, "amount": assetAmount})
                elif assetType == 2:
                    insert_exchange(database, colName, username, portfolioList[portfolioNum-1], {"name": assetName,"type":assetName , "amount": assetAmount})
                elif assetType == 3:
                    insert_resource(database, colName, username, portfolioList[portfolioNum-1], {"name": assetName,"type":assetName, "amount": assetAmount})
        elif option == 5:
            if not portfolioList:
                print("You have no portfolios available!")
            else:
                print("Which portfolio would you like to list? (Type a number 1-" + str(len(portfolioList)) + ")" )
                deneme = 1
                for portfolio in portfolioList:
                    print(str(deneme) + " - " + str(portfolio))
                    deneme += 1
                portfolioNum = int(input("Portfolio number: "))
                print("What type of asset would you like to delete? (Type a number 1-3)")
                print("    1 - Foreign Exchange")
                print("    2 - Stock")
                print("    3 - Precious Minerals")
                assetType = int(input("Asset type: "))
                assetName = input("Asset name:")
                if assetType == 2:
                    delete_stock(database, colName, username, portfolioList[portfolioNum - 1], assetName)
                elif assetType == 1:
                    delete_exchange(database, colName, username, portfolioList[portfolioNum - 1], assetName)
                elif assetType == 3:
                    delete_resource(database, colName, username, portfolioList[portfolioNum - 1], assetName)
        elif option == 6:
            if not portfolioList:
                print("You have no portfolios available!")
            else:
                print("Which portfolio would you like to list? (Type a number 1-" + str(len(portfolioList)) + ")" )
                deneme = 1
                for portfolio in portfolioList:
                    print(str(deneme) + " - " + str(portfolio))
                    deneme += 1
                portfolioNum = int(input("Portfolio number: "))
                print("What type of asset would you like to update? (Type a number 1-3)")
                print("    1 - Foreign Exchange")
                print("    2 - Stock")
                print("    3 - Precious Minerals")
                assetType = int(input("Asset type: "))
                assetName = input("Asset name:")
                assetAmount = int(input("Asset amount (in Turkish Lira ₺):"))
                if assetType == 2:
                    update_stock(database, colName, username, portfolioList[portfolioNum - 1], assetName, assetAmount)
                elif assetType == 1:
                    update_exchange(database, colName, username, portfolioList[portfolioNum - 1], assetName, assetAmount)
                elif assetType == 3:
                    update_resource(database, colName, username, portfolioList[portfolioNum - 1], assetName, assetAmount)