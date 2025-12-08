from collections import Counter
from itertools import combinations
from operator import itemgetter

class location:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __repr__(self):
        return f'({self.x},{self.y},{self.z})'
    
    def __key(self):
        return (self.x, self.y, self.z)

    def __hash__(self):
        return hash(self.__key())
    
    def __eq__(self, other):
        return (self.__key() == other.__key())

    @classmethod
    def distance(cls,loc1, loc2):
        return (loc2.x-loc1.x)**2 + (loc2.y-loc1.y)**2 + (loc2.z-loc1.z)**2

   
with open('input/day8.txt', 'r') as f:
    lines = f.read().splitlines()

# Read in the locations of the boxes
boxes = []
for line in lines:
    x,y,z = line.split(",")
    boxes.append(location(x,y,z))

# Make a list of (dist, (box1, box2)) tupes, and sort them ascending on distance
distances = list()
for i in range(0, len(boxes)-1):
    for j in range(i+1, len(boxes)):
        distances.append((location.distance(boxes[i],boxes[j]), (boxes[i],boxes[j])))
distances.sort(key=itemgetter(0))

# Keep track of the circuits in a dictionary of box->circuit# (allowing fast lookups of boxes)
circuits = dict() #location->circuit
c = 0
it = 0
for distance, (box1, box2) in distances:
    if it == 1000:
        cnt = Counter(circuits.values())
        ans1=1
        for _, nr in cnt.most_common(3):
            ans1 *= nr
    if(box1 not in circuits and box2 not in circuits):
        # Add box1 and box2 to a new circuit
        circuits[box1] = c
        circuits[box2] = c
        c += 1
    elif(box1 in circuits and box2 in circuits):
        if not circuits[box1] == circuits[box2]:
            # They are in different circuits, we need to merge both circuits
            merged_c = circuits[box1]
            # Move boxes from circuit[box2] into the merged circuit
            for box, circuit in circuits.items():
                if circuit == circuits[box2]:
                    circuits[box] = merged_c           
        else:
            None #Already in the same circuit
    elif box1 in circuits:
        circuits[box2] = circuits[box1]
    elif box2 in circuits:
        circuits[box1] = circuits[box2]
    else:
        raise Exception
    uniques = len(set(circuits.values()))
    if uniques == 1 and it > 10:
        break
    it += 1
        
print(f'Stopped in iteration {it}')

print(f'Solution for day8/part1: {ans1}')
print(f'Solution for day8/part2: Last boxes {box1} and {box2} product of x coords = {box1.x*box2.x}')
