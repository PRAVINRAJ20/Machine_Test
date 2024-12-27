from algorithms import quicksort
from database_operations import insertData, updateData, deleteData, selectData, createTable
from web_app import app
from web_scraper import scrape_website
from tests.test_algorithms import test_quicksort
from data_manipulations import convert_and_process_files

def run():

#------------------------------------------
    
    # Create database table if it doesn't exist
    print("\nSetting up database...")
    createTable()

    # Database CRUD operations menu
  
    while True:
        print("\nMain Menu:")
        print("1. Insert Record into SQLite")
        print("2. Update Record in SQLite")
        print("3. Delete Record from SQLite")
        print("4. View All Records from SQLite")
        print("5.Start REST API")
        print("6.Data Mnipulation")
        print("7.Sorting Algorithm")
        print("8.Scraping")
        print("9.Testing")
        print("10.Exit")
        
        choice = input("Enter your choice: ").strip()

        # SQLite CRUD operations
        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            city = input("Enter City: ")
            insertData(name, age, city)

        elif choice == "2":
            id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            city = input("Enter City: ")
            updateData(name, age, city, id)

        elif choice == "3":
            id = int(input("Enter ID: "))
            deleteData(id)

        elif choice == "4":
            print("Fetching all records from SQLite...")
            records = selectData()
            for record in records:
                print(record)

        elif choice == "5":  # Start Flask App
            print("Starting Flask app...")
            app.run(debug=True)
            break
        
        elif choice == "6":
             #data manipulation  
            print("Processing CSV data...")
            print(convert_and_process_files("data/data.csv","data/data.json","data/data.xml"))
            break

        elif choice == "7":
            # sorting algorithm
            print("Running algorithms...")
            print(quicksort([5, 3, 8, 6, 2]))
            break
       
       
        elif choice == "8":
            print('Scrapping...............')
            scrape_website
            break
       
        elif choice == "9":
            print('Testing:cd tests pytest test_algorithms.py')
            test_quicksort()
            break
        
        elif choice == "10":  # Exit
            print("Exiting...")
            break
        
       

        else:
            print("Invalid choice. Please try again.")
#-----------------------------------------------
   
#-----------------------------------------------
  
if __name__ == "__main__":
        run()
