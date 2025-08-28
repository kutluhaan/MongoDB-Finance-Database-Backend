💰 MongoDB Finance Database Backend
📝 What's This All About?
Hey there! This is the backend code for a finance and user operations database. It's built to handle all the tricky stuff like managing user portfolios and keeping track of different assets like stocks, exchanges, and natural resources. Think of it as the brain behind a finance app, making sure all the data is safe, sound, and ready to go! It also has a basic command-line interface so you can test out all the functions.

🚀 What Can It Do?
User Management: Create and manage user accounts with their own unique portfolios.

Portfolio Operations: Add, update, and delete different portfolios for each user.

Asset Tracking: Keep a close eye on various assets like stocks, foreign exchanges, and precious minerals.

Data Manipulation: Perform all the essential database operations, like inserting, reading, updating, and deleting data.

Database Connection: Connects directly to a MongoDB Atlas cluster, which is a great cloud-based database service.

⚙️ What's Under the Hood?
This project is built with Python and uses the MongoDB database.

Python: Our go-to language for the backend logic.

PyMongo: The official Python driver for MongoDB. This is how we talk to the database!

MongoDB: A powerful NoSQL database that's perfect for handling flexible and complex data.

🛠️ How to Get Started
To get this running on your machine, you'll need to set up a MongoDB database first.

Clone the repo:

git clone https://github.com/kutluhaan/MongoDB-Finance-Database-Backend.git
cd MongoDB-Finance-Database-Backend

Install the dependencies:
You'll only need pymongo to get this running.

pip install pymongo

Set up your MongoDB Atlas connection:

Create a free account on MongoDB Atlas.

Create a new cluster and get your connection string.

Important! Open the mongobackend.py file and replace the connection_string variable with your own.

Run the script:
You can run the command-line interface to start using the backend.

python "MongoDB Finance Database Backend/phase4/phase4_cli.py"

This will connect to your database and give you a menu to interact with it.

⚖️ The Boring Stuff (The License)
This project is licensed under the MIT License, which means you can use it however you want! Check out the LICENSE file for all the details.

🙏 A Big Thank You!
MongoDB: For their fantastic database and the great documentation!

The PyMongo team: For an excellent library that makes it easy to work with MongoDB in Python.
