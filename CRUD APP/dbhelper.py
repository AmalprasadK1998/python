"""Database logic!"""

import mysql.connector
import sys

class DBhelper:

    def __init__(self):
        try:
            # returns a connection object
            self.conn = mysql.connector.connect(host="localhost",
                                                username = "root",
                                                password = "",
                                                database = "crud app")

            # Always use the cursor object to talk to the database!
            # cursor is a class specifically created to interact with database!
            self.mycursor = self.conn.cursor()

        except:
            print("Some error occured,couldn't connect to database!")
            sys.exit(0)



        else:
            print("Connected to database")


    def register(self,name,email,password):

        try:

            self.mycursor.execute("""
            INSERT INTO `users` (`id`, `Name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}');""".format(name,email,password))
            self.conn.commit()

        except:

            return -1

        else:
            return 1

    def search(self,email,password):

        # By executing the query with SELECT , we retrieve the information from the database and store it in mycursor object!
        self.mycursor.execute("""
        SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'""".format(email,password))

        data = self.mycursor.fetchall()

        return data




