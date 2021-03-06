   
def assignmentToIndex(coordinate,dimension):
    lengthDimension = len(dimension)
    lengthCoordinate = len(coordinate)
    if (lengthDimension<>lengthCoordinate):
        raise Exception("Dimension mismatch")
    for i in range(lengthDimension):
        if (not isinstance(coordinate[i], int)):
            raise Exception("Coordinate must be integer")
        if (not isinstance(dimension[i], int)):
            raise Exception("Dimension must be interger")
        if (dimension[i]<1):
            raise Exception("Dimension must be greater than 0")
        if (coordinate[i]<0):
            raise Exception("Coordindate must be greater or equal than 0")
        if (coordinate[i]>=dimension[i]):
            raise Exception("Coordinate exceeds dimension")
    group=[]
    group.append(1)
    accumulator=group[0]
    for i in range(1,lengthDimension):
        group.append((dimension[lengthDimension-i])*accumulator)
        accumulator=group[i]
    accumulator = 0
    for i, n in enumerate(reversed(coordinate)):
        accumulator=accumulator+group[i]*n
    result = accumulator
    return result

#tests
print "Tests"

d = [3,1,3]
c = [1,0,2]

print "Happy test"
print "dimension"
print d
print "coordinate"
print c
print "000   [0,0,0-2]"
print "010   [1,0,0-2]"
print "000   [2,0,0-2]"
print "result"
result = assignmentToIndex(c,d)
print result
print "expected"
expected = 5
print expected
if (result == expected):
    print "pass"
else:
    print "failed"

d = [2,2]
c = [1,1]

print "Happy test 2"
print "dimension"
print d
print "coordinate"
print c
print "00   [0,0-1]"
print "01   [1,0-1]"
print "result"
result = assignmentToIndex(c,d)
print result
print "expected"
expected = 3
print expected
if (result == expected):
    print "pass"
else:
    print "failed"

d = [4,2]
c = [2,1]

print "Happy test 3"
print "dimension"
print d
print "coordinate"
print c
print "00   [0,0-1]"
print "01   [1,0-1]"
print "00   [2,0-1]"
print "00   [3,0-1]"
print "result"
result = assignmentToIndex(c,d)
print result
print "expected"
expected = 5
print expected
if (result == expected):
    print "pass"
else:
    print "failed"

d = [2,3,4]
c = [1,1,3]

print "Happy test 4"
print "dimension"
print d
print "coordinate"
print c
print "0000   [0,0,0-3]"
print "0000   [0,1,0-3]"
print "0000   [0,2,0-3]"
print "0000   [1,0,0-3]"
print "0001   [1,1,0-3]"
print "0000   [1,2,0-3]"
print "result"
result = assignmentToIndex(c,d)
print result
print "expected"
expected = 19
print expected
if (result == expected):
    print "pass"
else:
    print "failed"


d = [3,1,3]
c = [0,1,2]
             
print "Exception: Coordinate exceeds dimension"
print "dimension"
print d
print "coordinate"
print c
print "result"
try:
    assignmentToIndex(c,d)
except Exception, e:
    result = str(e)
    print result
print "expected"
print expected
expected = "Coordinate exceeds dimension"
if (result == expected):
    print "pass"
else:
    print "failed"


d = [3.1,1,3]
c = [0,1,2]
             
print "Exception: Dimension must be interger"
print "dimension"
print d
print "coordinate"
print c
print "result"
try:
    assignmentToIndex(c,d)
except Exception, e:
    result = str(e)
    print result
print "expected"
expected = "Dimension must be interger"
print expected
if (result == expected):
    print "pass"
else:
    print "failed"


d = [3,1,3]
c = [0,0,2.1]
             
print "Exception: Coordinate must be integer"
print "dimension"
print d
print "coordinate"
print c
print "result"
try:
    assignmentToIndex(c,d)
except Exception, e:
    result = str(e)
    print result
print "expected"
expected = "Coordinate must be integer"
print expected
if (result == expected):
    print "pass"
else:
    print "failed"

d = [3,1,3]
c = [0,0,2,4]
             
print "Exception: Dimension mismatch"
print "dimension"
print d
print "coordinate"
print c
print "result"
try:
    assignmentToIndex(c,d)
except Exception, e:
    result = str(e)
    print result
print "expected"
expected = "Dimension mismatch"
print expected
if (result == expected):
    print "pass"
else:
    print "failed"


d = [0,1,3]
c = [0,0,2]
             
print "Exception: Dimension must be greater than 0"
print "dimension"
print d
print "coordinate"
print c
print "result"
try:
    assignmentToIndex(c,d)
except Exception, e:
    result = str(e)
    print result
print "expected"
expected = "Dimension must be greater than 0"
print expected
if (result == expected):
    print "pass"
else:
    print "failed"


d = [2,1,3]
c = [-1,0,2]
             
print "Exception: Coordindate must be greater or equal than 0"
print "dimension"
print d
print "coordinate"
print c
print "result"
try:
    assignmentToIndex(c,d)
except Exception, e:
    result = str(e)
    print result
print "expected"
expected = "Coordindate must be greater or equal than 0"
print expected
if (result == expected):
    print "pass"
else:
    print "failed"

