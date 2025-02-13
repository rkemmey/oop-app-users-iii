# Your PremiumUser class goes here
from users.User import User

class PremierUser(User):
    def extra_benefit(self):
        print("Woohoo premium accounts have no ads.")