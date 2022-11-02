import mysql.connector

mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = '',database ='recipiedb')
mycursor = mydb.cursor()

while True:
    print("""            1. Add details
            2. view details
            3. search details
            4. update details
            5. delete details
            6. Starting letter of name of recepi
            7. total number of dishes
            8. exit
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
        sql = 'SELECT * FROM `reciepie`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif choice==3:
        print("search selected")
        dish = input('enter the name of dish : ')
    
        sql = "SELECT `id`, `reciepie_name`, `reciepie_description`, `reciepie_incredient`, `recipie_author` FROM `reciepie` WHERE `reciepie_name`='"+dish+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif choice==4:
        print("update selected")
        name = input('enter the name of the recipe to be update : ')
        zname = input('enter the updated name : ')

        
        recipiedescription= input('enter the description : ')
        incredient = input('enter the incredients : ')
        author = input("Enter the recipie author name : ")
        sql = "UPDATE `reciepie` SET `reciepie_name`='"+zname+"',`reciepie_description`='"+recipiedescription+"',`reciepie_incredient`='"+incredient+"',`recipie_author`='"+author+"' WHERE `reciepie_name`='"+name+"'"
        mycursor.execute(sql)
        mydb.commit()
    elif choice==5:
        print("delete details")
        name = input('enter the name of the recipe to be deleting : ')
        sql = "DELETE FROM `reciepie` WHERE `reciepie_name`='"+name+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("Deleted succesfully")
    elif(choice==6):
        print(' enter recipie  name first letter to get full list : ')
        st = input('Enter the first character of the name : ')
        sql = "SELECT * FROM `reciepie` WHERE `reciepie_name` LIKE '%"+st+"%'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif choice ==7:
        print("total number of dishes selected")
        sql = "SELECT COUNT(`reciepie_name`) FROM `reciepie`"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)

    elif choice==8:
        break
