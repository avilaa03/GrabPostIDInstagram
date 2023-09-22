import mysql.connector

class MySql():

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
    )

    def insert_pub_id(self, list):

        mycursor = self.mydb.cursor()

        sql = "INSERT INTO nomedatabela name VALUES (%s)"

        val = list

        mycursor.executemany(sql, val)

        self.mydb.commit()

    def insert_pub_id(self, comments, date, id):

        mycursor = self.mydb.cursor()

        sql = "INSERT INTO nomedatabela name VALUES (%s, %s, %s, )"

        val = list

        mycursor.executemany(sql, val)

        self.mydb.commit()