
#William McDaniel

i = 6
a = 6
x = 6
class Employee():
    def __init__(self):
        self.name = 'name'
        self.address = 'address'
        self.workPhoneNumber = 'workPhoneNumber'
        self.position = 'position'
        self.employeeComp1Dict = {}
        self.employeeComp2Dict = {}
        self.employeeComp3Dict = {}
        

    def employeesCompnay1(self):
        employeeC11 = ['Will' , '123 1st st' , '123-456-7890' , 'Sales']
        employeeC12 = ['Alex' , '124 1st st' , '123-123-7890' , 'Sales']
        employeeC13 = ['Elias' , '125 1st st' , '123-456-1230' , 'Manager']
        employeeC14 = ['Aiden' , '126 1st st' , '456-456-1230' , 'CEO']
        employeeC15 = ['Mike' , '127 1st st' , '456-456-4560' , 'Assistant Manager']
        self.employeeComp1Dict = { 1 : employeeC11, 2 : employeeC12 , 3 : employeeC13 , 4 : employeeC14 , 5 : employeeC15 }
        print (self.employeeComp1Dict[1])
        print (self.employeeComp1Dict[2])
        print (self.employeeComp1Dict[3])
        print (self.employeeComp1Dict[4])
        print (self.employeeComp1Dict[5])

    def employeesCompnay2(self):
        employeeC21 = ['Robin' , '456 12th st' , '389-178-7934' , 'CPA']
        employeeC22 = ['Patrik' , '198 56th st' , '389-178-8902' , 'Professor']
        employeeC23 = ['George' , '364 71st st' , '389-867-6826' , 'Chef']
        employeeC24 = ['Kelly' , '629 41st st' , '389-168-7810' , 'Bouncer']
        employeeC25 = ['Kid' , '839 69th st' , '389-012-7352' , 'Assistant Janitor']
        self.employeeComp2Dict = { 1 : employeeC21, 2 : employeeC22 , 3 : employeeC23 , 4 : employeeC24 , 5 : employeeC25 }
        print (self.employeeComp2Dict[1])
        print (self.employeeComp2Dict[2])
        print (self.employeeComp2Dict[3])
        print (self.employeeComp2Dict[4])
        print (self.employeeComp2Dict[5])

    def employeesCompnay3(self):
        employeeC31 = ['Garrett' , '625 79th st' , '639-3690-7934' , 'Chef']
        employeeC32 = ['Quevon' , '974 86th st' , '612-178-8202' , 'Server']
        employeeC33 = ['Bill' , '247 61st st' , '389-107-6326' , 'Bartender']
        employeeC34 = ['Barry' , '074 51st st' , '629-168-1210' , 'Car Salesman']
        employeeC35 = ['Mark' , '083 24th st' , '529-012-7352' , 'Dancer']
        self.employeeComp3Dict = { 1 : employeeC31, 2 : employeeC32 , 3 : employeeC33 , 4 : employeeC34 , 5 : employeeC35 }
        print (self.employeeComp3Dict[1])
        print (self.employeeComp3Dict[2])
        print (self.employeeComp3Dict[3])
        print (self.employeeComp3Dict[4])
        print (self.employeeComp3Dict[5])

    def newEmployeeComp1(self):
        global i 
        j = str(i)
        j = []
        name = input('Name: ')
        address = input('Address: ')
        workPhoneNumber =input('Work Phone Number: ')
        position = input('Position: ')    
        j.insert(0 , name)
        j.insert(1 , address)
        j.insert(2 , workPhoneNumber)
        j.insert(3 , position)
        self.employeeComp1Dict.update({ i : j })
        print(self.employeeComp1Dict[i])
        i = i + 1
        return i 
        
    def newEmployeeComp2(self):
        global a 
        j = str(a)
        j = []
        name = input('Name: ')
        address = input('Address: ')
        workPhoneNumber =input('Work Phone Number: ')
        position = input('Position: ')    
        j.insert(0 , name)
        j.insert(1 , address)
        j.insert(2 , workPhoneNumber)
        j.insert(3 , position)
        self.employeeComp2Dict.update({ a : j })
        print(self.employeeComp2Dict[a])
        a = a + 1
        return a 
        
    def newEmployeeComp3(self):
        global x 
        j = str(x)
        j = []
        name = input('Name: ')
        address = input('Address: ')
        workPhoneNumber =input('Work Phone Number: ')
        position = input('Position: ')    
        j.insert(0 , name)
        j.insert(1 , address)
        j.insert(2 , workPhoneNumber)
        j.insert(3 , position)
        self.employeeComp3Dict.update({ x : j })
        print(self.employeeComp3Dict[x])
        x = x + 1
        return x

Office = Employee()
Office.employeesCompnay1()
print()
Office.employeesCompnay2()
print()
Office.employeesCompnay3()
print()
newEmployeeChoice = input('Would you like to add an employee to the database? yes or no\n')
while newEmployeeChoice == 'yes':
    companyChoice = input('Which company would you like to add him/her to? 1, 2, or 3')
    if companyChoice == '1':
        Office.newEmployeeComp1()
    elif companyChoice == '2':
        Office.newEmployeeComp2()
    elif companyChoice == '3':
        Office.newEmployeeComp3()
    newEmployeeChoice2 = input('Would you like to add another employee? yes or no\n')
    if newEmployeeChoice2 == 'no':
        show = input('Would you like to see the full database? yes or no\n')
        if show == 'yes':
            print (Office.employeeComp1Dict)
            print()
            print(Office.employeeComp2Dict)
            print()
            print(Office.employeeComp3Dict)
            break
        elif show == 'no':
            break