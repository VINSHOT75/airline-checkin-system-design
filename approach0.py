import mysql.connector


cnx = mysql.connector.connect(host= 'sql6.freesqldatabase.com', password='HeFcelIrJY',user='sql6589129')
cursor = cnx.cursor()

cursor.execute("use systemdesign")
# cursor.execute("show tables")

print("welcome to Raoji bazar airlines")
print()


for i in range(1,5):
    seat = int(input("select seat no. = "))
    print(seat)
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
    print()


# for x in cursor:
#   print(x)