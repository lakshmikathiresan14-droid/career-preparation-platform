notes_data = {

    "python": """
PYTHON PROGRAMMING

UNIT 1: INTRODUCTION TO PYTHON

Python is a high-level, interpreted, object-oriented, and general-purpose programming language developed by Guido van Rossum in 1991.

Features:
1. Easy to Learn and Use
2. Open Source
3. Platform Independent
4. Object-Oriented
5. Interpreted Language
6. Large Standard Library
7. Dynamic Typing

Applications:
1. Web Development
2. Artificial Intelligence
3. Machine Learning
4. Data Science
5. Automation
6. Cyber Security

UNIT 2: PYTHON BASICS

Variables:
x = 10
name = "John"

Data Types:
1. int
2. float
3. str
4. bool
5. complex

Operators:
1. Arithmetic
2. Relational
3. Logical
4. Assignment
5. Bitwise

Control Statements:
1. if
2. if-else
3. elif
4. for loop
5. while loop

Functions:
def greet():
    print("Welcome")

Data Structures:
1. List
2. Tuple
3. Set
4. Dictionary

OOP Concepts:
1. Class
2. Object
3. Inheritance
4. Polymorphism
5. Encapsulation
6. Abstraction

File Handling:
r - Read
w - Write
a - Append

Exception Handling:
try
except
finally

Popular Libraries:
1. NumPy
2. Pandas
3. Flask
4. Django
5. TensorFlow

Advantages:
1. Easy Syntax
2. Large Community
3. Rapid Development

Conclusion:
Python is widely used in AI, Machine Learning, Data Science and Web Development.
""",

    "java": """
JAVA PROGRAMMING

UNIT 1: INTRODUCTION TO JAVA

Java is a high-level, object-oriented, platform-independent programming language developed by Sun Microsystems.

Features:
1. Platform Independent
2. Object-Oriented
3. Secure
4. Robust
5. Portable
6. Multithreaded

Applications:
1. Android Development
2. Enterprise Applications
3. Banking Systems
4. Web Applications

UNIT 2: JAVA BASICS

Structure of Java Program:

class Demo {
    public static void main(String args[]) {
        System.out.println("Hello World");
    }
}

Data Types:
1. byte
2. short
3. int
4. long
5. float
6. double
7. char
8. boolean

Operators:
1. Arithmetic
2. Relational
3. Logical
4. Assignment

Control Statements:
1. if
2. if-else
3. switch
4. for
5. while
6. do-while

OOP Concepts:
1. Class
2. Object
3. Encapsulation
4. Inheritance
5. Polymorphism
6. Abstraction

Constructors:
1. Default Constructor
2. Parameterized Constructor

Exception Handling:
1. try
2. catch
3. finally
4. throw
5. throws

Packages and Interfaces:
Used for code organization and abstraction.

Collection Framework:
1. ArrayList
2. LinkedList
3. HashSet
4. HashMap

Multithreading:
Thread creation and execution.

Advantages:
1. Platform Independent
2. Secure
3. Object-Oriented

Conclusion:
Java is widely used for Android Development, Enterprise Applications and Banking Systems.
""",

    "dbms": """
DATABASE MANAGEMENT SYSTEM (DBMS)

UNIT 1: INTRODUCTION TO DBMS

DBMS is software used to store, manage and retrieve data efficiently.

Examples:
1. MySQL
2. Oracle
3. PostgreSQL
4. SQL Server

Advantages:
1. Data Security
2. Data Integrity
3. Reduced Redundancy
4. Backup and Recovery

UNIT 2: DATABASE ARCHITECTURE

Three-Level Architecture:
1. External Level
2. Conceptual Level
3. Internal Level

UNIT 3: DATA MODELS

1. Hierarchical Model
2. Network Model
3. Relational Model
4. Object-Oriented Model

UNIT 4: ER MODEL

Entity:
Real-world object.

Attributes:
Properties of entities.

Relationships:
1. One-to-One
2. One-to-Many
3. Many-to-Many

UNIT 5: SQL

DDL:
1. CREATE
2. ALTER
3. DROP

DML:
1. INSERT
2. UPDATE
3. DELETE

DQL:
1. SELECT

DCL:
1. GRANT
2. REVOKE

TCL:
1. COMMIT
2. ROLLBACK

UNIT 6: NORMALIZATION

1NF
2NF
3NF
BCNF

Purpose:
Reduce redundancy and improve consistency.

UNIT 7: KEYS

1. Primary Key
2. Foreign Key
3. Candidate Key
4. Alternate Key
5. Composite Key

UNIT 8: TRANSACTIONS

ACID Properties:
A - Atomicity
C - Consistency
I - Isolation
D - Durability

UNIT 9: CONCURRENCY CONTROL

Problems:
1. Lost Update
2. Dirty Read

Solutions:
1. Locking
2. Timestamping

UNIT 10: DATABASE SECURITY

1. Authentication
2. Authorization
3. Encryption

Applications:
1. Banking
2. Hospital Management
3. College Management
4. E-Commerce

Conclusion:
DBMS helps organizations store, manage and secure large amounts of data efficiently.
"""
}

def generate_notes(subject):
    return notes_data.get(
        subject.lower(),
        "Study material not available for this subject."
    )
