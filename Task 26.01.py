import pickle
class CarRecord:
    def __init__(self):
        self.VehicleID=""
        self.Registration=""
        self.DateOfRegistration=None
        self.EngineSize=0
        self.PurchasePrice=0.00
Car=[CarRecord()for i in range(100)]
CarFile=open("CarFile.DAT","wb")
for i in range(100):
    pickle.dump(Car[i],CarFile)
CarFile.close()
CarFile=open("CarFile.DAT","rb")
Car=[]
while True:
    Car.append(pickle.load(CarFile))
    print(Car)
CarFile.close()