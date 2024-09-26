import mysql.connector
conn = mysql.connector.connect(host="localhost", user="Sabelo",password="Carni5721@#$%",database="guessing_Game")
c = conn.cursor()

def add_staff(name,surname,age,salary):
    x="insert into staff(name,surname,age,salary) values(%s,%s,%s,%s)"
    c.execute(x,(name,surname,age,salary))
    conn.commit()

def delete_staff(id_number):
    x= f"delete from staff where id_number = {id_number} "
    c.execute(x)
    conn.commit()

def view_staff():
    x="select * from staff"
    c.execute(x)
    y=c.fetchall()
    for row in y:
        print(f"id_number :{row[0]}, name : {row[1]}, surname : {row[2]}, age : {row[3]}, salary : {row[4]}")

def main():
    while True:
        try:
            user = int(input("press 1 to add staff, press 2 to remove staff, press 3 to view staff list, press 4 to exit:  "))

            if user ==1:
                name=input("Enter name :")
                surname=input("Enter surname :")
                age=int(input("Enter the age :"))
                salary=float(input("Enter salary :"))
                add_staff(name,surname,age,salary)

            if user ==2:
                id_number=int(input("Enter ID number :"))
                delete_staff(id_number)


        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    main()
c.close()
conn.close()