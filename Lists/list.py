
myUniqueList = []

def add(number):
    if number in myUniqueList:
        return False, myUniqueList
    else:
        myUniqueList.append(number)
        return True, myUniqueList


print(add(5))

print(add(1))

print(add(5))
