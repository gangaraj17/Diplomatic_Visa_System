# diplomatic_visa_system.py
import mysql.connector

from mysql.connector import Error

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='user'
    )
mycursor=mydb.cursor()

class DiplomaticRecord:
    def __init__(self, visa_id, diplomat_name, position, country):
        self.visa_id = visa_id
        self.diplomat_name = diplomat_name
        self.position = position
        self.country = country
        self.is_valid = True  # Assuming all records start valid



class DiplomaticVisaSystem:
    def createdb():
        try:
            mycursor.execute('create database appvisa')
            print('created DB successfully ')
        except Exception:
            print('Issue while using appvisa..')
            
    def useDB():
        try:
            mycursor.execute('Use visa')
            print('Using appvisa DB')
        except Exception:
            print('Issue while using DB..')
            
            
    def createRecord():
        try:
            mycursor.execute('CREATE TABLE IF NOT EXISTS AppliRecord (visa_id INT(10), diplomat_name VARCHAR(20), position VARCHAR(20), country VARCHAR(20))')
            print('Table created successfully..')
            mydb.commit()
        except Exception as e:
            print('Issue while creating table:', e)
    def insertRecord():
        try:
            mycursor.execute('insert into applirecord(visa_id , diplomat_name , position , country ) values(101,"smith","F1","india")')
            mydb.commit()
            print('inserted successfully..')
        except Exception as e:
            print('Issue while inserting table:', e)
    


            
            
obj=DiplomaticVisaSystem

obj.useDB()
#obj.createRecord()
obj.insertRecord()






























# class DiplomaticVisaSystem:
#     def __init__(self):
#         self.records = {}  # Using a dictionary to store diplomatic records
#         self.entry_logs = {}

#     def add_record(self, visa_id, diplomat_name, position, country):
#         # Create a new diplomatic record.
#         if visa_id in self.records:
#             print(f"Record with visa ID {visa_id} already exists.")
#         else:
#             self.records[visa_id] = DiplomaticRecord(visa_id, diplomat_name, position, country)
#             print(f"Record for {diplomat_name} added successfully.")

#     def get_record(self, visa_id):  # Read a diplomatic record.
#         return self.records.get(visa_id, None)

#     def update_record(self, visa_id, diplomat_name=None, position=None, country=None):
#         # Update existing diplomatic record.
#         if visa_id not in self.records:
#             print(f"No record found with visa ID {visa_id}.")
#         else:
#             record = self.records[visa_id]
#             if diplomat_name:
#                 record.diplomat_name = diplomat_name
#             if position:
#                 record.position = position
#             if country:
#                 record.country = country
#             print(f"Record for visa ID {visa_id} updated successfully.")

#     def delete_record(self, visa_id):  # Delete a diplomatic record.
#         if visa_id in self.records:
#             del self.records[visa_id]
#             print(f"Record with visa ID {visa_id} deleted successfully.")
#         else:
#             print(f"No record found with visa ID {visa_id}.")

#     def process_diplomatic_visas(self, visa_id):
#         # Process visas specifically designated for diplomatic personnel.
#         record = self.get_record(visa_id)
#         if record and record.is_valid:
#             print(f"Visa {visa_id} processed for diplomat {record.diplomat_name}.")
#         else:
#             print(f"Visa ID {visa_id} is invalid or does not exist.")

#     def track_diplomatic_entries(self, entry_id, visa_id, action='entry'):
#         # Track entries and exits of diplomatic personnel based on visa ID.
#         record = self.get_record(visa_id)
#         if record and record.is_valid:
#             self.entry_logs[entry_id] = {'visa_id': visa_id, 'action': action}
#             print(f"{record.diplomat_name} has {'entered' if action == 'entry' else 'exited'}.")
#         else:
#             print(f"Invalid operation for visa ID {visa_id}.")























# def menu():
#     system = DiplomaticVisaSystem()

#     while True:
#         print("\n--- Diplomatic Visa Handling System ---")
#         print("1. Add Diplomatic Record")
#         print("2. View Diplomatic Record")
#         print("3. Update Diplomatic Record")
#         print("4. Delete Diplomatic Record")
#         print("5. Process Diplomatic Visa")
#         print("6. Track Diplomatic Entry/Exit")
#         print("7. Exit")
#         choice = input("Enter your choice (1-7): ")

#         if choice == '1':
#             visa_id = int(input("Enter Visa ID: "))
#             diplomat_name = input("Enter Diplomat Name: ")
#             position = input("Enter Position: ")
#             country = input("Enter Country: ")
#             system.add_record(visa_id, diplomat_name, position, country)

#         elif choice == '2':
#             visa_id = int(input("Enter Visa ID: "))
#             record = system.get_record(visa_id)
#             if record:
#                 print(f"Visa ID: {record.visa_id}, Name: {record.diplomat_name}, Position: {record.position}, Country: {record.country}")
#             else:
#                 print(f"No record found for Visa ID {visa_id}")

#         elif choice == '3':
#             visa_id = int(input("Enter Visa ID: "))
#             diplomat_name = input("Enter new Diplomat Name (or press Enter to skip): ")
#             position = input("Enter new Position (or press Enter to skip): ")
#             country = input("Enter new Country (or press Enter to skip): ")
#             system.update_record(visa_id, diplomat_name if diplomat_name else None,
#                                  position if position else None, country if country else None)

#         elif choice == '4':
#             visa_id = int(input("Enter Visa ID to delete: "))
#             system.delete_record(visa_id)

#         elif choice == '5':
#             visa_id = int(input("Enter Visa ID to process: "))
#             system.process_diplomatic_visas(visa_id)

#         elif choice == '6':
#             entry_id = input("Enter Entry/Exit ID: ")
#             visa_id = int(input("Enter Visa ID: "))
#             action = input("Enter 'entry' or 'exit': ").lower()
#             system.track_diplomatic_entries(entry_id, visa_id, action)

#         elif choice == '7':
#             print("Exiting the system.")
#             break

#         else:
#             print("Invalid choice. Please try again.")


# # Run the menu
# if __name__ == "__main__":
#     menu()
