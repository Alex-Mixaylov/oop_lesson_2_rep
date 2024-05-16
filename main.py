class Engine():
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Car():
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

my_car = Car()
my_car.start()
my_car.stop()

class Teacher():
    def teach(self):
        print("Teacher is teaching")

class School():
    def __init__(self, new_teacher):
       self.teacher = new_teacher

    def start_lesson(self):
        self.teacher.teach()

my_teacher = Teacher()
my_school = School(my_teacher)

