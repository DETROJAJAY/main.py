import mysql.connector

conn  = mysql.connector.connect(host = 'localhost' , username = 'root' , password = 'adminjay' ,        ### DATABASE CONNECT KRI TENE AK VARIABLE MA STORE KRVANU
 database  = 'new_database')     ### AAPDO JUNO DATABASE OPEN KRVO HOI TO J AA LAKHVANU BAKI NAI

my_cursor = conn.cursor()   ### AK CURSOR NI JARUR PADE DATA BASE MA MOVE KRVA MATE


#******************************************************************************************************

#quary = "CREATE DATABASE new_database"      ### NEW DATA BASE CREATE KRVANI QUARY ,,, NEW DATABSE NU NAME "new_databse" J AAPYU 6 TE REHSE
#quary = "SHOW DATABASES "                   ### DATABASE SHOW KRVA MATE NI QUARY
#quary = "CREATE TABLE student(name VARCHAR(30) , age INT)"      ### TABLE NU NAME "student" AND TENI COLUMN NU NAME "name,age" CREATE KRYUS
# quary = "INSERT INTO student(name,age) VALUES (%s , %s)"        ### INSERT NI QUARY ,,, VALUES MA PLACEHOLDER PASS KRAVEL 6
# values = [('jay' , 21) ,('heet', 22) ,('dishant',23)]           ### VALUE AYA INSERT KRELI 6 ,,, AK SATHE JAJI VALUE ENTER KRVI HOI TO AAM BAKI KHALI LIST BANAVYA VINA AK TUPPLE PN BANAVI SAKIYE
quary = "SELECT * FROM student"                             ### SHOW KRVA MATE PN SATHE FOR LOOP PN EXECUTE KRVU PADSE


my_cursor.execute(quary)                        ### VALUE ENETER NA KRVANI HOI  TYARE AAA RITE LAKHVANU
#my_cursor.execute(quary , values)                    ### QUARY EXICUTE KRVANI
# my_cursor.executemany(quary,values)                     ### AK SATHE VADHU INSERT KRI TYRE AA BAKI UPPR NU PN CHALE
#******************************************************************************************************


# for i in my_cursor:                       ### CURSOR MOVE THAI AND BDHA DATA BASE NA NAME PRINT KRE BUT TUPPLE MA AAVE
#     print(i)
print(my_cursor.fetchall())                 ### INBUILT FUNCTION 6 "fetchall()" JENATHI BDHA DATABASES NA NAME NI LIST J PRINT THAI JAI LOOP NA LAGAVVU PADE



#******************************************************************************************************
#conn.commit()       ### QUARY SAVE KRVANI
conn.close()        ### CONNECTION CLOSE KRVANU