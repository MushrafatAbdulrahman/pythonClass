class User():
    first_name = ""
    last_name = ""
    email_address = ""
    phone_number = ""
    allergies = ""
    food_diet = ""
    user_type = ""
    is_active = False

    def get_full_name(self):
        return "{},{}".format(self.first_name, self.last_name)

class MealItem():
    name = ""
    description = ""
    serving_size = ""
    allergens = ""


class Order():
    day = ""
    weekly_reoccurence = ""



class Price():
    per_plate_price = ""

class Review():
    feedback = ""


user = User()
user.first_name = "Mush"
user.last_name = "Rahman"
user.phone_number = "0201709434"
user.email_address = "mushrahman@yahoo.com"

print("My first and last name is {}".format(user.get_full_name()))



class Father():
    last_name = ''
    company = ''
    __wife__ = ''

class Son(Father):
    first_name = ''

son = Son()
son.last_name = 'Rahman'
son.company = 'Geo World'
son.first_name = 'Mush'

print("{}".format(son.last_name))
