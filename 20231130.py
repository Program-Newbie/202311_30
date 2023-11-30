class Student :
    # Initial
    def __init__(self,school,school_adr,dep,manager,sname,sid,address,score,gpa):
        self.school = school
        self.school_adr = school_adr
        self.dep = dep
        self.manager = manager
        self.sname = sname
        self.sid = sid
        self.address = address
        self.score = score
        self.gpa = gpa
    # Set & Get
    def Set(self,choose,_set):
        self.__dict__[choose] = _set  # Use __dict__ to set new value
    def Get(self,choose):
        print(f"{choose} : {self.__dict__[choose]}") # Get Value
    def GetAll(self):
        print("-------------------------")
        for key,value in self.__dict__.items() :
            print(f"{key} : {value}")
        print("-------------------------")

if __name__ == "__main__" :
    E1 = Student("S1","A2B1","D1","Haiya","Eric","123","C1D1","3","2")
    E1.GetAll()
    E1.Set("school","S2")
    E1.Set("sid","456")
    E1.Set("score","5")
    E1.Get("sname")
    E1.GetAll()