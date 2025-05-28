"""
Assignment:
Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens."""

class Employee:
    def  __init__(self, name, salary, ssn):
        self.name = name #public variable
        self._salary = salary #protected variable
        self.__ssn = ssn #private variable

if __name__ == "__main__":
    emp = Employee("Aliza",60000,"555-45-8454")
    #access public variable
    print("Public Variable:",emp.name)
       #access protected variable
    print("Protected Variable:",emp._salary)
       #access private variable
    try:
        print("Private Variable:",emp.__ssn)
    except AttributeError:
        print("cann't access private variable __ssn")
