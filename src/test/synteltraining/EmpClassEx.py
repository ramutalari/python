class Employee:
    """ this is the method2 """

    def __init__(self, id=101, name="Pradeep", salary=12000.00):
        self.id = id;
        self.name = name;
        self.salary = salary;
        print("Employee Created..");

    def __del__(self):
        print("Employee Destroyed");

    def display(self):
        print(self.id, self.name, self.salary);

    def display2(self):
        # """ this is the method2 """
        print(self.id, self.name, self.salary);


def start():
    employee1 = Employee();
    employee1.display();
    employee1.display2();
    employee2 = Employee(102, "Sachin Tendulkar", 34000.00);
    employee2.display();


employee3 = Employee();  # creation of object
    #employee3.start();  # will result in error
start();