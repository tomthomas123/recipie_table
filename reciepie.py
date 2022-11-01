import mysql.connector

mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = '',database ='recipiedb')
mycursor = mydb.cursor()

while True:
    print("""            1. Add details
            2. view details
            3. search details
            4. update details
            5. delete details
            6. exit
            """)
    choice=int(input("Enter your choice : "))
    if choice==1:
        print("Add details selected")
        name = input("enter the reciepie name : ")
        description = input("enter the description : ")
        incredient = input("enter the incredient : ")
        author = input("enter the recipie author name : ")
        sql ='INSERT INTO `reciepie`(`reciepie_name`, `reciepie_description`, `reciepie_incredient`, `recipie_author`) VALUES (%s,%s,%s,%s)'
        data= (name,description,incredient,author)
        mycursor.execute(sql,data)
        mydb.commit()
    elif choice==2:
        print("view selected")
    elif choice==3:
        print("search selected")
    elif choice==4:
        print("update selected")
    elif choice==5:
        print("delete details")
    elif choice==6:
        break