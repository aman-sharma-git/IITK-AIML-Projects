#import the built-in module DateTime to handle the rental time and bill
import datetime

#create a class for renting the cars 
class CarRental:
        #Constructor class to represent car rental shop.
    def __init__(self,stock=0):
        self.stock = stock

        #Displays the currently available cars for rent.
    def displaystock(self):
        print("We have currently {} cars available to rent.".format(self.stock))
        return self.stock
    
        #Rent a car on hourly basis to a customer.
    def rent_car_on_hourlybasis(self,n):

        if n <= 0:
            print("NUmber of cars should be positive.")
            return None
        elif n> self.stock:
            print("Sorry... We have currently {} cars available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()   
            print("You have rented a {} car(s) on hourly basis today at {} hours.".format(n,now.hour))
            print("You will be charged $10 for each hour per car.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now

        #Rent a car on daily basis to a customer.
    def rent_car_on_dailybasis(self,n):

        if n <= 0:
            print("NUmber of cars should be positive.")
            return None
        elif n> self.stock:
            print("Sorry... We have currently {} cars available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()   
            print("You have rented a {} car(s) on daily basis today at {} hours.".format(n,now.hour))
            print("You will be charged $50 for each day per car.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now
    
        #Rent a car on weekly basis to a customer.
    def rent_car_on_weeklybasis(self,n):

        if n <= 0:
            print("NUmber of cars should be positive.")
            return None
        elif n> self.stock:
            print("Sorry... We have currently {} cars available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()   
            print("You have rented a {} car(s) on weekly basis today at {} hours.".format(n,now.hour))
            print("You will be charged $250 for each week per car.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now
    

        """
        1. Accept a rented car from a customer
        2. replensihes the inventory
        3. return a bill
        """
    def return_Car(self, request):

        RentalTime, RentalBasis, NumOfCars = request
        Bill = 0

        if RentalTime and RentalBasis and NumOfCars:
            self.stock += NumOfCars
            now = datetime.datetime.now()
            RentalPeriod = now - RentalTime

            #Hourly Bill Calculation
            if RentalBasis == 1:
                Bill = round(RentalPeriod.seconds / 3600)*10*NumOfCars

            #Daily Bill Calculation
            elif RentalBasis == 2:
                Bill = round(RentalPeriod.days)*50*NumOfCars

            #Weekly Bill Calculation
            elif RentalBasis == 3:
                Bill = round(RentalPeriod.days / 7)*250*NumOfCars
            
            if(3 <= NumOfCars <= 5):
                print("You are eligible for Family Rental Promotion of 30% discount.")
                Bill = Bill * 0.7
            
            print("Thanks for returning your car. Hope you enjoyed our Service...")
            print("That would be ${}".format(Bill))
            return Bill
        else:
            print("Are your sure you rented a car with us?")
            return None
        


#Create a class for Customer
class Customer:
    #Consturctor Method to represent various customer objects.
    def __init__(self):

        self.Cars = 0
        self.RentalBasis = 0
        self.RentalTime = 0
        self.Bill = 0


    #Takes a request from the customer for the numbers of Cars.
    def requestCar(self):
        Cars = input("How many cars would you like to rent?")
        try:
            Cars = int(Cars)
        except ValueError:
            print("That's not a postive integer...")
            return -1
        
        if Cars < 1:
            print("Invalid input. Number of Cars should be greater than Zero...")
            return -1
        else:
            self.Cars = Cars
        return self.Cars
    
    #Allows customers to return thier cars to the rental shop.
    def return_Car(self):
        if self.RentalBasis and self.RentalTime and self.Cars:
            return self.RentalTime, self.RentalBasis, self.Cars
        else:
            return 0,0,0