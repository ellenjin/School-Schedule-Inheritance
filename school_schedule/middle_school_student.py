from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation
    
    def summary(self):
        parent_summary = super().summary()
        if self.gets_transportation:
            transportation_summary = f"{self.name} needs transportation."
        else:
            transportation_summary = f"{self.name} does not need transportation."
        return (f"{parent_summary}. {transportation_summary}")