
class Garage():
    
    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9,10]
        self.parking_spaces = [1,2,3,4,5,6,7,8,9,10]
        self.current_ticket = {}
    
    def take_ticket(self):
        tickets = self.tickets
        parking_spaces = self.parking_spaces
        if tickets == []:
            print("Sorry we are full!")
        else:
            ticket1 = self.tickets.pop(0)
            print(f'Please take ticket {ticket1} ')
            print(self.tickets)
            parking1 = self.parking_spaces.pop(0)
            print(parking_spaces)
            self.current_ticket[ticket1]= ''
            print(self.current_ticket)
        
    
    def pay_park(self):
        pay_ticket = int(input(f'Please enter your ticket number: '))
        if pay_ticket in self.current_ticket:
            self.current_ticket[pay_ticket]
            payment = input(f'Please pay your ticket: PRESS "P" TO FINISH PAYMENT ')
            if payment.lower() == 'p':
                print(f'Thank you for your payment, you have 15 min to leave the garage')
                self.current_ticket[pay_ticket]= 'paid'
            else:
                print('Your payment was declined. Please try again')
        else:
            print("Oops ticket number unavailable try again")

    def leave_garage(self):
        leave_ticket = int(input(f'Please enter your ticket number: '))
        if leave_ticket in self.current_ticket:
            paid_ticket = self.current_ticket[leave_ticket]
            if paid_ticket == 'paid':
                print("Thank you have a nice day!")
                self.tickets.append(leave_ticket)
                self.parking_spaces.append(leave_ticket)
                self.current_ticket.pop(leave_ticket)
            else:
                print("Sorry you havent paid please select pay")
        else:
            print("Oops ticket number unavailable try again")
    

class UI(Garage):
    def __init__(self):
        super().__init__()
    def run_program(self):
        while True:
            welcome_ = input("Would you like to park here? Yes or No ")
            if welcome_.lower( )== 'yes':
                break
            elif welcome_.lower( )== 'no':
                exit()
            else:
                print("Sorry try again")

        while True:
            response = input("Would you like to park, pay or leave?: ")
            if response.lower() == 'park':
                self.take_ticket()
            elif response.lower() == 'pay':
                self.pay_park()

            elif response.lower() == 'leave':
                self.leave_garage()

            elif response.lower() == 'quit':
                break

            else:
                print("Oops incorrect try again!")

ui = UI()
ui.run_program()

