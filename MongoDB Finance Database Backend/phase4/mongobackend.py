import pymongo
import pprint


def is_connected(db):
    try: 
        db.command('ping')
        return True
    except:
        return False

def connect():
    try:
        connection_string = "mongodb+srv://kutluhan:1453Kutlu52@cluster0.tlttpeg.mongodb.net/bank_app?retryWrites=true&w=majority"
        # Connect to MongoDB Atlas
        client = pymongo.MongoClient(connection_string)
        
        # Access or create the specified database
        db = client.bank_app
        
        print(f"Successfully connected to database")
        
        return db
    except Exception as error:
        print("Database could not be created:", error)

def create_collection(db, collection_name):
    try:
        if len(db.list_collection_names()) == 0 or collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print(f"Collection {collection_name} created successfully!")
        else:
            print(f"Collection {collection_name} is already present!")
    except Exception as error:
        print("Collection could not be created:", error)

def get_user_portfolio_names(db, collection_name, user_name):
    try:
        collection = db[collection_name]
        query = {"name": user_name}
        user_data = collection.find_one(query)

        if user_data:
            portfolios = user_data.get("portfolios", {})
            portfolio_names = list(portfolios.keys())
            return portfolio_names
        else:
            print(f"{user_name} does not have any portfolios")
            return []
    except Exception as error:
        print("Error fetching user portfolio names:", error)
        return []

def get_collection(db, collection_name):
    try:
        collection = db[collection_name]
        dataset = collection.find()
        return list(dataset)
    except Exception as error:
        print("Data could not be read", error) 
   

def print_all_collection(db, collection_name):
    try:
        collection = db[collection_name]
        dataset = collection.find()
        dataset = list(dataset)
        if len(dataset) != 0:
            pprint.pprint(dataset, width=40)
        else:
            print("Collection is empty")
        return dataset
    except Exception as error:
        print("Data could not be read", error) 

def read_with_filter(db, collection_name, user_name, portfolio_name, query):
    try: 
        collection = db[collection_name]
        dataset = None
        user_query = {"name": user_name}
        user_data = collection.find_one(user_query)
        
        if user_data:
            portfolios = user_data.get("portfolios", {})
            if portfolio_name in portfolios:
                portfolio = portfolios[portfolio_name]
                
                if query == "exchanges":
                    dataset = portfolio["content"]["exchanges"]
                    
                elif query == "natural_resources":
                    dataset = portfolio["content"]["natural_resources"]
                    
                elif query == "stocks":
                    dataset = portfolio["content"]["stocks"]
                
                else:
                    dataset = portfolio["content"]
                
                if len(dataset) != 0:
                    pprint.pprint(dataset, width=40)
                else:
                    print("Dataset is empty")
                    
            else:
                print(f"Portfolio '{portfolio_name}' not found for user '{user_name}'")
        else:
            print(f"User '{user_name}' not found")
        
            
    except Exception as error:
        print("Data could not be read", error)

def is_user(db, collection_name, user_name):
    try:
        collection = db[collection_name]
        user = collection.find_one({"name": user_name})
        if user:
            print(f"{user_name} is a user")
            return True  # User found in the database
        else:
            print(f"{user_name} is not a user")
            return False  # User not found in the database
    except Exception as e:
        print("An error occurred:", e)
        return False  # Return False in case of any exception or error
    


def insert_stock(db, collection_name, user_name, portfolio_name, new_stock):
    try:
        collection = db[collection_name]
        user_query = {"name": user_name}
        user_data = collection.find_one(user_query)
        if user_data:
            portfolios = user_data.get("portfolios", {})
            if portfolio_name in portfolios:
                update_result = collection.update_one(
                    {"name": user_name},
                    {"$set": {f"portfolios.{portfolio_name}.content.stocks.{new_stock['name']}": new_stock}}
                )
                if update_result.modified_count > 0:
                    print(f"New stock '{new_stock}' is added successfully to the stocks.")
                else:
                    print("Failed to add the new stock.")
            else:
                print("Given portfolio is not present for user")
        else:
            print(f"{user_name} not found!")
    except Exception as error:
        print("An error occurred", error)

def insert_resource(db, collection_name, user_name, portfolio_name, new_resource):
    try:
        collection = db[collection_name]
        user_query = {"name": user_name}
        user_data = collection.find_one(user_query)
        if user_data:
            portfolios = user_data.get("portfolios", {})
            if portfolio_name in portfolios:
                update_result = collection.update_one(
                    {"name": user_name},
                    {"$set": {f"portfolios.{portfolio_name}.content.natural_resources.{new_resource['name']}": new_resource}}
                )
                if update_result.modified_count > 0:
                    print(f"New resource '{new_resource}' is added successfully to the natural resources.")
                else:
                    print("Failed to add the new resource.")
            else:
                print("Given portfolio is not present for user")
        else:
            print(f"{user_name} not found!")
    except Exception as error:
        print("An error occurred", error)

def insert_exchange(db, collection_name, user_name, portfolio_name, new_exchange):
    try:
        collection = db[collection_name]
        user_query = {"name": user_name}
        user_data = collection.find_one(user_query)
        if user_data:
            portfolios = user_data.get("portfolios", {})
            if portfolio_name in portfolios:
                update_result = collection.update_one(
                    {"name": user_name},
                    {"$set": {f"portfolios.{portfolio_name}.content.exchanges.{new_exchange['name']}": new_exchange}}
                )
                if update_result.modified_count > 0:
                    print(f"New exchange '{new_exchange}' added successfully to the exchanges.")
                else:
                    print("Failed to add the new exchange.")
            else:
                print("Given portfolio is not present for user")
        else:
            print(f"{user_name} not found!")
        
    except Exception as error:
        print("An error occurred", error)

def insert_portfolio(db, collection_name, user_name, newportfolio):
       try:
            collection = db[collection_name]
            user_query = {"name": user_name}
            user_data = collection.find_one(user_query)
            if user_data:
                portfolios = user_data.get("portfolios", {})
                if newportfolio['name'] not in portfolios:
                    update_result = collection.update_one(
                        {"name": user_name},
                        {"$set": {f"portfolios.{newportfolio['name']}": newportfolio}}
                    )
                if update_result.modified_count > 0:
                    print(f"New portfolio '{newportfolio}' is added successfully to the portfolios.")
                else:
                    print("Failed to add the new portfolio.")
            else:
                print(f"{user_name} could not be found!")
       except Exception as error:
           print("Something went wrong", error)

def insert_user(db, collection_name, user):
    try:
        collection = db[collection_name]
        collection.insert_one(user)
        print(f"{user} is inserted succesfully")
    except Exception as error:
        print("Data could not be inserted", error) 



def delete_stock(db, collection_name, user_name, portfolio_name, stock_name):
    try:
        collection = db[collection_name]
        user_query = {"name": user_name}
        user_data = collection.find_one(user_query)
        if user_data:
            portfolios = user_data.get("portfolios", {})
            if portfolio_name in portfolios:
                update_result = collection.update_one(
                    {"name": user_name, f"portfolios.{portfolio_name}.content.stocks.{stock_name}": {"$exists": True}},
                    {"$unset": {f"portfolios.{portfolio_name}.content.stocks.{stock_name}": ""}}
                )

                if update_result.modified_count > 0:
                    print(f"Stock '{stock_name}' is deleted successfully from the portfolio {portfolio_name}.")
                else:
                    print("Failed to delete the stock.")
            else:
                print(f"{portfolio_name} is not present for the {user_name}")
        else:
            print(f"{user_name} is not present")
    except Exception as error:
        print("An error occurred", error)
        
def delete_resource(db, collection_name, user_name, portfolio_name, resource_name):
    try:
        collection = db[collection_name]
        user_query = {"name": user_name}
        user_data = collection.find_one(user_query)
        if user_data:
            portfolios = user_data.get("portfolios", {})
            if portfolio_name in portfolios:
                update_result = collection.update_one(
                    {"name": user_name, f"portfolios.{portfolio_name}.content.natural_resources.{resource_name}": {"$exists": True}},
                    {"$unset": {f"portfolios.{portfolio_name}.content.natural_resources.{resource_name}": ""}}
                )

                if update_result.modified_count > 0:
                    print(f"Natural resource '{resource_name}' is deleted successfully from the portfolio {portfolio_name}.")
                else:
                    print("Failed to delete the natural resource.")
            else:
                print(f"{portfolio_name} is not present for the {user_name}")
        else:
            print(f"{user_name} is not present")
    except Exception as error:
        print("An error occurred", error)

def delete_exchange(db, collection_name, user_name, portfolio_name, exchange_name):
    try:
        collection = db[collection_name]
        user_query = {"name": user_name}
        user_data = collection.find_one(user_query)
        if user_data:
            portfolios = user_data.get("portfolios", {})
            if portfolio_name in portfolios:
                update_result = collection.update_one(
                    {"name": user_name, f"portfolios.{portfolio_name}.content.exchanges.{exchange_name}": {"$exists": True}},
                    {"$unset": {f"portfolios.{portfolio_name}.content.exchanges.{exchange_name}": ""}}
                )

                if update_result.modified_count > 0:
                    print(f"Exchange '{exchange_name}' is deleted successfully from the portfolio {portfolio_name}.")
                else:
                    print("Failed to delete the exchange.")
            else:
                print(f"{portfolio_name} is not present for the {user_name}")
        else:
            print(f"{user_name} is not present")
    except Exception as error:
        print("An error occurred", error)
        
def delete_portfolio(db, collection_name, user_name, portfolio_name):
    try:
        collection = db[collection_name]
        user_query = {"name": user_name}
        user_data = collection.find_one(user_query)
        if user_data:
            portfolios = user_data.get("portfolios", {})
            if portfolio_name in portfolios:
                update_result = collection.update_one(
                    {"name": user_name, f"portfolios.{portfolio_name}": {"$exists": True}},
                    {"$unset": {f"portfolios.{portfolio_name}": ""}}
                )

                if update_result.modified_count > 0:
                    print(f"Portfolio '{portfolio_name}' is deleted successfully for user {user_name}.")
                else:
                    print("Failed to delete the portfolio.")
            else:
                print(f"{portfolio_name} is not present for the {user_name}")
        else:
            print(f"{user_name} is not present")
    except Exception as error:
        print("An error occurred", error)

def delete_user(db, collection_name, user_name):
    try:
        collection = db[collection_name]
        user_query = {"name": user_name}
        user_data = collection.find_one(user_query)
        if user_data:
            delete_result = collection.delete_one({"name": user_name})

            if delete_result.deleted_count > 0:
                print(f"User '{user_name}' is deleted successfully.")
            else:
                print("Failed to delete the user.")
        else:
            print(f"{user_name} is not present")
    except Exception as error:
        print("An error occurred", error)



def update_stock(db, collection_name, user_name, portfolio_name, stock_name, new_amount):
    try:
        collection = db[collection_name]
        user_query = {"name": user_name}
        user_data = collection.find_one(user_query)
        if user_data:
            update_result = collection.update_one(
                {"name": user_name, f"portfolios.{portfolio_name}.content.stocks.{stock_name}": {"$exists": True}},
                {"$set": {f"portfolios.{portfolio_name}.content.stocks.{stock_name}.amount": new_amount}}
            )

            if update_result.modified_count > 0:
                print(f"Stock '{stock_name}' is updated successfully to '{new_amount}'.")
            else:
                print("Failed to update the stock.")
        else:
            print(f"{user_name} is not present")
    except Exception as error:
        print("An error occurred", error)
        
def update_resource(db, collection_name, user_name, portfolio_name, resource_name, new_value):        
    try:
        collection = db[collection_name]
        user_query = {"name": user_name}
        user_data = collection.find_one(user_query)
        if user_data:
            update_result = collection.update_one(
                {"name": user_name, f"portfolios.{portfolio_name}.content.natural_resources.{resource_name}": {"$exists": True}},
                {"$set": {f"portfolios.{portfolio_name}.content.natural_resources.{resource_name}.amount": new_value}}
            )

            if update_result.modified_count > 0:
                print(f"Natural resource '{resource_name}' is updated successfully to '{new_value}'.")
            else:
                print("Failed to update the resource.")
        else:
            print(f"{user_name} is not present")
    except Exception as error:
        print("An error occurred", error)

def update_exchange(db, collection_name, user_name, portfolio_name, exchange_name, new_value):
    try:
        collection = db[collection_name]
        user_query = {"name": user_name}
        user_data = collection.find_one(user_query)
        if user_data:
            update_result = collection.update_one(
                {"name": user_name, f"portfolios.{portfolio_name}.content.exchanges.{exchange_name}": {"$exists": True}},
                {"$set": {f"portfolios.{portfolio_name}.content.exchanges.{exchange_name}.amount": new_value}}
            )

            if update_result.modified_count > 0:
                print(f"Exchange '{exchange_name}' is updated successfully to '{new_value}'.")
            else:
                print("Failed to update the exchange.")
        else:
            print(f"{user_name} is not present")
    except Exception as error:
        print("An error occurred", error)

def update_user(db, collection_name, user_name, new_name):
    try:
        collection = db[collection_name]
        update_result = collection.update_one(
            {"name": user_name},
            {"$set": {"name": new_name}}
        )

        if update_result.modified_count > 0:
            print(f"{user_name}'s name updated to '{new_name}' succesfully.")
        else:
            print("Failed to update the user's name.")
    except Exception as error:
        print("An error occurred", error)