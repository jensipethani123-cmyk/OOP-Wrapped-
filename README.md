# Python OOP Project – Employee Management System

## Author

**Jensi Pethani**

## Project Overview

This project is a **Python-based Employee Management System** developed using **Object-Oriented Programming (OOP)** concepts.

The system allows users to create and manage:

* Person records
* Employee records
* Manager records
* Employee IDs and salaries
* Manager departments
* Display details of stored records

The project demonstrates important Python OOP concepts such as **Inheritance, Encapsulation, Method Overriding, Default Arguments, Constructors, and Destructors**.

---

## OOP Concepts Used

### 1. Class and Object

The project uses classes such as:

* `Person`
* `Employee`
* `Manager`

Objects are created from these classes to store individual records.

Example:

```python
p = Person(name, age)
emp = Employee(name, age, emp_id, salary)
mgr = Manager(name, age, emp_id, salary, department)
```

---

### 2. Inheritance

The `Employee` class inherits from the `Person` class.

```python
class Employee(Person):
```

The `Manager` class further inherits from `Employee`.

```python
class Manager(Employee):
```

Therefore, the inheritance hierarchy is:

```text
Person
   ↓
Employee
   ↓
Manager
```

---

### 3. Encapsulation

Private attributes are used in the `Employee` class:

```python
self.__emp_id = emp_id
self.__salary = salary
```

These attributes can be accessed and modified using getter and setter methods:

```python
get_emp_id()
set_emp_id()

get_salary()
set_salary()
```

This demonstrates **Encapsulation** in Python.

---

### 4. Method Overloading Using Default Arguments

Python does not support traditional method overloading like some other programming languages.

This project demonstrates similar behavior using **default arguments**.

Example:

```python
def __init__(self, name="Unknown", age=0, emp_id="E000", salary=0.0):
```

This allows an object to be created with different numbers of arguments.

---

### 5. Method Overriding

The `Manager` class overrides the `display()` method of the `Employee` class.

```python
def display(self):
    super().display()
    print(f"Department: {self.department}")
```

The `super()` function is used to call the parent class implementation.

---

### 6. Constructor

The `__init__()` method is used as a constructor to initialize object attributes.

Example:

```python
def __init__(self, name="Unknown", age=0):
    self.name = name
    self.age = age
```

---

### 7. Destructor

The `Employee` class contains a destructor:

```python
def __del__(self):
    pass
```

The destructor can be used for cleanup when an object is destroyed.

---

## Features

* Create a Person
* Create an Employee
* Create a Manager
* Store records using Python lists
* Display Person details
* Display Employee details
* Display Manager details
* Store employee ID and salary securely using private attributes
* Demonstrate inheritance and method overriding
* Check whether `Manager` is a subclass of `Employee`

---

## Project Structure

```text
OOP_WRAPPER/
│
├── employee_management.py
└── README.md
```

---

## How to Run

### Step 1: Open the Project Directory

```bash
cd OOP_WRAPPER
```

### Step 2: Run the Python Program

```bash
python oop_wrapper.py
```

---

## Menu Options

When the program starts, the following menu is displayed:

```text
--- Python OOP Project: Employee Management System ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit
```

### Create a Person

The user enters:

* Name
* Age

The information is stored as a `Person` object.

### Create an Employee

The user enters:

* Name
* Age
* Employee ID
* Salary

The information is stored as an `Employee` object.

### Create a Manager

The user enters:

* Name
* Age
* Employee ID
* Salary
* Department

The information is stored as a `Manager` object.

### Show Details

Users can select whether they want to display:

* Person details
* Employee details
* Manager details

---

## Example Output

```text
--- Python OOP Project: Employee Management System ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

Enter your choice: 2

Enter Name: Rahul
Enter Age: 25
Enter Employee ID: E101
Enter Salary: 35000

Employee created with name: Rahul, age: 25, ID: E101, and salary: $35000.0.
```

Manager details example:

```text
Manager Details:
Name: Priya
Age: 32
Employee ID: M101
Salary: $55000.0
Department: IT

Is Manager subclass of Employee? True
```

---

## Technologies Used

* **Python 3**
* Object-Oriented Programming
* Python Lists
* User Input
* Inheritance
* Encapsulation
* Method Overriding
* Constructors and Destructors

---

## Learning Outcomes

By completing this project, the following OOP concepts can be understood:

* How to create classes and objects
* How inheritance works in Python
* How to implement encapsulation
* How private attributes work
* How getter and setter methods are used
* How method overriding works
* How `super()` is used
* How default arguments can simulate method overloading
* How objects can be stored and managed using lists

---

## Author

**Jensi Pethani**

Python OOP Employee Management System Project.
