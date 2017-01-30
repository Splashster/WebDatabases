import mysql.connector 
from mysql.connector import errorcode
from Database import *

'''
Create shop database if it does not exist
'''
def create_db(cursor):
	try:
		cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db))
	except mysql.connector.Error as err:
		print "Failed creating datbase: {}".format(err)
		exit(1)


'''
Create user defined tables if it does not exist
'''
def create_table(cursor, table_nm, fields):
	command = "CREATE TABLE IF NOT EXISTS " + table_nm  + " " + fields + " ENGINE=InnoDB"
	print command
	cursor.execute(command)


'''
Insert items to user defined tables
'''
def insert_items(cursor, table_nm, fields, values):
	command = "INSERT INTO " + table_nm + " " + fields + " VALUES " + values
	print command
	cursor.execute(command)


'''
Try to connect to the database.
If database does not exist, create the database.
If administrator user does not exist, create user.
'''
try:
	con = mysql.connector.connect(user=user, password=passwd, host=host,database= db)
	cursor = con.cursor(buffered=True)
except mysql.connector.Error as err:		
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print "Soemthing is wrong with your user name or password"
		exit(1)
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
       		print "Database does not exist! Attempting to create " + db + "...."
		con = mysql.connector.connect(user=user, password=passwd)
		cursor = con.cursor(buffered=True)
		create_db(cursor)
		print "Database " + db + " sucessfully created!"
		con.database = db

create_table(cursor, "`UserAccounts`", "(`first_name` varchar(14) NOT NULL, `last_name` varchar(16) NOT NULL,"
		     "`user_id` varchar (15) NOT NULL, `password` varchar(16) NOT NULL, `email` varchar(50) NOT NULL)")

create_table(cursor, "`Inventory`", "(`prod_id` varchar(10) NOT NULL, `prod_name` varchar(20) NOT NULL,`description`"
		     "varchar(50), `price` decimal(9,2) NOT NULL, `in_cart` int NOT NULL DEFAULT 0)")
		
insert_items(cursor, "`Inventory`","(`prod_id`,`prod_name`,`description`,`price`,`in_cart`)","('1239239CR','ServerT','Server Tower'"
		     ", 10.95,'')")
cursor.execute("select * from Inventory")

result = cursor.fetchall()

for row in result:
	print row
	
cursor.close()
con.close()	
	
	
