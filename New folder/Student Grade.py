from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def format_subject(self, subject, score):
        pass

    @abstractmethod
    def calculate_average(self):
        pass

    @abstractmethod
    def calculate_grade(self):
        pass

    @abstractmethod
    def display(self):
        pass


class GradePrinter(Printer):
    def __init__(self, grades):
        self.grades = grades

    def format_subject(self, subject, score):
        return f"{subject}: {score}"

    def calculate_average(self):
        return sum(self.grades.values()) / len(self.grades)

    def calculate_grade(self):
        avg = self.calculate_average()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        for subject, score in self.grades.items():
            print(self.format_subject(subject, score))

        print(f"\nAverage: {self.calculate_average():.2f}")
        print(f"Grade: {self.calculate_grade()}")


grades = {
    "Math": 95,
    "English": 90,
    "History": 85
}

printer = GradePrinter(grades)
printer.display()