class student_class:
    count = 0
    def __init__(self, num_of_students):
        self.num_of_students = num_of_students        
    def set_ages(self) :
        ages = input()
        self.ages = map(float, ages.split(" "))
        
    def set_heights(self):
        heights = input()
        self.heights = map(float, heights.split(" "))
        
    def set_weights(self):
        weights = input()
        weights = map(float, weights.split(" "))
        self.weights = weights
        
    def get_average_age(self):
        avg_sum = sum(self.ages)
        self.average_age = avg_sum / self.num_of_students    
        return self.average_age
    
    def get_average_height(self):
        height_sum = sum(self.heights)
        self.average_height = height_sum / self.num_of_students
        return self.average_height
    
    def get_average_weight(self):
        weight_sum = sum(self.weights)
        self.average_weight = weight_sum / self.num_of_students
        return self.average_weight
    def compare(self):
        pass
    
num_of_students_a = int(input())
class_a = student_class(num_of_students_a)
class_a.set_ages()
class_a.set_heights()
class_a.set_weights()

num_of_students_b = int(input())
class_b = student_class(num_of_students_b)
class_b.set_ages()
class_b.set_heights()
class_b.set_weights()

a_avg_age = class_a.get_average_age()
a_avg_height = class_a.get_average_height()
a_avg_weight = class_a.get_average_weight()

b_avg_age = class_b.get_average_age()
b_avg_height = class_b.get_average_height()
b_avg_weight = class_b.get_average_weight()

print("%s" % a_avg_age)
print("%s" % a_avg_height)
print("%s" % a_avg_weight)
print("%s" % b_avg_age)
print("%s" % b_avg_height)
print("%s" % b_avg_weight)

if (a_avg_height > b_avg_height):
    print("A")
elif (a_avg_height == b_avg_height):
    if (a_avg_weight < b_avg_weight):
        print("A")
    elif (a_avg_weight == b_avg_weight):
        print("Same")
    else: 
        print("B")
else:
    print("B")
