class Employee:
    salary = 250
    increment = 20
    @property
    def salary_after_increment(self):
        """Return salary after applying increment percentage."""
        return (self.salary + self.salary * (self.increment/100))
    
    

    @salary_after_increment.setter
    def salary_after_increment(self, salary):
        self.increment = ((salary /self. salary) -1)*100



e = Employee()
print(e.salary_after_increment)

        
    