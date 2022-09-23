ParticipantNumber = 5
ParticipantData = []
registeredParcipants = 0
outputFile = open("ParticipantData.txt","w")


while(registeredParcipants < ParticipantNumber):
    tempPartData = [] #name,country of origin, age
    
    name = input("Please Enter your Name: ")
    tempPartData.append(name)
    country = input("Please enter your country of origin: ")
    tempPartData.append(country)
    age = int(input("Please enter your age: "))# int("25) -> 25
    tempPartData.append(age)
    print(tempPartData)
    ParticipantData.append(tempPartData)#[tempPartData]= [name,country of origin, age]
    print(ParticipantData)
    
    registeredParcipants +=1 # registered participants +1
    

    
for participant in ParticipantData:
    for data in participant:
        outputFile.write(str(data))# str(25)
        outputFile.write(" ")#MaxU.S.21
                             #Bob Canada 25
    outputFile.write("\n")
    
outputFile.close()

inputFile = open("ParticipantData.txt","r")

inputList = []

for line in inputFile:
    tempParticipant = line.strip("\n").split()
    print(tempParticipant)
    inputList.append(tempParticipant)
    print(inputList)
                     
    #"Max U.S 21 \n".strip("\n") -> Max U.S. 21
    #"Max U.S 21".split() -> ["Max","21"]


Age = {}
print(inputList)
for part in inputList:
    tempAge = int(part[-1])
    
    if tempAge in Age:
        Age[tempAge] += 1
    else:
        Age[tempAge] = 1
        
print(Age)

Countries = {}
for part in inputList:
    tempCountry = part[1]
    
    if tempCountry in Countries:
        Countries[tempCountry] += 1
    else:
        Countries[tempCountry] = 1
        
print("Countries thar attended:",Countries)
Oldest = 0
Youngest = 100
counter = 0

for tempAge in Age:
    if tempAge > Oldest:
        Oldest = tempAge
    if tempAge < Youngest:
        Youngest = tempAge
    if Age[tempAge]>=counter:
        counter = Age[tempAge]
        mostOcurringAge = tempAge
print(Oldest)
print(Youngest)
print("Most Ocurring age is: ",mostOcurringAge,"with",counter,"participants")
inputFile.close()
