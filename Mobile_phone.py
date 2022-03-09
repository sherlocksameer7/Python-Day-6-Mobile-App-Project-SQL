import sqlite3

from prettytable import PrettyTable

connection = sqlite3.connect("mobile.db")

list_of_tables = connection.execute("Select name from sqlite_master Where type='table' And name='Smart_phones'").fetchall()

if list_of_tables != []:
    print("Table not found!  ")

else:
    connection.execute(''' Create Table Smart_phones(
                       ID Integer Primary Key Autoincrement,
                       Serial_Number Integer,
                       Brand_Name Text,
                       Model_Name Text,
                       Manufacturing_Year Integer,
                       Manufacturing_Month Text,
                       Price Integer
    ); ''')
    print("Table created successfully")

while True:
    print("Select an option from the Menu ? ")

    print("1. Add a Mobile phones ")
    print("2. Search a Mobile phones ")
    print("3. Update a Mobile phones ")
    print("4. Delete a Mobile phones ")
    print("5. View All Mobile phones ")
    print("6. Max of all Mobile phones ")
    print("7. Min of all Mobile phones ")
    print("8. Avg of all Mobile phones ")
    print("9. Count of all Mobile phones ")
    print("10. Sum of all Mobile phones ")
    print("11. Group of all Mobile phones ")
    print("12. Order of all Mobile phones ")
    print("13. Range Between of all Mobile phones ")
    print("14. Max values and Details of all Mobile phones ")
    print("15. Exit ")

    choice = int(input("Enter a Choice ? "))

    if choice == 1:
        get_serial_number = input("Enter Serial Number: ")
        get_brandName = input("Enter Brand Name: ")
        get_Model_name = input("Enter Model name: ")
        get_manufacturing_year = input("Enter a Manufacturing Year: ")
        get_manufacturing_month = input("Enter a Manufacturing Month: ")
        get_price = input("Enter a Mobile Price: ")
        connection.execute("Insert Into Smart_phones(Serial_Number, Brand_Name, Model_Name, Manufacturing_Year,\
        Manufacturing_Month, Price) Values ("+get_serial_number+",'"+get_brandName+"','"+get_Model_name+"',\
        "+get_manufacturing_year+",'"+get_manufacturing_month+"',"+get_price+")")
        connection.commit()

        # connection.close()  NEVER USED IN THIS ******

        print("Inserted Successfully")


    elif choice == 2:
        get_mobile = input("Enter Mobile Serial Number to be Searched ? ")

        table = PrettyTable(["ID", "Serial Number", "Brand Name", "Model Name", "Manufacturing Year", "Manufacturing Month", "Price"])

        result = connection.execute("Select * From Smart_phones Where Serial_Number=" + get_mobile)

        for i in result:

            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])

            # print("ID", i[0])
            # print("Serial_Number", i[1])
            # print("Brand_Name", i[2])
            # print("Model_Name", i[3])
            # print("Manufacturing_Year", i[4])
            # print("Manufacturing_Month", i[5])
            # print("Price", i[6])

        print(table)   # it must be in outside of the loop

    elif choice == 3:
        get_mobile_serial = input("Enter a Serial Number to be Updated ? ")

        get_brandName = input("Enter Brand Name: ")
        get_Model_name = input("Enter Model name: ")
        get_manufacturing_year = input("Enter a Manufacturing Year: ")
        get_manufacturing_month = input("Enter a Manufacturing Month: ")
        get_price = input("Enter a Mobile Price: ")

        connection.execute("Update Smart_phones \
        Set Brand_Name= '"+get_brandName+"', Model_Name= '"+get_Model_name+"', Manufacturing_Year= "+get_manufacturing_year+", \
        Manufacturing_Month= '"+get_manufacturing_month+"', Price= "+get_price+" Where Serial_Number=" +get_mobile_serial)

        print("Updated Successfully")

    elif choice == 4:
        get_serial = input("Enter a Serial Number to be Deleted ? ")

        connection.execute("Delete From Smart_phones Where Serial_Number=" +get_serial)

        connection.commit()

        print("Deleted Successfully")

    elif choice == 5:
        result = connection.execute("Select * From Smart_phones")

        table = PrettyTable(["ID", "Serial Number", "Brand Name", "Model Name", "Manufacturing Year", "Manufacturing Month", "Price"])

        for i in result:

            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])

            # print("ID", i[0])
            # print("Serial_Number", i[1])
            # print("Brand_Name", i[2])
            # print("Model_Name", i[3])
            # print("Manufacturing_Year", i[4])
            # print("Manufacturing_Month", i[5])
            # print("Price", i[6])

        print(table)

    elif choice == 6:

        result = connection.execute("Select Max(Price) as price From Smart_phones")

        for i in result:
            print("Maximum Price: ", i[0])

    elif choice == 7:

        result = connection.execute("Select Min(Price) as price From Smart_phones")

        for i in result:
            print("Minimum Price: ", i[0])

    elif choice == 8:

        result = connection.execute("Select Avg(Price) as price From Smart_phones")

        for i in result:
            print("Average Price: ", i[0])

    elif choice == 9:

        result = connection.execute("Select Count(*) as count From Smart_phones")

        for i in result:
            print("Total Count of an Mobile Phones: ", i[0])

    elif choice == 10:

        result = connection.execute("Select Sum(Price) as price From Smart_phones")

        for i in result:
            print("Sum of all Mobile Price: ", i[0])

    elif choice == 11:

        result = connection.execute("Select Brand_Name,Sum(Price) as price From Smart_phones Group by Brand_Name")
        table = PrettyTable(["Brand", "Price"])

        for i in result:
            table.add_row([i[0], i[1]])
        print(table)

    elif choice == 12:

        result = connection.execute("Select Brand_Name,Sum(Price) as price From Smart_phones Group by Brand_Name Order by Brand_Name Desc")
        table = PrettyTable(["Brand", "Price"])

        for i in result:
            table.add_row([i[0], i[1]])
        print(table)

    elif choice == 13:

        lower_Amount = input("Enter a lower number to print ? ")
        Higher_Amount = input("Enter a higher number to print ? ")
        result = connection.execute("Select * From Smart_phones Where Price Between "+lower_Amount+" And "+Higher_Amount)
        table = PrettyTable(
            ["ID", "Serial Number", "Brand Name", "Model Name", "Manufacturing Year", "Manufacturing Month", "Price"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)

    elif choice == 14:

        result = connection.execute("Select * From Smart_phones Where Price = (Select Max(Price) From Smart_phones)")
        table = PrettyTable(["ID", "Serial Number", "Brand Name", "Model Name", "Manufacturing Year", "Manufacturing Month", "Price"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)

    elif choice == 15:
        connection.close()
        break

    else:
        print("Invalid Choice ??? ")