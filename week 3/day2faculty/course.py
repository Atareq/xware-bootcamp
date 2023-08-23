class course :
    course_lst=[]
    def __init__(self,id,name,prof_id) -> None:
        self. id = id
        self. name = name
        self.prof_id = prof_id
        course.course_lst=(self)
    @classmethod
    def read_all():
        print("the courses are ")
        for i in course.course_lst:
            print(i.id,i.name,i.prof_id)
    @classmethod
    def search():
        u_input= input("please enter the id of the search")
        for i in course.course_lst:
            if i. id == u_input:
                print(f"the id found{i.name} ")

course_1= course(1, 'OS',1)
course_2= course(2, 'natwork',1)
course_3= course(3, 'web',2)