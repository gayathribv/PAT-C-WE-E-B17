#This file contains the blueprint for any vehicle
#Attributes would be make, model, year, weight
# from the vehicle class we can inherit truck, car, van etc, each wtih its own attributes
# and methods that operate on these attributes. each of them can be hired out and hiring
# charges to be calculated based on distance and the purpose of hiring (varies according to
# the vehicle)

class Vehicle:
    #Blueprint for vehicle class

    def __init__(self, make, model, year, weight):
        # Initialize member attributes
        self.Make = make
        self.Model = model
        self.Year = year
        self.Weight = weight
        self.MaintDone = True
        self.TripsAfterLastMaint = 0

    def PrintDetails(self):
        print(f"Make: {self.Make}")
        print(f"Model {self.Model}")
        print(f"Year of Make: {self.Year}")
        print(f"Weight of Model: {self.Model}")
        print(f"No. of Trips after Prev Maintenance: {self.TripsAfterLastMaint}")

    def RepairDone(self):
        #Vehicle maintenance repair taken care. so set the switch MaintDone to True and reset
        # Trips AFter last maintenance to be set to 0 and incremented thereafter
        self.MaintDone = True
        self.TripsAfterLastMaint = 0
        print(f"{self.Make,  self.Model}\'s maintenance is completed. Ready to ride!!!")


class Car(Vehicle):

        def __init__(self, make, model, year, weight, numdoors,rent):
            super().__init__(make, model, year, weight)
            self.Num_doors = numdoors
            self.OutForTrip = False
            self.Rent = rent

        def PrintDetails(self):
            super().PrintDetails()
            print(f"Number of Doors = {self.Num_doors}")
            if self.OutForTrip:
                print("Presently Out for Trip: Yes")
            else:
                print("Presently Out for Trip: No")
            print(f"Rent per KM: Rs{self.Rent}")


        def GoneForTrip(self):
            if self.OutForTrip is not True:
                self.OutForTrip = True
                print(f"{self.Make} is now out for a trip")
            else:
                print(f"{self.Make} is already out for a trip")

        def BackFromTrip(self):
            if self.OutForTrip:
                self.OutForTrip = False
                self.TripsAfterLastMaint +=1
            if self.TripsAfterLastMaint > 100:
                self.MaintDone = False
                print(f"{self.Make} {self.Model} has completed 100 trips since last maintenance.")
                print(f"{self.Make} {self.Model} IS DUE FOR MAINTENANCE")

        def CalculateRent(self):
            if self.OutForTrip:
                distance = int(input("Distance covered. Enter in KM"))
                BaseRent = 100
                RentCharges = BaseRent + (distance * self.Rent)
                print(f"The Rent for {self.Make}, {self.Model} for KM{distance} works out to Rs{RentCharges}")
            else:
                if self.OutForTrip is False and self.MaintDone is False:
                    print(f"{self.Make}, {self.Model} is under Maintenance")
class Truck(Vehicle):

    def __init__(self, make, model, year, weight, trucktype, freightcharge):
        super().__init__(make, model, year, weight)
        self.TruckType = trucktype
        self.FreightCharge = freightcharge
        self.OutForTrip = False

    def PrintDetails(self):
        super().PrintDetails()
        print(f"Truck Type : {self.TruckType}")
        print(f"FreightCharge: {self.FreightCharge} ")
        print(f"Present Out For Trip: {self.OutForTrip}")

    def HireTruck(self):
        if self.OutForTrip is False:
            self.OutForTrip = True
            print(f"{self.Make}, {self.Model} is out carrying load")
        else:
            print(f"{self.Make}, {self.Model} is not for Hire")

    def TruckBackInGarage(self):
        if self.OutForTrip:
            self.OutforTrip = False
            self.TripsAfterLastMaint += 1
            if self.TripsAfterLastMaint > 100:
                self.MaintDone = False
                print(f"{self.Make} {self.Model} has completed 100 trips since last maintenance.")
                print(f"{self.Make} {self.Model} IS DUE FOR MAINTENANCE")


    def CalculateRent(self):
        if self.OutForTrip:
            load=int(input("Enter the Load under Transit in KG: "))
            Baserent = 600
            LoadFreightcharges = Baserent + load * self.FreightCharge
            print(f"The Freight Charge for {self.Make}, {self.Model}, {self.TruckType} for kg{load} is Rs{LoadFreightcharges}")
        else:
            print("Truck not for Hire")

GenVandi1 = Vehicle("Generic", "Vandi", 2020, 4650)
GenVandi1.PrintDetails()
car1 = Car("Maruti", "Baleno", 2019, 1000, 4, 50)
car1.PrintDetails()
car1.GoneForTrip()
car1.CalculateRent()
car1.BackFromTrip()
truck1 = Truck("AL", "Boss", 2019, 5000, "LCV", 100)
truck1.PrintDetails()
truck1.HireTruck()
truck1.TruckBackInGarage()
truck1.CalculateRent()
