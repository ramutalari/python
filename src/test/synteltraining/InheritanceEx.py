class Employee:
    def __init__(self, id=101, name="Pradeep", salary=12000.00):
        self.id = id;
        self.name = name;
        self.salary = salary;
        print("Employee Created..");

    def __del__(self):
        print("Employee Destroyed");

    def display(self):
        print(self.id, self.name, self.salary);


class Manager(Employee):
    def __init__(self, id, name, salary, designation="Manager"):
        super().__init__(id, name, salary);
        self.designation = designation;
        print("Manager Created....");

    def display(self):
        super(Manager, self).display();
        print(self.designation);


e = Employee();
e.display();
m = Manager(2222, "Pramod Patil", 34000, "Account Manager");
m2 = Manager(2223, "Pramod P", 35000);
m.display();
m2.display();