# Created by: Izram Khan
# Date completed: 11-Nov-25 (12:30 am) midnight
# Feel free to use and copy code anywhere. It's all your's

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
import random
import string
import json
import os
import time

contacts = []
deleted_contacts = []

def load_contacts():
    global contacts
    if os.path.exists('contacts.json'):

        with open('contacts.json', 'r') as f:
            contacts= json.load(f)
    else:
        contacts = []

load_contacts()

def add_contact():
    print('''
[--------------------]
|---ADDING-CONTACT---|
[--------------------]
          ''')
    
    contact_id = ''.join(random.sample(string.digits, 8))

    while True:
        name = input('\nEnter contact name: ').title()
        if not name: 
            print('\n❌ Error: Name can not be empty!')
        else:
            break
    
    while True:
        try:
            contact_number = input('\nEnter contact number: ')
            if len(contact_number) != 11:
                print('\n❌ Error: Lenght must be 11 characters')
            elif not contact_number.isdigit():
                print('\n❌ Error: Contact number should only consist of numbers!')
            else:
                break
        except ValueError:
          print('❌ Error: Invalid contact number!')
        
    while True:
        gmail = input('\nEnter contact\'s gmail address: ')
        if not gmail.endswith('@gmail.com'):
            print('\n❌ Error: Gmail must end with @gmail.com!')
        else:
            break

    address = input('\nEnter contact\'s physical address: ').title()

    favorite = input("\nAdd to favorites? (y/n): ").lower() == "y"
        
    contact = {
        'ID': contact_id,
        'Name': name,
        'Contact number': contact_number,
        'Gmail Address': gmail,
        'Address': address, 
        'Favorite': favorite
    }

    print('\n✅ Contact added successfully!\n')
    for key, value in contact.items():
        print(f'• {key} - {value}')

    contacts.append(contact)
    save_contacts()

def remove_contact():
    print('''
[----------------------]
|---REMOVING-CONTACT---|
[----------------------]
          ''')

    id_check = input('\nEnter ID to remove: ')
    if id_check == '0':
        print('\n🛑 Contact removal was stopped!')
        return

    found = False
    for contact in contacts:

        if contact['ID'] == id_check:
            confirm = input('\nAre you sure (y/n): ').lower()
            if confirm == 'y':
                contacts.remove(contact)
                deleted_contacts.append(contact)
                print('\n✅ Contact removed successfully!')
                break
            else:
                print('\n🛑 Contact removal was stopped!')
            found = True
            break

    if not found:
        print('\n❌ Error: ID does not exist')
              
    save_contacts()

def search_contact():
    print('''
[-----------------------]
|---SEARCHING-CONTACT---|
[-----------------------]
          ''')

    id_check = input('\nEnter ID to search: ')
    if id_check == '0':
        print('\n🛑 Contact searching was stopped!')
        return
    
    found = False
    print('\n')
    for contact in contacts:

        if contact['ID'] == id_check:
            for key, value in contact.items():
                print(f'• {key} - {value}')
            found = True
            break
    if not found:
        print('\n❌ Error: ID does not exist!')

def view_all_contacts():
    print('''
[----------------------]
|---VIEWING-CONTACTS---|
[----------------------]
''')

    # Sort by names
    contacts.sort(key=lambda x: x['Name'].lower())

    # Separate favorites and normal contacts
    normal_contacts = [c for c in contacts if not c['Favorite']]
    favorite_contacts = [c for c in contacts if c['Favorite']]

    # Table headings
    headers = f'{'ID':<10} {'Name':<15} {'Number':<12} {'Gmail':<25} {'Address':<20} {'Fav'}'

    print('''
---CONTACTS---
''')

    print(headers)
    print('-'*95)  
    
    if normal_contacts:
        for c in normal_contacts:
            fav = '★' if c['Favorite'] else ''
            print(f"{c['ID']:<10} {c['Name']:<15} {c['Contact number']:<12} {c['Gmail Address']:<25} {c['Address']:<20} {fav}")

    else:
        print("🛑 No normal contacts available!")

    print('''
---FAVORITES---
''')

    print(headers)
    print("-" * 95)
    if favorite_contacts:
        for c in favorite_contacts:
            fav = "★" if c['Favorite'] else ""
            print(f"{c['ID']:<10} {c['Name']:<15} {c['Contact number']:<12} {c['Gmail Address']:<25} {c['Address']:<20} {fav}")
    else:
        print("🛑 No favorite contacts available!")

    print('''
---DELETED---
          ''')

    print(headers)
    print('-' * 95)
    if deleted_contacts:
        for c in deleted_contacts:
            fav = "★" if c['Favorite'] else ""
            print(f"{c['ID']:<10} {c['Name']:<15} {c['Contact number']:<12} {c['Gmail Address']:<25} {c['Address']:<20} {fav}")
    
    else:
        print('🛑 No deleted contacts available!')

def update_contact():
    print('''
[----------------------]
|---UPDATING-CONTACT---|
[----------------------]
          ''')

    id_check = input('\nEnter ID to update: ')

    found = False
    for contact in contacts:
        if contact['ID'] == id_check:
            print('\n1. Name')
            print('2. Contact')
            print('3. Gmail')
            print('4. Address')
            print('5. Get new ID')
            print('6. Add to favorites')
            print('7. Remove from favorites')

            user_choice = input('\nEnter (1 - 5): ')

            if user_choice == '1':
                new_name = input('\nEnter new contact name: ').title()
                contact['Name'] = new_name
                print(f'\n✅ Name changed to [{new_name}] successfully!')
                break
            
            elif user_choice == '2':
                try:
                    new_contact = input('\nEnter new contact number: ')
                    if len(new_contact) != 11:
                        print('\n❌ Error: Lenght must be 11 characters')
                    elif not new_contact.isdigit():
                        print('\n❌ Error: Contact number should only consist of numbers!')
                    else:
                        contact['Contact number'] = new_contact
                        print(f'\n✅ Contact number changed to [{new_contact}] successfully!')
                        break
                except ValueError:
                    print('\n❌ Error: Invalid contact number')
            
            elif user_choice == '3':
                new_gmail = input('\nEnter new gmail: ')
                if not new_gmail.endswith('@gmail.com'):
                    print('\n❌ Error: Gmail must end with @gmail.com!')
                else:
                    contact['Gmail Address'] = new_gmail
                    print(f'\n✅ Gmail changed to [{new_gmail}] successfully!')
                    break

            elif user_choice == '4':
                new_address = input('\nEnter new physical address: ').title()
                contact['Address'] = new_address
                print(f'\n✅ Address changed to [{new_address}] successfully!')
                break

            elif user_choice == '5':
                new_id = ''.join(random.sample(string.digits, 8))
                print(f'\nContact\'s new ID: {new_id}')

            elif user_choice == '6':
                if contact['Favorite'] == True:
                    print('\n❌ Contact already in favorites!')
                else:
                    contact['Favorite'] = True
                    print('\n✅ Contact added to favorites!')
            
            elif user_choice == '7':
                if contact['Favorite'] == False:
                    print('\n❌ Contact already not in favorite!')
                else:
                    contact['Favorite'] = False
                    print('\n✅ Contact removed from favorites successfully!')

            elif user_choice == '0':
                print('\n🛑 Updating contacts was stopped!')
                found = True
                break

    if not found:
        print('\n❌ Error: ID does not exist!')

    save_contacts()

def clear_all_contacts():
    print('''
[------------------------]
|---CLEAR-ALL-CONTACTS---|
[------------------------]
          ''')

    print('\nWhat do you want to delete')
    print('1. Normal Contacts')
    print('2. Favorite contacts')
    print('3. All contacts')
    print('0. Cancel')

    while True:
        user_choice = input('Enter (0 - 3): ').strip()

        if user_choice == '1':
            validation = input('\nAre you sure you want to delete all normal contacts? (y/n): ').lower()
            if validation == 'y':
                # Move deleted normal contacts to deleted_contacts
                normal_contacts = [c for c in contacts if not c['Favorite']]
                deleted_contacts.extend(normal_contacts)
                # Keep only favorite contacts
                contacts[:] = [c for c in contacts if c['Favorite']]
                print('\n✅ All normal contacts cleared successfully!')
            elif validation == 'n':
                print('\n🛑 Clearing normal contacts was stopped!')
            else:
                print('\n❌ Please enter y or n')

        elif user_choice == '2':
            validation = input('\nAre you sure you want to delete all favorite contacts? (y/n): ').lower()
            if validation == 'y':
                # Move deleted favorite contacts to deleted_contacts
                favorite_contacts = [c for c in contacts if c['Favorite']]
                deleted_contacts.extend(favorite_contacts)
                # Keep only normal contacts
                contacts[:] = [c for c in contacts if not c['Favorite']]
                print('\n✅ All favorite contacts cleared successfully!')
            elif validation == 'n':
                print('\n🛑 Clearing favorite contacts was stopped!')
            else:
                print('\n❌ Please enter y or n')

        elif user_choice == '3':
            validation = input('\nAre you sure you want to delete ALL contacts? (y/n): ').lower()
            if validation == 'y':
                deleted_contacts.extend(contacts)
                contacts.clear()
                print('\n✅ All contacts cleared successfully!')
            elif validation == 'n':
                print('\n🛑 Clearing all contacts was stopped!')
            else:
                print('\n❌ Please enter y or n')

        elif user_choice == '0':
            print('\n🛑 Clearing contacts was canceled!')
            break

        else:
            print('\n❌ Invalid choice. Enter 0, 1, 2, or 3.')

    save_contacts()

                
def save_contacts():

    with open('contacts.json', 'w') as f:
        json.dump(contacts, f, indent=3)

def intro():
    text = '| ** Welcome to your personal Address Book — quick, simple, and built to keep your contacts organized. ** |'
    delay = 0.03
    print('\n')
    for i in text.upper():
        print(i, end='', flush=True)
        time.sleep(delay)
    time.sleep(1)

def instruction_manual():
    print('''
[--- HOW TO USE ---]

1) Add Contact
   Enter name, number (11 digits), Gmail, address, and optional favorite.

2) Remove Contact
   Enter the contact ID. Type 0 to cancel.

3) Search Contact
   Search by ID to view details.

4) View All
   Shows all contacts (sorted). Favorites marked with ★.

5) Update Contact
   Change name, number, Gmail, address, ID, or favorite status.

6) Saving
   All changes are saved automatically.

----------------------
Tip: IDs are auto-made.
Note: To stop Removing, updating or searching enter 0. 
----------------------
''')

def main():
    intro()

    print('\n')
    print('-' * 50)
    # print('\n')
    print('1. Add a contact')
    print('2. Delete a contact')
    print('3. Search contact')
    print('4. View all contacts')
    print('5. Update contact')
    print('6. Clear all contacts')
    print('7. Instruction manual')
    all_func = [add_contact, remove_contact, search_contact, view_all_contacts, update_contact, clear_all_contacts, instruction_manual]
 
    while True:
        try:
            user_choice = int(input('\nEnter (1 - 7): '))
            
            if user_choice == 0:
                print('\n🛑 Address book was stopped!')
                return

            all_func[user_choice-1]()
        except ValueError:
            print('\n❌ Error: Invalid number please enter a valid number!')
        except IndexError:
            print('\n❌ Error: Enter (1 - 7)')

if __name__ == '__main__':
    main()