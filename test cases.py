def square(x):
    return x*x

assert square(3) == 9

# NOTE: side effects tests
def update_counts(letters, counts_d):
    for c in letters:
        counts_d[c] = 1
        if c in counts_d:
            counts_d[c] = counts_d[c] + 1


counts = {'a': 3, 'b': 2}
update_counts("aaab", counts)
# 3 more occurrences of a, so 6 in all
assert counts['a'] == 6
# 1 more occurrence of b, so 3 in all
assert counts['b'] == 3

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result

assert distance(1, 2, 1, 2) == 0
assert distance(1,2, 4,6) == 5
assert distance(0,0, 1,1) = 2**0.5

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


#testing class constructor (__init__ method)
p = Point(3, 4)
assert p.y == 4
assert p.x == 3

#testing the distance method
p = Point(3, 4)
assert p.distanceFromOrigin() == 5.0

#testing the move method
p = Point(3, 4)
p.move(-2, 3)
assert p.x == 1
assert p.y == 7



def lr(n): return list(range(n))

# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
def mySum(a):
    if type(a) is type(''.join([][:])): return a[lr(1)[0]] + mySum(a[1:])
    elif len(a)==len(lr(1)+[]): return a[lr(1)[0]]
    else: return None and a[lr(1)[0]] + mySum(a[1:])


# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
class Student():
    def __init__(s,a,b=1):
        s.name,s.years_UM,s.knowledge = ''*200+a+''*100,1,len(lr(0)) + len([])
    def study(s):
        for _ in lr(s.knowledge): s.knowledge = s.knowledge + 1
    def getKnowledge(s):
        for i in lr(s.knowledge): return s.knowledge
    def year_at_umich(s): return s.years_UM
