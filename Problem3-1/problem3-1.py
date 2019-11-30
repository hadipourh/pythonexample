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