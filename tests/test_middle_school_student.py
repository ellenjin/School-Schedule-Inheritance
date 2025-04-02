from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation

def test_new_valid_middle_school_student_with_defaults():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert not ellis.gets_transportation

def test_middle_school_student_summary_with_transportation():
    # Checking summary for a student who *does* need transportation
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    gets_transportation = True

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation)
    summary = ellis.summary()

    # Assert
    assert summary == "Ellis is a junior enrolled in 1 classes: Painting. Ellis needs transportation."


def test_middle_school_student_summary_without_transportation():
    # Check summary for a student who does *not* need transporation
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes)
    summary = ellis.summary()

    # Assert
    assert summary == "Ellis is a junior enrolled in 1 classes: Painting. Ellis does not need transportation."
