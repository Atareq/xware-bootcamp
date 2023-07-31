faculty = []
def create_faculty():
    id = input("please enter faculty id: ")
    name = input("please enter faculty name: ")
    department = input("please enter department name: ")
    faculty.append({'id': id, 'name': name, 'department': department})
    print('\nFaculty Created Successfully..!')
def read_faculty():
    id = input("Please enter id: ")
    for fac in faculty:
        if fac['id'] == id:
            print(fac)
            return
    print('\nFaculty not found')
def update_faculty():
    id = input("Please enter id: ")
    name = input("Please enter new name: ")
    for fac in faculty:
        if fac['id'] == id:
            fac['name'] = name
            print(fac)
            return
    print('\nFaculty not found')
def delete_faculty():
    id = input('Please enter id: ')
    for fac in faculty:
        if fac['id'] == id:
            faculty.remove(fac)
    print('\nFaculty not found')
def main():
    while True:
        print('\n1- create faculty')
        print('2- read faculty')
        print('3- update faculty')
        print('4 - delete faculty')
        print('5 - exit')
        choice = input("Please enter from 1 - 5: ")
        if choice == '1':
            create_faculty()
        elif choice == '2':
            read_faculty()
        elif choice == '3':
            update_faculty()
        elif choice == '4':
            delete_faculty()
        elif choice == '5':
            print("\nThanks for using Faculty Management System, Goodbye..!")
            break
        else:
            print('\ninvalid input, please try again!')
