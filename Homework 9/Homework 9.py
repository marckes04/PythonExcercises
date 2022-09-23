class Vehicle:
     def __init__(self,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance):
         self.Make = Make
         self.Model= Model
         self.Year = Year
         self.Weight = Weight
         self.NeedsMaintenance = NeedsMaintenance
         self.TripsSinceMaintenance = TripsSinceMaintenance
         
        
#getters
         
def getMake(self):
        return self.Make
    
def getModel(self):
        return self.Model
    
def getYear(self):
        return self.Year
    
def getWeight(self):
        return self.Weight
     
def getNeeds(self):
        return self.NeedsMaintenance
     
def getTrips(self):
         return self.TripsSinceMaintenance


#setters

def setMake(self,make):
        self.Make = make
         
def setModel(self,model):
        self.Model = model

def setYear(self,year):
        self.Year = year
        
def setWeight(self,weight):
        self.Weight = weight

def setNeeds(self,needsMaintenance):
         self.NeedsMaintenance = needsMaintenance

def setTrips(self,tripsSinceMaintenance):
          self.TripsSinceMaintenance = tripsSinceMaintenance
          
def __str__(self):
        return ("The car needs mantaince" + str(self.NeedsMaintenance ) )
 

class Cars(Vehicle):
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance,Drive,Stop,Repair):
        Vehicle.__init__(self,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance)
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance
        self.Drive = Drive
        self.Stop = Stop
        self.Repair = Repair
        
    def driveAuto(self):
         if self.TripsSinceMaintenance > 100:

               return(self.NeedsMaintenance == True)
         else:
              return (self.NeedsMaintenance == False)
   


def repairAuto(self):
         if self.TripsSinceMaintenance < 0:
              return("Needs reparation")


car1 = Cars("Holland","Ford",1978,120,False,101,True,False,False)
car2 = Cars("Germany","Ford",1980,120,False,90,False,False,False)
car3 = Cars("Hindi","Chevrolet",2010,120,False,103,True,True,False)

car1.driveAuto()
car2.driveAuto()
car3.driveAuto()

print(car1)
print(car2)
print(car3)
          

              
              
              
         
        

