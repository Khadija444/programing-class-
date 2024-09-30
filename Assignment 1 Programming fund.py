# Customer class
class Customer:
#defining the attributes
    def __init__(self, customerID, name, email, contactInfo, paymentDetails):
       #all the attributes are private
        self.__customerID = customerID
        self.__name = name
        self.__email = email
        self.__contactInfo = contactInfo
        self.__paymentDetails = paymentDetails
        self.__reservations = []

    # Getter and Setter methods
    def get_customerID(self):
        return self.__customerID
    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def get_contactInfo(self):
        return self.__contactInfo
    def get_paymentDetails(self):
        return self.__paymentDetails
    def set_contactInfo(self, contactInfo):
        self.__contactInfo = contactInfo

    # Methods for the costumer class
   # to create an account for user
    def createAccount(self):
        print(f"Account created for {self.__name}")
        return True
   #to update their account if needed
    def updateAccountDetails(self, new_contactInfo):
        self.set_contactInfo(new_contactInfo)
        print(f"Contact info updated for {self.__name} to {self.__contactInfo}")
        return True
   #to add a reservation
    def addReservation(self, reservation):
        self.__reservations.append(reservation)
   # to review an existing reservation
    def viewReservations(self):
        if not self.__reservations:
            print(f"{self.__name} has no reservations.")
        else:
            for reservation in self.__reservations:
                print(f"Reservation ID: {reservation.get_reservationID()}, Status: {reservation.get_status()}")
   # to make the payment process
    def makePayment(self, payment):
        if payment.processPayment():
            print(f"Payment of ${payment.get_transactionAmount()} for {self.__name} was successful.")
            return True
        else:
            print("Payment failed.")
            return False


# Reservation class
class Reservation:
#defining the attributes of the class
    def __init__(self, reservationID, checkInDate, checkOutDate, totalPrice, roomDetails, status="Pending"):
    #all attributes are private
        self.__reservationID = reservationID
        self.__checkInDate = checkInDate
        self.__checkOutDate = checkOutDate
        self.__totalPrice = totalPrice
        self.__roomDetails = roomDetails
        self.__status = status

    # Getter and Setter methods
    def get_reservationID(self):
        return self.__reservationID
    def get_checkInDate(self):
        return self.__checkInDate
    def get_checkOutDate(self):
        return self.__checkOutDate
    def get_totalPrice(self):
        return self.__totalPrice
    def get_roomDetails(self):
        return self.__roomDetails
    def get_status(self):
        return self.__status
    def set_status(self, status):
        self.__status = status

    # Methods for the reservation class
   # to make a reservation
    def makeReservation(self):
        self.__status = "Confirmed"
        print(f"Reservation {self.__reservationID} confirmed.")
        return True
   # to cancel an exsiting reservation
    def cancelReservation(self):
        if self.__status == "Confirmed":
            self.__status = "Cancelled"
            print(f"Reservation {self.__reservationID} cancelled.")
            return True
        else:
            print(f"Reservation {self.__reservationID} is not confirmed yet or already cancelled.")
            return False
   # to update an exsiting reservation
    def updateReservation(self, new_checkInDate, new_checkOutDate):
        self.__checkInDate = new_checkInDate
        self.__checkOutDate = new_checkOutDate
        print(f"Reservation {self.__reservationID} updated to new dates.")
        return True
   # to view current reservation details
    def viewReservation(self):
        print(f"Reservation {self.__reservationID} details:\nCheck-In: {self.__checkInDate}, Check-Out: {self.__checkOutDate}, Room: {self.__roomDetails}, Status: {self.__status}")
        return self


# Room class
class Room:
#defininf all the attributes
    def __init__(self, roomID, roomType, availability, pricePerNight, amenities):
    #all attributes are private
        self.__roomID = roomID
        self.__roomType = roomType
        self.__availability = availability
        self.__pricePerNight = pricePerNight
        self.__amenities = amenities

    # Getter and Setter methods
    def get_roomID(self):
        return self.__roomID
    def get_roomType(self):
        return self.__roomType
    def get_availability(self):
        return self.__availability
    def get_pricePerNight(self):
        return self.__pricePerNight
    def get_amenities(self):
        return self.__amenities
    def set_availability(self, availability):
        self.__availability = availability

    # Methods for the room class
    # to check the availability of the room
    def checkAvailability(self):
        return self.__availability
   # to book the room
    def bookRoom(self):
        if self.__availability:
            self.__availability = False
            print(f"Room {self.__roomID} booked.")
            return True
        else:
            print(f"Room {self.__roomID} is not available.")
            return False
    # to update room details
    def updateRoomDetails(self, new_pricePerNight, new_amenities):
        self.__pricePerNight = new_pricePerNight
        self.__amenities = new_amenities
        print(f"Room {self.__roomID} details updated.")
        return True


# Payment class
class Payment:
#defininf all the attributes
    def __init__(self, paymentID, paymentMethod, paymentStatus, transactionAmount, transactionDate):
    #all attributes are private
        self.__paymentID = paymentID
        self.__paymentMethod = paymentMethod
        self.__paymentStatus = paymentStatus
        self.__transactionAmount = transactionAmount
        self.__transactionDate = transactionDate

    # Getter and Setter methods
    def get_paymentID(self):
        return self.__paymentID
    def get_paymentMethod(self):
        return self.__paymentMethod
    def get_paymentStatus(self):
        return self.__paymentStatus
    def get_transactionAmount(self):
        return self.__transactionAmount
    def get_transactionDate(self):
        return self.__transactionDate
    def set_paymentStatus(self, paymentStatus):
        self.__paymentStatus = paymentStatus

    # Methods for the payment class
    # to process a payment
    def processPayment(self):
        # For this example, assume all payments succeed.
        self.__paymentStatus = "Completed"
        return True
   # to refund a payment
    def refundPayment(self):
        if self.__paymentStatus == "Completed":
            self.__paymentStatus = "Refunded"
            print(f"Payment {self.__paymentID} refunded.")
            return True
        else:
            print(f"Payment {self.__paymentID} is not eligible for a refund.")
            return False
    # to view payment details
    def viewPaymentDetails(self):
        print(f"Payment {self.__paymentID} details: Method: {self.__paymentMethod}, Amount: ${self.__transactionAmount}, Date: {self.__transactionDate}, Status: {self.__paymentStatus}")
        return self


# Creating objects and displaying the information from Figure 1
# Customer object
customer = Customer("Khadija44", "Khadija Alhammadi", "khadijaalhammadi@gmail.com", "0512312312", "Mastercard ending in 1010")

# Room object
room = Room("204", "2 Queen Beds", True, 89.95, "No Smoking/Desk/Safe/Coffee Maker In Room/Hair Dryer/Wi-Fi/Iron table")

# Reservation object
reservation = Reservation("123123123", "Oct 22, 2024", "Oct 24, 2024", 201.48, room.get_roomType(), "Confirmed")

# Payment object
payment = Payment("PMT10001", "Mastercard", "Completed", 201.48, "Oct 22, 2024")

# Displaying the information
print("Your Reservation is Confirmed")
print(f"Your Name: {customer.get_name()}")
print(f"Your Email: {customer.get_email()}")
print(f"Hotel Confirmation Number: {reservation.get_reservationID()}")
print(f"Check-In: {reservation.get_checkInDate()}")
print(f"Check-Out: {reservation.get_checkOutDate()}")
print(f"Room: {reservation.get_roomDetails()}")
print(f"Room Type: {room.get_roomType()}")
print(f"Total Charges: ${reservation.get_totalPrice()}")

print("\nSummary of Charges")
print(f"Billing Name: {customer.get_name()}")
print(f"Credit Card: {customer.get_paymentDetails()}")
print(f"Room Cost: ${room.get_pricePerNight()} per night")
print(f"Rooms: 1")
print(f"Nights: 2")
print(f"Room Subtotal: ${room.get_pricePerNight() * 2}")
print(f"Taxes and Fees: ${reservation.get_totalPrice() - room.get_pricePerNight() * 2}")
print(f"Total Charges: ${reservation.get_totalPrice()}")

