import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","python123","python" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
name = raw_input("enter your first name")
last = raw_input("enter your last name")
age = int(raw_input("enter your age"))
sex = raw_input("enter your sex")
income = int(raw_input("enter your income"))

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) \
         VALUES (%s, %s, %s, %s, %s);"
try:
   # Execute the SQL command
   cursor.execute(sql, (name, last, age, sex, income))
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
