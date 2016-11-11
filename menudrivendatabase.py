import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","root","python123","python" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
print "tell us your choice:insert, read ,delete or update"
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
        cursor.execute(sql, (idn, name, last, age, sex, income))
        db.commit()
        print "Record Inserted"
    except:
        print "============ Error ================"
        db.rollback()

if x == "read" :
    idn = raw_input("enter id no.: ")
    l = "SELECT EXISTS(SELECT * FROM EMPLOYEE WHERE EMPLOYEE.id=%s )"
    cursor.execute(l,(idn))
    results = cursor.fetchall()
    for row in results:
        exist = row[0]
        break
    print exist
    if exist == 1 :
        sql = "SELECT * FROM EMPLOYEE WHERE id = %s"
        try:
            cursor.execute(sql, idn)
            results = cursor.fetchall()
            for row in results:
                print row
                print "above are your readings"
        except:
            print "========== Error =============="
            db.close()
    else :
        print "row does not exist"


if x == "delete" :
    idn = raw_input("enter id no. : ")
    l = "SELECT EXISTS(SELECT * FROM EMPLOYEE WHERE EMPLOYEE.id=%s )"
    cursor.execute(l,(idn))
    results = cursor.fetchall()
    for row in results:
        exist = row[0]
        break
    print exist
    if exist == 1 :
        sql = "DELETE FROM EMPLOYEE WHERE id = %s"
        try:
            cursor.execute(sql, (idn))
            db.commit()
            print "your record is deleted"
        except:
            print "================= Error ============="
            db.rollback()
            db.close()
    else :
        print "row does not exist"


if x == "update" :
    idn = raw_input("enter ur id no. where update is needed :")
    l = "SELECT EXISTS(SELECT * FROM EMPLOYEE WHERE EMPLOYEE.id=%s )"
    cursor.execute(l,(idn))
    results = cursor.fetchall()
    for row in results:
        exist = row[0]
        break
    print exist
    if exist == 1 :
        print "row exists"
        name = raw_input("enter your updated first name: ")
        last = raw_input("enter your updated last name: ")
        age = int(raw_input("enter your updated age: "))
        sex = raw_input("enter your updated sex: ")
        income = int(raw_input("enter your updated income: "))
        sql = "UPDATE EMPLOYEE SET FIRST_NAME=%s, \
        LAST_NAME=%s, AGE=%s, SEX=%s, INCOME=%s WHERE id=%s"
        try:
            cursor.execute(sql, (name, last, age, sex, income, idn))
            db.commit()
            print "data has been updated"
        except:
            db.rollback()
            db.close()
            print "=============== Error =============="
    else :
        print "row does not exist"
