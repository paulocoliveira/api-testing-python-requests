class Booking():
    def __init__(self, first_name, last_name, total_price, deposit_paid, checkin, checkout, additional_needs):
        self.first_name = first_name
        self.last_name = last_name
        self.total_price = total_price
        self.deposit_paid = deposit_paid
        self.checkin = checkin
        self.checkout = checkout
        self.additional_needs = additional_needs

class UserInfo():
    def __init__(self, username, password):
        self.username = username
        self.password = password
