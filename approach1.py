import mysql.connector
import random

cnx = mysql.connector.connect(host= 'sql6.freesqldatabase.com', password='HeFcelIrJY',user='sql6589129')
cursor = cnx.cursor()

cursor.execute("use sql6589129")
cursor.execute("show tables")

for i in cursor:
    print(i)

print("welcome to Raoji bazar airlines")
print()

cursor.execute("update seats set user_id = null")
cnx.commit()

for i in range(1,121):
    seat = random.randint(1,120)
    cursor.execute(f"Update seats set user_id={i} where id = {seat} ")
cnx.commit()

cursor.execute("select id from seats where user_id is not null")
BookedSeats=[]
for i in cursor:
    BookedSeats.append(i[0])

# print(BookedSeats)
booked = 1
for i in range(6):
    for j in range(20):
        if booked in BookedSeats:
            print("x ",end="")
        else:
            print(". ", end="")
        booked += 1
    if i==2:
        print()
    print()


