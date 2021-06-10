import new_uuid
import random

"""
Testing:
- Generate 1000 UUIDs
- Add to dictionary with key, value being UUID and generation sequence counter
- Add to unordered list
- Shuffle the list
- Sort the list
- Iterate through the sorted list and compare current list position to dictionary's value to verify they match
"""

# Global Variables
devDebugs = False # True to view generation process
returnType = "hex" # String Values: bin, int, hex

showUUIDs = False # True to view the generated UUID returnType and lists

def v7Tests(showUUIDs):
    counter = 0
    testList = []
    masterDict = {}
    while counter < 1000:
        UUIDv7 = new_uuid.uuid7(devDebugs, returnType)
        testList.append(UUIDv7)
        masterDict[UUIDv7] = counter
        counter += 1

    if showUUIDs:
        print("\n")
        print("Start List")
        counter = 0
        for UUID in testList:
            print('{0}: {1}'.format(str(counter), UUID))
            counter+= 1

    random.shuffle(testList)
    if showUUIDs:
        print("\n")
        print("Shuffled List")
        counter = 0
        for UUID in testList:
            print('{0}: {1}'.format(str(counter), UUID))
            counter += 1

    print("\n")
    print("Post Sorted List Results")
    testList.sort()
    counter = 0
    failCount = 0
    for UUID in testList:
        if masterDict[UUID] != counter:
            failCount+=1
            print('{0}: {1}'.format(str(counter), UUID))
        counter+= 1
    if failCount == 0:
        print("+ No Failures Observed")

v7Tests(showUUIDs)
