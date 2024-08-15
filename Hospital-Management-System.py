import mysql.connector as connector

print("\n")

new = 'MULTICARE HOSPITAL'
new_1 = new.center(93)
print(new_1)
dx = 'GREATER NOIDA , SEC - A30'
dx_4 = dx.center(95)
print(dx_4)
dr = 'Near EXPO MART , GREATER NOIDA'
dr_2 = dr.center(94)
print(dr_2)
vc = 'GAUTAM BUDH NAGAR , UTTAR PRADESH'
vc_10 = vc.center(95)
print(vc_10)

print("-"*92)
print("\n")


try:
    con = connector.connect(host='localhost',
                            user='root',
                            passwd='',
                            charset='utf8')
    if con.is_connected():
        print("SUCCESSFULLY CONNECTED TO MYSQL...")
    else:
        print("WRONG INPUT..")

    cursor = con.cursor()
    cursor.execute('create database if not exists hospital')
except connector.Error as err:
    print("Error",err)
try:
    con = connector.connect(host='localhost',
                            user='root',
                            passwd='',
                            database='hospital',
                            charset='utf8')
    if con.is_connected():
        print("SUCCESSFULLY CONNECTED TO MYSQL...")
    else:
        print("WRONG INPUT..")

    cursor = con.cursor()
    cursor.execute('create table if not exists doctor(doctor_id int(20), doctor_name varchar(40), specialist varchar(30) NOT NULL, cabin_no integer, salary integer)')
except connector.Error as err:
    print("Error",err)

def addDoctor():
    while True:
        con = connector.connect(host='localhost',
                                user='root',
                                password='',
                                database='hospital',
                                charset='utf8')
        if con.is_connected():
            print("SUCCESSFULLY CONNECTED...")
        else:
            print("SOMETHING WENT WRONG.....")

        cursor = con.cursor()

        doctor_id = int(input("Enter Doctors's ID :"))
        doctor_name = input("Enter Doctor's Name :")
        specialist = input("Enter special proffession of doctor :")
        cabin_no = int(input("Enter Doctor's cabin number :"))
        salary = int(input("Enter salary of the doctor :"))
        query = "Insert into doctor values({},'{}','{}',{},{})".format(doctor_id,doctor_name,specialist,cabin_no,salary)
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount,"DOCTOR'S DETAILS SUCCESSFULLY ENTERED...")
        x = input("Do you want to continue(y/n)..??")
        if x == "n" or x == "N":
            "anykey"
        if x == "y" or x == "Y":
            continue
        anykey = input("PRESS ANYKEY TO PROCEED .....")
        menu()


def viewDoctor():
    con = connector.connect(host='localhost',
                            user='root',
                            password='',
                            database='hospital',
                            charset='utf8')
    if con.is_connected():
        print("SUCCESSFULLY CONNECTED....")
    else:
        print("SOME CONNECTIVITY ISSUE...")
    cursor = con.cursor()
    query = "select * from doctor"
    cursor.execute(query)
    p = cursor.fetchall()
    print("*******************************")
    print('%3s'%"doctor_id",'%21s'%"doctor_name",'%22s'%"specialist",'%19s'%"cabin_no",'%18s'%"salary")
    print("*******************************")
    for row in  p:
        print('%3s'%row[0],'%27s'%row[1],'%22s'%row[2],'%19s'%row[3],'%17s'%row[4])
    print("Total no. of rows=",cursor.rowcount)
    print("All records displayed.........")
    anykey = input("PRESS ANYKEY TO PROCEED...")
    menu()


def deleteDoctor():
    con = connector.connect(host='localhost',
                            user='root',
                            password='',
                            database='hospital',
                            charset='utf8')
    cursor = con.cursor()
    d = int(input("Enter Doctor ID for deleting :-"))
    query = "delete from doctor where doctor_id={0}".format(d)
    cursor.execute(query)
    con.commit()
    print("Entry Deleted...")
    anykey = input("PRESS ANYKEY TO PROCEED")
    menu()


def updateDoctor():
    con = connector.connect(host='localhost',
                            user='root',
                            password='',
                            database='hospital',
                            charset='utf8')
    cursor = con.cursor()
    d = int(input("Enter Doctor Id to be updated :"))

    doctor_id = int(input("Enter new Doctor's Id :"))
    doctor_name= input("Enter new Doctor name :")
    specialist = input("Enter new Doctor's Field :")
    cabin_no = int(input("Enter new cabin number :"))
    salary = int(input("Enter New salary of the Doctor :"))
    
    query = "update doctor set doctor_id=%s, doctor_name='%s', specialist='%s', cabin_no=%s, salary=%s where doctor_id=%s"%(doctor_id, doctor_name, specialist, cabin_no, salary,d)
    
    cursor.execute(query)
    con.commit()
    print("UPDATION IN PROGRESS ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print(cursor.rowcount,"Entry updated successfully...")
    anykey = input("PRESS ANYKEY TO PROCEED")
    menu()


def searchDoctor():
    con = connector.connect(host='localhost',
                            user='root',
                            password='',
                            database='hospital',
                            charset='utf8')
    cursor = con.cursor()
    print("ENTER CHOICE ACCORDING TO YOU WANT TO SEARCH :")
    print("1. ACCORDING TO DOCTOR'S ID :")
    print("2. ACCORDING TO DOCTOR'S NAME :")
    print("3. ACCORDING TO SPECIAL PROFFESION :")
    print("4. ACCORDING TO CABIN NUmBER :")
    print("5. ACCORDING TO SALARY :")
              
    choice = int(input("Enter the choice (1-5) :"))
    if choice == 1:
        d = int(input("Enter Doctor ID which you want to search :"))
        query = "select * from doctor where doctor_id=%s"%(d)
    elif choice == 2:
        name = input("Enter Doctor name which you want to search :")
        data = "select * from doctor where doctor_name LIKE '%s'"%(name)
    elif choice == 3:
        s = input("Enter Doctor special proffession to search :")
        query = "select * from doctor where specialist LIKE '%s'"%(s)
    elif choice == 4:
        c = int(input("Enter Doctor cabin number to be searched :"))
        query = "select * from doctor where cabin_no=%s"%(c)
    elif choice == 5:
        sal = int(input("Enter Doctor salary to be searched :"))
        query = "select * from doctor where salary=%s"%(sal)
    else:
        print("Wrong Choice")
    cursor.execute(query)
        
    r = cursor.fetchall()
    print("*"*80)
    print('%3s'%"doctor_id",'%21s'%"doctor_name",'%22s'%"specialist",'%19s'%"cabin_no",'%18s'%"oneday_salary")
    print("*"*80)
    for row in r:
        print('%3s'%row[0],'%27s'%row[1],'%22s'%row[2],'%19s'%row[3],'%17s'%row[4])
    print("ENTRY SEARCHED:",cursor.rowcount)

    anykey = input("PRESS ANY KEY TO PROCEED")
    menu()

try:
    con = connector.connect(host='localhost',
                            user='root',
                            passwd='',
                            database='hospital',
                            charset='utf8')
    if con.is_connected():
        print("SUCCESSFULLY CONNECTED TO MYSQL...")
    else:
        print("WRONG INPUT..")

    cursor = con.cursor()
    cursor.execute('create table if not exists appointment(patient_id int(20), patient_name varchar(40), app_date varchar(30) NOT NULL, meeting_with varchar(40) NOT NULL, fees integer)')
except connector.Error as err:
    print("Error",err)


def addApp():
    while True:
        con = connector.connect(host='localhost',
                        user='root',
                        password='',
                        database='hospital',
                        charset='utf8')

        cursor = con.cursor()

        patient_id = int(input("Enter Patient's ID :"))
        patient_name = input("Enter patient's name :")
        app_date = input("Enter appointment date :")
        meeting_with = input("Enter Doctor's name whom patient want to consult  :")
        fees = int(input("Enter Checkup's Total charge  :"))
        query = "Insert into appointment values({},'{}','{}','{}',{})".format(patient_id,patient_name,app_date,meeting_with,fees)
        
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount,"ISSUING DATA ENTERED ...")
        x = input("Do you want to continue entry(y/n) ..?")
        if x == "n" or x == "N":
            "anykey"
        if x == "y" or x == "Y":
            continue
        anykey = input("PRESS ANYKEY TO PROCEED")
        menu() 
        
    
def viewApp():
    con= connector.connect(host='localhost',
                           user='root',
                           password='',
                           database='hospital',
                           charset='utf8')
    cursor = con.cursor()
    query = "select * from appointment"
    cursor.execute(query)
    x = cursor.fetchall()
    print("*******************************")
    print('%3s'%"patient_id",'%20s'%"patient_name",'%20s'%"app_date",'%20s'%"meeting_with",'%15s'%"fees")
    print("*******************************")
    for row in  x:
        print('%3s'%row[0],'%24s'%row[1],'%23s'%row[2],'%19s'%row[3],'%17s'%row[4])
    print("Total entries :",cursor.rowcount)
    anykey = input("PRESS ANYKEY TO PROCEED")
    menu()
          

def searchApp():
    con = connector.connect(host='localhost',
                            user='root',
                            password='',
                            database='hospital',
                            charset='utf8')
    cursor = con.cursor()
    print("ENTER CHOICE ACCORDING TO YOU WANT TO SEARCH :")
    print("1. ACCORDING TO PATIENT'S ID :")
    print("2. ACCORDING TO PATIENT'S NAME :")
    print("3. ACCORDING TO APPOINTMENT DATE :")
    print("4. ACCORDING TO DOCTOR'S NAME :")
    print("5. ACCORDING TO FEES :")
              
    choice = int(input("Enter the choice (1-5) :"))
    if choice == 1:
        d = int(input("Enter Patient ID which you want to search :"))
        query = "select * from appointment where patient_id=%s"%(d)
    elif choice == 2:
        name = input("Enter Patient name which you want to search :")
        data = "select * from appointment where patient_name LIKE '%s'"%(name)
    elif choice == 3:
        s = input("Enter Appointment date to search :")
        query = "select * from appointment where app_date='%s'"%(s)
    elif choice == 4:
        c = input("Enter Doctor's Name  to be searched :")
        query = "select * from doctor where meeting_with LIKE '%s'"%(c)
    elif choice == 5:
        fe = int(input("Enter Doctor Fees to be searched :"))
        query = "select * from appointment where fees=%s"%(fe)
    else:
        print("Wrong Choice")

    cursor.execute(query)
        
    m = cursor.fetchall()
    print("*******************************")
    print('%3s'%"patient_id",'%20s'%"patient_name",'%20s'%"app_date",'%20s'%"meeting_with",'%15s'%"fees")
    print("*******************************")
    for row in m:
        print('%3s'%row[0],'%24s'%row[1],'%23s'%row[2],'%19s'%row[3],'%17s'%row[4])
    print("ENTRY SEARCHED:",cursor.rowcount)
    anykey = input("PRESS ANY KEY TO PROCEED")
    menu()


def deleteApp():
    con = connector.connect(host='localhost',
                            user='root',
                            password='',
                            database='hospital',
                            charset='utf8')
    cursor = con.cursor()
    d = int(input("Enter Patient ID for deleting :-"))
    query = "delete from appointment where patient_id={0}".format(d)
    cursor.execute(query)
    con.commit()
    print(cursor.rowcount,"Entry Deleted...")
    anykey = input("PRESS ANYKEY TO PROCEED")
    menu()


def updateApp():
    con = connector.connect(host='localhost',
                            user='root',
                            password='',
                            database='hospital',
                            charset='utf8')
    cursor = con.cursor()
    fd = int(input("Enter Patient Id to update :"))

    patient_name = input("Enter new Name of patient :")
    app_date = input("Enter new appointment date :")
    fees = int(input("Enter the new Total amount of fees :"))

    query = "update appointment set patient_name='%s', app_date='%s', fees=%s where patient_id=%s"%(patient_name,app_date,fees,fd)
    

    cursor.execute(query)
    con.commit()
    print("UPDATION IN PROGRESS |||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("Entry updated successfully...")
    anykey = input("PRESS ANYKEY TO PROCEED")
    menu()

try:
    con = connector.connect(host='localhost',
                            user='root',
                            passwd='',
                            database='hospital',
                            charset='utf8')
    if con.is_connected():
        print("SUCCESSFULLY CONNECTED TO MYSQL...")
    else:
        print("WRONG INPUT..")

    cursor = con.cursor()
    cursor.execute('create table if not exists report(patient_id int(20), patient_name varchar(40), report_date varchar(30) NOT NULL, disease varchar(30) NOT NULL, report_status varchar(50) NOT NULL)')
except connector.Error as err:
    print("Error",err)


def addReport():
    while True:
        con = connector.connect(host='localhost',
                                user='root',
                                password='',
                                database='hospital',
                                charset='utf8')

        cursor = con.cursor()

        patient_id = int(input("Enter Patient's Id :"))
        patient_name = input("Enter Patients's name :")
        report_date = input("Enter Report date :")
        disease = input("Enter Disease of patient :")
        report_status = input("Enter report postivity or negativity  :")
        query = "Insert into report values({},'{}','{}','{}','{}')".format(patient_id,patient_name,report_date,disease,report_status)
        
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount,"FINE ENTRY DONE ...")
        x = input("Do you want to continue Entry(y/n)..?")
        if x == "n" or x == "N":
            "anykey"
        if x == "y" or x == "Y":
            continue
        anykey = input("PRESS ANYKEY TO PROCEED")
        menu()

def viewReport():
    con = connector.connect(host='localhost',
                            user='root',
                            password='',
                            database='hospital',
                            charset='utf8')
    cursor = con.cursor()
    query = "select * from report"
    cursor.execute(query)
    m = cursor.fetchall()
    print("********************************")
    print('%3s'%"patient_id",'%20s'%"patient_name",'%19s'%"report_date",'%16s'%"disease",'%21s'%"report_status")
    print("********************************")
    for row in  m:
        print('%3s'%row[0],'%26s'%row[1],'%19s'%row[2],'%16s'%row[3],'%21s'%row[4])
        
    print("Total entries :",cursor.rowcount)

    anykey = input("PRESS ANY KEY TO PROCEED")
    menu()

def deleteReport():
    con = connector.connect(host='localhost',
                            user='root',
                            password='',
                            database='hospital',
                            charset='utf8')
    cursor = con.cursor()
    fd = int(input("Enter Patient ID for deleting :-"))
    query = "delete from report where patient_id={0}".format(fd)
    cursor.execute(query)
    con.commit()
    print(cursor.rowcount,"Fine Entry Deleted...")
    anykey = input("PRESS ANY KEY TO PROCEED")
    menu()


def updateReport():
    con = connector.connect(host='localhost',
                            user='root',
                            password='',
                            database='hospital',
                            charset='utf8')
    cursor = con.cursor()

    fd = int(input("Enter Patient ID to be update :"))

    patient_id = int(input("Enter new Patient ID :"))
    patient_name = input("Enter the changed patient name :")
    report_date = input("Enter the new report date :")
    disease = input("Enter the corrrected disesase :")
    report_status = input("Enter the correction in report status :")
    query = "update report set patient_id=%s, patient_name='%s', report_date='%s', disease='%s', report_status='%s' where patient_id=%s"%(patient_id,patient_name,report_date,disease,report_status,fd)
    cursor.execute(query)
    con.commit()
    print("UPDATION IN PROGRESS ||||||||||||||||||||||||||||||")
    print(cursor.rowcount," FINE Entry updated successfully...")
    anykey = input("PRESS ANYKEY TO PROCEED")
    menu()


def searchReport():
    con = connector.connect(host='localhost',
                            user='root',
                            password='',
                            database='hospital',
                            charset='utf8')
    cursor = con.cursor()
    print("ENTER CHOICE ACCORDING TO YOU WANT TO SEARCH :")
    print("1. ACCORDING TO PATIENT'S ID :")
    print("2. ACCORDING TO PATIENT'S NAME :")
    print("3. ACCORDING TO REPORT DATE :")
    print("4. ACCORDING TO DISEASE :")
    print("5. ACCORDING TO REPORT STATS :")
              
    choice = int(input("Enter the choice (1-5) :"))
    if choice == 1:
        d = int(input("Enter Patient ID which you want to search :"))
        query = "select * from report where patient_id=%s"%(d)
    elif choice == 2:
        name = input("Enter Patient name which you want to search :")
        data = "select * from report where patient_name LIKE '%s'"%(name)
    elif choice == 3:
        s = input("Enter Report date to search :")
        query = "select * from report where report_date=%s"%(s)
    elif choice == 4:
        c = input("Enter Disease Name to be searched :")
        query = "select * from report where disease LIKE '%s'"%(c)
    elif choice == 5:
        rs = input("Enter Doctor Fees to be searched :")
        query = "select * from report where report_status LIKE '%s'"%(rs)
    else:
        print("Wrong Choice")
    cursor.execute(query)
        
    m = cursor.fetchall()
    print("*******************************")
    print('%3s'%"patient_id",'%20s'%"patient_name",'%20s'%"report_date",'%20s'%"disease",'%15s'%"report_status")
    print("*******************************")
    for row in m:
        print('%3s'%row[0],'%24s'%row[1],'%23s'%row[2],'%19s'%row[3],'%17s'%row[4])
    print("ENTRY SEARCHED:",cursor.rowcount)

    anykey = input("PRESS ANY KEY TO PROCEED")
    menu()
    



def menu():
    nestedList = [["1.) Enter Doctor's data" ,"6.) Enter Appointment details" ,"11.)  Enter Report Details"],
                  ["2.) View Doctor's data"  ,"7.)  View Appointment details","12.)   View Report Details"],
                  ["3.) Delete Doctor's data","8.) Search Appoitment details" ,"13.)  Delete Report Detail"],
                  ["4.) Update Doctor's data","9.) Delete Appointment detail","14.) Update Report Details"],
                  ["5.) Search Doctor's data","10.)Update Appointment detail","15.) Search Report Details"]]

    print("-"*94)
    print("|        Doctors data       |     Appointmnet Details        |         Report Details      |")
    print("-"*94)

    for py in nestedList:
        print("|",py[0]," "*(24-len(py[0])),"|",
              py[1]," "*(25-len(py[1])) ,"|",
              py[2]," "*(10-len(py[2])) ,"|")

    print("-"*94)

    
    a_string = 'PRESS 16'
    new_string = a_string.center(90)
    print("\n")
    print(new_string)

    a_string = 'for EXIT'
    new_string = a_string.center(90)
    print(new_string)

    while True:
        try:
            choice = int(input("ENTER YOUR CHOICE HERE(1-16) :="))
            if choice == 1:
                addDoctor()
                break
            elif choice == 2:
                viewDoctor()
                break
            elif choice == 3:
                deleteDoctor()
                break
            elif choice == 4:
                updateDoctor()
                break
            elif choice == 5:
                searchDoctor()
                break
            elif choice == 6:
                addApp()
                break
            elif choice == 7:
                viewApp()
                break
            elif choice == 8:
                searchApp()
                break
            elif choice == 9:
                deleteApp()
                break
            elif choice == 10:
                updateApp()
                break
            elif choice == 11:
                addReport()
                break
            elif choice == 12:
                viewReport()
                break
            elif choice == 13:
                deleteReport()
                break
            elif choice == 14:
                updateReport()
                break
            elif choice == 15:
                searchReport()
                break
            elif choice == 16:
                exit()
                break
            else:
                print("INVALID CHOICE!!!! { ENTER 1-16 } ")
                menu()
        except ValueError:
                print("INVALID CHOICE!!! { ENTER 1-16 }")
                exit()

menu()
