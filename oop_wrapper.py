class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age


class Employee(Person):
    # Method Overloading via default arguments
    def __init__(self, name="Unknown", age=0, emp_id="E000", salary=0.0):
        super().__init__(name, age)
        # Encapsulation: Private attributes
        self.__emp_id = emp_id
        self.__salary = salary

    # Get and Set for employee_id
    def get_emp_id(self):
        return self.__emp_id

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    # Getand Set for salary
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.get_emp_id()}")
        print(f"Salary: ${self.get_salary():.1f}")

    def __del__(self):
        # Destructor to clean up resources
        pass


class Manager(Employee):
    def __init__(self, name="Unknown", age=0, emp_id="M000", salary=0.0, department="General"):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    # Method Overriding
    def display(self):
        super().display()
        print(f"Department: {self.department}")


# Lists to store records
persons = []
employees = []
managers = []

print("--- Python OOP Project: Employee Management System ---")

while True:
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        p = Person(name, age)
        persons.append(p)
        print(f"\nPerson created with name: {name} and age: {age}.")
        print("\n--- Choose another operation ---")

    elif choice == '2':
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        emp = Employee(name, age, emp_id, salary)
        employees.append(emp)
        print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary:.1f}.")
        print("\n--- Choose another operation ---")

    elif choice == '3':
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")
        mgr = Manager(name, age, emp_id, salary, department)
        managers.append(mgr)
        print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary:.1f}, and department: {department}.")
        print("\n--- Choose another operation ---")

    elif choice == '4':
        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        sub_choice = input("Enter your choice: ")

        if sub_choice == '1':
            if not persons:
                print("\nNo Person records found.")
            for p in persons:
                print("\nPerson Details:")
                print(f"Name: {p.name}")
                print(f"Age: {p.age}")
        elif sub_choice == '2':
            if not employees:
                print("\nNo Employee records found.")
            for emp in employees:
                print("\nEmployee Details:")
                emp.display()
        elif sub_choice == '3':
            if not managers:
                print("\nNo Manager records found.")
            for mgr in managers:
                print("\nManager Details:")
                mgr.display()
                print(f"Is Manager subclass of Employee? {issubclass(Manager, Employee)}")
        print("\n--- Choose another operation ---")

    elif choice == '5':
        print("\nExiting the system. All resources have been freed.")
        print("Goodbye!")
        break
    else:
        print("\nInvalid choice! Please try again.")
        print("\n--- Choose another operation ---")