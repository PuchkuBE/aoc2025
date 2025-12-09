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

def search_set(box:location, s: list[set]):
    for i,st in enumerate(s):
        if box in st:
            return i
    return None
   
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
circuits = [{box} for box in boxes]
it = 0
for distance, (box1, box2) in distances:
    if it == 1000:
        c = sorted(circuits, key=len, reverse=True)
        ans1 = len(c[0]) * len(c[1]) * len(c[2])
    circ1 = search_set(box1, circuits)
    circ2 = search_set(box2, circuits)
    if not circ1 == circ2:
        circuits[circ1] = circuits[circ1] | circuits[circ2]
        del circuits[circ2]
    if len(circuits) == 1:
        ans2 = box1.x * box2.x
        break
    it += 1
        
print(f'Solution for day8/part1: {ans1}')
print(f'Solution for day8/part2: Last boxes {box1} and {box2} product of x coords = {box1.x*box2.x}')
