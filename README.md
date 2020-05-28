# Python Examples
This repository consists of some python examples for who want to learn advanced Python programming.

# Contents
1 - [Chapter 1: Introduction](#chapter1)

* [Problem 1-1](#problem1-1)
* [Problem 2-1](#problem2-1)
* [Problem 3-1](#problem3-1)
* [Problem 4-1](#problem4-1)
---
2 - [Chapter 2: Object-Oriented Programming (OOP) With Python](#chapter2)

* [Problem 1-2](#problem1-2)
* [Problem 2-2](#problem2-2)

3 - [Chapter 3: Parallel Programming in Python](#parallel_programming)

<a name="chapter1"></a>
# Chapter 1 - Introduction

<a name="problem1-1"></a>
## Problem 1-1

Write a Python program reading ten integer numbers from terminal, and output the number which has the maximum number of distinct prime divisors, and it's number of disticnt prime divisiors too. If more than one numbers have such a property, it must does that for one which is the maximum. 


Sample input: 
```
123
43
54
12
76
84
98
678
543
231
```

Output:
```
678 3
```


```python
def num_of_distinct_prime_divisors(n):
    d = 2
    distinct_divisors = []
    while (n != 1):
        if (n % d == 0):
            n //= d
            if d not in distinct_divisors:
                distinct_divisors.append(d)
        else:
            d += 1
    return len(distinct_divisors)

input_data = int(input())
output, output_ndivs = input_data, num_of_distinct_prime_divisors(input_data)
for i in range(9):
    input_data = int(input())
    temp = num_of_distinct_prime_divisors(input_data)
    if (temp > output_ndivs):
        output, output_ndivs = input_data, temp
    elif (temp == output_ndivs):
        if (input_data > output):
            output = input_data
print(output, output_ndivs)
```

<a name="problem2-1"></a>
## Problem 2-1

The group B of 2018 FIFA world cup consisted of Iran, Portugal, Spain, and Morocco. The results of the mathces can be found [here](https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_B). 
Write a Python program to receive the results of the matches, and then compute the number of wins, losts, and the goal differences, and point of each team, and finally print out the name of each team, and the computed paramaters in front of it in a seperate line, where the output must be ordered based on the points, and if the points are the same, they must be ordered based on the number of wins, and if the number of wins are the same too, they must be orderd in lexicographic order. It is assumed that the inputs are given based on the following order:

```
Iran-Spain
Iran-Portugal
Iran-Morocco
Spain-Portugal
Spain-Morocco
Portugal-Morocco
```

Sample Input: 
```
2-2
2-1
1-2
2-2
3-1
2-1
```
Sample Output:
```
Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3
```


```python
from operator import itemgetter
list_of_teams = [{} for i in range(4)]
list_of_teams[0]["name"] = "Iran"
list_of_teams[1]["name"] = "Spain"
list_of_teams[2]["name"] = "Portugal"
list_of_teams[3]["name"] = "Morocco"
game_schedule = [[i, j] for i in range(3) for j in range(i + 1, 4)]
for i in range(6):
    result = input()    
    result = result.split("-")    
    result = list(map(int, result))
    list_of_teams[game_schedule[i][0]]["goals_for"] = list_of_teams[game_schedule[i][0]].get("goals_for", 0) + result[0]    
    list_of_teams[game_schedule[i][0]]["goals_against"] = list_of_teams[game_schedule[i][0]].get("goals_against", 0) + result[1]    
    list_of_teams[game_schedule[i][1]]["goals_for"] = list_of_teams[game_schedule[i][1]].get("goals_for", 0) + result[1]    
    list_of_teams[game_schedule[i][1]]["goals_against"] = list_of_teams[game_schedule[i][1]].get("goals_against", 0) + result[0]    
    if result[0] > result[1]:
        list_of_teams[game_schedule[i][0]]["wins"] = list_of_teams[game_schedule[i][0]].get("wins", 0) + 1
        list_of_teams[game_schedule[i][1]]["wins"] = list_of_teams[game_schedule[i][1]].get("wins", 0) + 0
        list_of_teams[game_schedule[i][1]]["losts"] = list_of_teams[game_schedule[i][1]].get("losts", 0) + 1
        list_of_teams[game_schedule[i][0]]["losts"] = list_of_teams[game_schedule[i][0]].get("losts", 0) + 0
        list_of_teams[game_schedule[i][0]]["draws"] = list_of_teams[game_schedule[i][0]].get("draws", 0) + 0
        list_of_teams[game_schedule[i][1]]["draws"] = list_of_teams[game_schedule[i][1]].get("draws", 0) + 0
    elif result[1] > result[0]:
        list_of_teams[game_schedule[i][1]]["wins"] = list_of_teams[game_schedule[i][1]].get("wins", 0) + 1
        list_of_teams[game_schedule[i][0]]["wins"] = list_of_teams[game_schedule[i][0]].get("wins", 0) + 0
        list_of_teams[game_schedule[i][0]]["losts"] = list_of_teams[game_schedule[i][0]].get("losts", 0) + 1
        list_of_teams[game_schedule[i][1]]["losts"] = list_of_teams[game_schedule[i][1]].get("losts", 0) + 0
        list_of_teams[game_schedule[i][0]]["draws"] = list_of_teams[game_schedule[i][0]].get("draws", 0) + 0
        list_of_teams[game_schedule[i][1]]["draws"] = list_of_teams[game_schedule[i][1]].get("draws", 0) + 0
    else:
        list_of_teams[game_schedule[i][0]]["draws"] = list_of_teams[game_schedule[i][0]].get("draws", 0) + 1
        list_of_teams[game_schedule[i][1]]["draws"] = list_of_teams[game_schedule[i][1]].get("draws", 0) + 1
        list_of_teams[game_schedule[i][1]]["wins"] = list_of_teams[game_schedule[i][1]].get("wins", 0) + 0
        list_of_teams[game_schedule[i][0]]["wins"] = list_of_teams[game_schedule[i][0]].get("wins", 0) + 0
        list_of_teams[game_schedule[i][0]]["losts"] = list_of_teams[game_schedule[i][0]].get("losts", 0) + 0
        list_of_teams[game_schedule[i][1]]["losts"] = list_of_teams[game_schedule[i][1]].get("losts", 0) + 0
for team in list_of_teams:
    team["goal difference"] = team["goals_for"] - team["goals_against"]
    team["points"] = 3*team["wins"] + team["draws"]
list_of_teams = sorted(list_of_teams, key = itemgetter("points", "wins"), reverse = True)
team_points_and_wins = lambda x : (x["points"], x["wins"])
###### This part might be reduced ###
target_index = []
for i in range(3):
    if (team_points_and_wins(list_of_teams[i]) == team_points_and_wins(list_of_teams[i + 1])):
        target_index.append(i)
if target_index != []:
    part1 = list_of_teams[0 : target_index[0]]
    part2 = sorted(list_of_teams[target_index[0] : target_index[-1] + 2], key = itemgetter("name"))
    if (target_index[-1] + 2 < 4):
        part3 = list_of_teams[target_index[-1] + 2 : 5]
        list_of_teams = part1 + part2 + part3
    else:
        list_of_teams = part1 + part2
#####################################
for team in list_of_teams:
    print("%s  wins:%d , loses:%d , draws:%d , goal difference:%d , points:%d" \
          % (team["name"], team["wins"], team["losts"], team["draws"], team["goal difference"], team["points"]))
```

<a name="problem3-1"></a>
## Problem 3-1

In a voting about six different cinematic genre, one must chose three out of the six following geners: 

1- Horror,

2- Romance,

3- Comedy,

4- History,

5- Adventure,

6- Action

Write a Python program to recieve the number of attended persons, and the name of each person with three geners he (she) is interested to, and then print out the number of persons who are interested to a each genere. If the number of those who are interested to some geners are the same, those generes must be sorted in lexicographic order in the output. 

Sampl Input: 

```
4 
hossein Horror Romance Comedy
mohsen Horror Action Comedy
mina Adventure Action History
sajjad Romance History Action
```

Sample Output:

```
Action : 3
Comedy : 2
History : 2
Horror : 2
Romance : 2
Adventure : 1
```


```python
n = int(input())
votes = dict()
geners = ["Horror", "Romance", "Comedy", "History", "Adventure", "Action"]
for i in range(n):
    person_interests = input()
    person_interests = person_interests.split(" ")    
    for j in range(3):        
        votes[person_interests[j + 1]] = votes.get(person_interests[j + 1], 0) + 1
votes = [(geners[i], votes.get(geners[i], 0)) for i in range(6)]
votes = sorted(votes, key = lambda v : v[1], reverse = True)
###### can be reduced ####
for j in range(5, 1, -1):
    for i in range(j):
        if votes[i][1] == votes[i + 1][1]:
            if votes[i][0] > votes[i + 1][0]:
                votes[i + 1], votes[i] = votes[i], votes[i + 1]
##########################            
for v in votes:
    print("%s : %d" % (v[0], v[1]))
```

    4
    hossein Horror Romance Comedy
    mohsen Horror Action Comedy
    mina Adventure Action History
    sajjad Romance History Action
    Action : 3
    Comedy : 2
    History : 2
    Horror : 2
    Romance : 2
    Adventure : 1


<a name=problem4-1></a>
# Problem 4-1


```python

```

    AhmadMaster


<a name=chapter2></a>
# Chapter 2 - Object-Oriented Programming (OOP) With Python

<a name=problem1-2></a>
## Problem 1-2

Let's say we are given the weights, heights, and ages of the students of two classes A, and B. Write a Python program to compare these classes according to the average height of students. If the average height is the same, compare them based on the average of weights, and if the weight averages are the same too, the word `same` must be printed out. A sample input and output is as follows: 

```
5
16 17 15 16 17
180 175 172 170 165
67 72 59 62 55
5
15 17 16 15 16
166 156 168 170 162
45 52 56 58 47
```

```
16.2
172.4
63.0
15.8
164.4
51.6
A
```


```python
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
```

    3
    15 17 14
    156 162 168
    45 52 48
    3
    16 17 15
    175 180 178
    65 72 68
    15.333333333333334
    162.0
    48.333333333333336
    16.0
    177.66666666666666
    68.33333333333333
    B


<a name=problem2-2></a>
## Problem 2-2

Write a Python program to receive the birth date of a person and calculate his (or her) age. The input format is `yyyy/mm/dd` and, this program print out `WRONG` when the input birth date is a wrong date. 

Sample input:
```
1995/02/03
```
Sample output: 
```
23
```

Hint : you can use the datetime library


```python
from datetime import datetime
todays_date = datetime.now()
birth_date = input()
birth_year = int(birth_date.split("/")[0])
birth_month = int(birth_date.split("/")[1])
birth_day = int(birth_date.split("/")[2])
if (birth_month > 12):
    print("WRONG")
elif (birth_day > 31):
    print("WRONG")
else:
    birth_date = datetime(birth_year, birth_month, birth_day)
    age = todays_date - birth_date
    age = age.days // 365
    print(age)
```

    1995/02/03
    24


<a name="parallel_programming"></a>
# Chapter 3 - Parallel Programming in Python

<a name="problem1-3"></a>
## Problem 1-3

Build a list of random integer numbers, and make them squared in parallel.


```python
import platform
from random import seed, randint
from time import time
from multiprocessing import Process, current_process, cpu_count

# Geeting the number of cores
num_of_cores = cpu_count()

# Constructing a random sequence
seed(time())
min_member = 0
max_member = 100
seq_length  = num_of_cores * 4
seq = [randint(min_member, max_member) for _ in range(seq_length)]
subseq_length = seq_length // num_of_cores
sub_seq = [[seq[i] for i in range(j*subseq_length, (j + 1)*subseq_length)] for j in range(num_of_cores)]

    
def square(int_list):    
    
    pid = current_process().name    
    output = []*(len(int_list))    
    for x in int_list:
        output.append(x**2)
    print(f"process id: {pid}")
    return output

# Setup a list of processes that we want to run
processes = [Process(target = square, args = (sub_seq[i], )) for i in range(num_of_cores)]

# Run processes
for pr in processes:
    pr.start()

# Exit the completed processes
for pr in processes:
    pr.join()
```

    process id: Process-569
    process id: Process-570
    process id: Process-571
    process id: Process-572
    process id: Process-573
    process id: Process-574
    process id: Process-575
    process id: Process-576



```python
from multiprocessing import Pool
from time import time
# Getting the number of cores
num_of_cores = cpu_count()

# Constructing a random sequence
seed(time())
min_member = 0
max_member = 100
seq_length  = num_of_cores * 4
seq = [randint(min_member, max_member) for _ in range(seq_length)]
subseq_length = seq_length // num_of_cores
sub_seq = [[seq[i] for i in range(j*subseq_length, (j + 1)*subseq_length)] for j in range(num_of_cores)]

def square(int_list):    
    
    pid = current_process().name    
    output = []*(len(int_list))    
    for x in int_list:
        output.append(x**2)
    print(f"process id: {pid}")
    return output
start_time = time()
with Pool(num_of_cores) as pool:
    results = [pool.apply(square, (sub_seq[i], )) for i in range(num_of_cores)]
elapsed_time = time() - start_time
print(results)
print(f"elapsed time : {elapsed_time}")
```

    process id: ForkPoolWorker-745
    process id: ForkPoolWorker-746
    process id: ForkPoolWorker-747
    process id: ForkPoolWorker-748
    process id: ForkPoolWorker-749
    process id: ForkPoolWorker-750
    process id: ForkPoolWorker-751
    process id: ForkPoolWorker-752
    [[225, 1764, 3136, 100], [3136, 5476, 3249, 1225], [5041, 169, 1156, 3721], [2704, 3969, 3136, 3364], [1849, 4900, 2500, 4], [9409, 6561, 1, 4900], [4096, 8100, 2401, 5476], [729, 7225, 8649, 7744]]
    elapsed time : 0.15274930000305176



```python

```
