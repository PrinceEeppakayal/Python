
# QUESTION: Write a class Train which has methods to book a ticket, get Status(no of Seats) and get fare information of trains running under Indian Railways

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")

    def getFare(self):
        print(f"The fare of the ticket is Rs.{self.fare}")

    def bookTicket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry, the train is full! No seats available.") 

    def cancelTicket(self, seatNo):
        print(f"Your ticket with seat number {seatNo} has been cancelled!")
        self.seats = self.seats + 1

chennai = Train("Chennai Express", 500, 10)
chennai.getStatus()
chennai.getFare()
chennai.bookTicket()
chennai.bookTicket()
chennai.getStatus()
chennai.cancelTicket(2)
chennai.getStatus()
