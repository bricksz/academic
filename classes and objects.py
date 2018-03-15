
import datetime



'''
class User:
    pass

user1 = User()
user1.f = "DAVE"
user1.l = "JONES"

print(user1.f, user1.l)

f = "ARTHUR"
l = "CLARKE"

print(f, l)
print(user1.f, user1.l)

user2 = User()
user2.f = "FRANK"
user2.l = "POOLE"

print(user2.f, user2.l)

user1.age = 37
user2.f_book = "2001: A Space Odyssey"

print(user1.age)
'''

class User:
    """ A member of FriendFace. For now we are
    only storing their name and birthday.
    But soon we will store an uncomfortable
    ammount of user information"""

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday   #yyyymmdd

        # extraft first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """ Return the age of the user in 10 years."""

        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) #Date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

user = User("Dave Bowman", "19710315")

print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)

print(user.age())

help(User)