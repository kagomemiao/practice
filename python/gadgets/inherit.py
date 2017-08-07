class Parent():
    def __init__(self, last_name, eye_color):
        print("P constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, toys_num):
        print("C constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.toys_num = toys_num

kat_wang = Child("Wang","brown", 7)

print(kat_wang.last_name)
print(kat_wang.toys_num)
