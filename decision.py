age = 18

if (age < 18):
    print("Still Growing")
elif age >=18 and age < 21:
    print("You're an adolescent")
else:
    print("You're an adult")


users = ["James", "John", "Sandra", "Monica", "Monalisa"]

index = 0
length = len(users)

for user in users:
    print("User Name is: " + user)

# while index < length:
#     print(users[index])
#     index += 1

# numbers = []
# index = 0
# while (index < 100):
#     numbers.append(index)
#     index +=1
# print(numbers)

# a = input("Enter your value: ")
# calc = input("Enter operator:")
# b = input("Enter your value: ")

# def add(a, b):
#     print(a + b)

# def subtract(a,b):
#     print(a - b)

# def multiply(a, b):
#     print(a*b)

# def divide(a, b):
#     print(a / b)

# # def calculator():
    


# add(a,b)
# subtract(a,b)
# multiply(a,b)
# divide(a,b)


my_list = ["Mush", "Moon"]
print(my_list)

print(my_list[1])

my_list.insert(0, "Mar")

print(my_list)

my_dict = {
    "id" : 001,
    "name": "Mush",
    "language" : [{"lang":"English", "proficiency":100},
                  {"lang":"French", "proficiency":99}
                ],
    "loans": [{"package": "Student Loan", "amount": 1000},
              {"package": "Car Loan", "amount": 900},
              {"package": "House Loan", "amount": 19000}
            ],
    "is_programmer": True,
    "salary": 1.2,
    "skills": ["Python", "Flutter", "Java"],
}

print(my_dict)
print(my_dict.get("name"))

if (my_dict.get("is_programmer") == True):
    print(my_dict["skills"][2])
    print(my_dict["language"][1]["lang"])
    print(my_dict["loans"][1]["amount"])


my_set = {"Lucky", "Funmi", "Lucky", "Caleb", "Caleb"}
my_set.add("Mush")

print(my_set)

my_tuple = ("Hello", "World!")

print(my_tuple)

#create a list of users to have the following fields
# id, name, email, phone number, n0 of visits, posts (post id, title, summary)
# at least 10 users

#print user, number of visit, number of post

user = [
    {"id" : 1,
    "email" : "mushrahman@yahoo.com",
    "phone" : "0244792063",
    "visits" : 10,
    "posts" : [
        {"postId" : "P001", "title" : "Greek Style Interior", "summary" : "Greek Interior Trends 2022"},
        {"postId" : "P002", "title" : "Fort Renovation", "summary" : "Modernising Capecoast Fort"},
        {"postId" : "P003", "title" : "Lightning Interiors", "summary" : "Utilizing The Power of Lightning"}
    ]},

    {"id" : 2,
    "email" : "mush@yahoo.com",
    "phone" : "0244745064",
    "visits" : 42,
    "posts" : [
        {"postId" : "P001", "title" : "Classy Fashion", "summary" : "Next In Fashion 2022"},
        {"postId" : "P002", "title" : "Universal Bags", "summary" : "All-In-One Totes"},
    ]},

    {"id" : 3,
    "email" : "mushrafat@gmail.com",
    "phone" : "0255791234",
    "visits" : 6,
    "posts" : [
        {"postId" : "P001", "title" : "Greek Style Interior", "summary" : "Greek Interior Trends 2022"},
        {"postId" : "P002", "title" : "Fort Renovation", "summary" : "Modernising Capecoast Fort"},
        {"postId" : "P003", "title" : "Lightning Interiors", "summary" : "Utilizing The Power of Lightning"}
    ]},

    {"id" : 4,
    "email" : "mushrahman@yahoo.com",
    "phone" : "0244792063",
    "visits" : 10,
    "posts" : [
        {"postId" : "P001", "title" : "Greek Style Interior", "summary" : "Greek Interior Trends 2022"},
        {"postId" : "P002", "title" : "Fort Renovation", "summary" : "Modernising Capecoast Fort"},
        {"postId" : "P003", "title" : "Lightning Interiors", "summary" : "Utilizing The Power of Lightning"}
    ]},

    {"id" : 5,
    "email" : "mushrahman@yahoo.com",
    "phone" : "0244792063",
    "visits" : 10,
    "posts" : [
        {"postId" : "P001", "title" : "Greek Style Interior", "summary" : "Greek Interior Trends 2022"},
        {"postId" : "P002", "title" : "Fort Renovation", "summary" : "Modernising Capecoast Fort"},
        {"postId" : "P003", "title" : "Lightning Interiors", "summary" : "Utilizing The Power of Lightning"}
    ]},

    {"id" : 6,
    "email" : "mushrahman@yahoo.com",
    "phone" : "0244792063",
    "visits" : 10,
    "posts" : [
        {"postId" : "P001", "title" : "Greek Style Interior", "summary" : "Greek Interior Trends 2022"},
        {"postId" : "P002", "title" : "Fort Renovation", "summary" : "Modernising Capecoast Fort"},
        {"postId" : "P003", "title" : "Lightning Interiors", "summary" : "Utilizing The Power of Lightning"}
    ]},

    {"id" : 7,
    "email" : "mushrahman@yahoo.com",
    "phone" : "0244792063",
    "visits" : 10,
    "posts" : [
        {"postId" : "P001", "title" : "Greek Style Interior", "summary" : "Greek Interior Trends 2022"},
        {"postId" : "P002", "title" : "Fort Renovation", "summary" : "Modernising Capecoast Fort"},
        {"postId" : "P003", "title" : "Lightning Interiors", "summary" : "Utilizing The Power of Lightning"}
    ]},

    # {"id" : 8,
    # "email" : "mushrahman@yahoo.com",
    # "phone" : "0244792063",
    # "visits" : 10,
    # "posts" : [
    #     {"postId" : "P001", "title" : "Greek Style Interior", "summary" : "Greek Interior Trends 2022"},
    #     {"postId" : "P002", "title" : "Fort Renovation", "summary" : "Modernising Capecoast Fort"},
    #     {"postId" : "P003", "title" : "Lightning Interiors", "summary" : "Utilizing The Power of Lightning"}
    # ]},

    # {"id" : 9,
    # "email" : "mushrahman@yahoo.com",
    # "phone" : "0244792063",
    # "visits" : 10,
    # "posts" : [
    #     {"postId" : "P001", "title" : "Greek Style Interior", "summary" : "Greek Interior Trends 2022"},
    #     {"postId" : "P002", "title" : "Fort Renovation", "summary" : "Modernising Capecoast Fort"},
    #     {"postId" : "P003", "title" : "Lightning Interiors", "summary" : "Utilizing The Power of Lightning"}
    # ]},

    # {"id" : 10,
    # "email" : "mushrahman@yahoo.com",
    # "phone" : "0244792063",
    # "visits" : 10,
    # "posts" : [
    #     {"postId" : "P001", "title" : "Greek Style Interior", "summary" : "Greek Interior Trends 2022"},
    #     {"postId" : "P002", "title" : "Fort Renovation", "summary" : "Modernising Capecoast Fort"},
    #     {"postId" : "P003", "title" : "Lightning Interiors", "summary" : "Utilizing The Power of Lightning"}
    # ]},
    
]

print(user)
print(user[1]["visits"])
print(user[1]["posts"])
print(len(user[1]["posts"]))



