students = [
    {"name" : 'Shihab', 'house' : 'Shah Paran Hall', 'home town' : 'Cumilla'},
    {"name" : 'Jabed', 'house' : 'Borogul', 'home town' : 'Chittagong'},
    {"name" : 'Jabir', 'house' : 'Shah Paran Hall', 'home town' : 'Tangail'},
    {"name" : 'Jabed', 'house' : 'Dhamali Para', 'home town' : 'Tangail'},
    {"name" : 'Likhon', 'house' : None , 'home town' : 'Tangail'}
]

for student in students:
  print(student['name'], student['house'], student['home town'], sep = ', ')