class Person:
    def __init__(self, name: str, yob: int) -> None:
        self._name = name
        self._yob = yob

    def describe(self):
        return f'Name: {self._name} - Yeaf of Birth: {self._yob} '


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str) -> None:
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        output = super().describe()
        output += f'- Grade: {self._grade}'
        print(output)


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str) -> None:
        super().__init__(name, yob)
        self._subject = subject
    
    def describe(self):
        output = super().describe()
        output += f'- Subject: {self._subject}'
        print(output)


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str) -> None:
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        output = super().describe()
        output += f'- Specialist: {self._specialist}'
        print(output)


class Ward:
    def __init__(self, name: str) -> None:
        self._name = name
        self.__alist = []
    
    def add_person(self, person: Person):
        self.__alist.append(person)

    def describe(self):
        print(f'Name of ward: {self._name}')
        for person in self.__alist:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.__alist:
            if isinstance(person, Doctor):
                count += 1
        print(f'Number of doctors in this ward is: {count}')
    
    def sort_age(self):
        self.__alist = sorted(self.__alist, key=lambda x: x._yob, reverse=True)

    def compute_average(self):
        teacher_group = [person._yob for person in self.__alist if isinstance(person, Teacher)]
        avg_age = sum(teacher_group) / len(teacher_group)
        print(f'Average year of teacher ages in this ward is: {avg_age}')

if __name__ == '__main__':
    student1 = Student (name="studentA", yob=2010 , grade="7")
    student1.describe()

    teacher1 = Teacher(name="teacherA", yob=1969, subject='Math')
    teacher1.describe()

    doctor1 = Doctor(name='doctorA', yob=1945, specialist='Endocrinologists')
    doctor1.describe()

    teacher2 = Teacher(name='teacherB', yob=1995, subject='History')
    doctor2 = Doctor(name='doctorB', yob=1975, specialist='Cardiologists')
    
    print('-'*30)
    ward1 = Ward(name='Ward1')
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()

    print('-'*30)
    ward1.count_doctor()

    print('-'*30)
    print('After sorting Age of Ward1 people')
    ward1.sort_age()
    ward1.describe()

    print('-'*30)
    ward1.compute_average()