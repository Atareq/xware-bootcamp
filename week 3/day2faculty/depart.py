from subject import *
class depart:
    Departments_lst = []

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        depart.Departments_lst.append(self)

def add():
    id = input("Enter ID: ")
    name = input("Enter name: ")
    depart(id, name)

def update():
   old_id = input("Enter the old ID , Please: ")
   for i in depart.Departments_lst:
       if i.id == old_id:
            new_id=input("Enter the new ID , Please: ")
            new_name=input("Enter the new name , Please: ")
            i.id = new_id
            i.name = new_name
            print(f"your update has done succesfully and the new data are {i.id}and{i.name}")

def search():
    u_input= input("enter the id of your department: ")
    for index in depart.Departments_lst:
        if  index.id == u_input: 
            print(f"The searched department: ID={index.id}, Name={index.name}")
            return
def get():
    for index in depart.Departments_lst:
        print(f"Last added department: ID={index.id}, Name={index.name}")

depart_1 = depart('1', 'FCI')
depart_2 = depart('2', 'BIO')
depart_3 = depart('3', 'IT')


def main():
    while True:
        enter = input("Enter the first character of your order:")
        print(enter)
        if enter == 'd a' :
            add()
        elif enter == 'd s' :
            search()
        elif enter == 'd g':
            get()
        elif enter == 'd u' :
            update()
        elif enter == 's a' :
            Subject.add()
        elif enter == 's s' :
            Subject.read_all_sub()
        elif enter == 's g' :
            Subject.search()
        elif enter == 's u' :
            Subject.update()
        else:
            print("Enter a valid character")
main()