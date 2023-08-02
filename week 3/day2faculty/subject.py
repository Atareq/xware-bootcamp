class Subject:
    sub_list = []

    def __init__(self, id, name):
        self.id = id
        self.name = name
        Subject.sub_list.append(self)
    @staticmethod
    def add ():
        id_input,name_input = input("Please enter the subject ID and name for update: ").split()
        Subject(id_input,name_input)
        print("has done sucessfully")
    
    @staticmethod
    def read_all_sub():
        for i in Subject.sub_list:
            print(i.id, i.name)
    @staticmethod
    def search():
        u_input = input("Please enter the search subject ID: ")
        for i in Subject.sub_list:
            if i.id == u_input:
                print(f"The ID has been found: {i.name}")
                return i
        print("Your ID not found")
    @classmethod
    def update(cls):
        i = Subject.search()
        if i :  
            id_input,name_input = input("Please enter the subject ID and name for update: ").split()
            i .id = id_input
            i.name = name_input
        else :
            print("error")
subject_1= Subject('1','Bio')
subject_2= Subject('2','Network')
ubject_3= Subject('3','Computetional')