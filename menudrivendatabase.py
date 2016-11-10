import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","python123","python" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
print "tell us your choice:insert, read or delete"
x = raw_input("enter your choice: ")
if x == "insert" :
    idn = raw_input("enter ur no.: ")
    name = raw_input("enter your first name: ")
    last = raw_input("enter your last name: ")
    age = int(raw_input("enter your age: "))
    sex = raw_input("enter your sex: ")
    income = int(raw_input("enter your income: "))

    sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) \
        VALUES (%s, %s, %s, %s, %s);"
    try:
        cursor.execute(sql, (name, last, age, sex, income))
        db.commit()
        print "Record Inserted"
    except:
        print "============ Error ================"
        db.rollback()

if x == "read" :
    idn = raw_input("enter name: ")
    sql = "SELECT * FROM EMPLOYEE WHERE FIRST_NAME = %s"
    try:
        cursor.execute(sql, idn)
        results = cursor.fetchall()
        for row in results:
            print row
            print "above are your readings"
    except:
        print "========== Error =============="
         db.rollback()
         db.close()

if x == "delete" :
    idn = raw_input("enter name: ")
    sql = "DELETE FROM EMPLOYEE WHERE FIRST_NAME = %s"
    try:
        cursor.execute(sql, (idn))
        db.commit()
        print "your record is deleted"

    except:
        print "================= Error ============="
        db.rollback()
        db.close()
