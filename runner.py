from users.User import User
from users.FreeUser import FreeUser
from users.PremiumUser import PremierUser

jim = FreeUser('jim', 'jim@yahoo.com', '12345')
bob = PremierUser('bob', 'bob@hotmail.com', '67891')

print(bob.name, bob.email)
print(jim.name, jim.email)
# bob.create_a_post()
# bob.create_a_post()
# bob.create_a_post()
# bob.see_my_posts()
jim.create_a_post()
jim.create_a_post()
jim.create_a_post()
jim.see_all_posts()
#print(type(bob))