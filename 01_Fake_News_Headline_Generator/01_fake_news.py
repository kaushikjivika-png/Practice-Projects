# import the random module

import random

# create subjects

subjects = [
    "Shahrukh khan",
    "Virat Kohlo",
    "Nirmala Sitaraman",
    "A Mumbai Cat",
    "A group of monkeys",
    "Prime Minister Modi",
    "Auto Rikshaw Driver from Delhi"
]

actions = [
    "Launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at red fort",
    "in mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at ganga ghat",
    "during IPL match"
]

# start the headline generation loop

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS : {subject} {action} {place_or_thing} "
    print("\n" + headline)

    user_choice = input("\n Do you want another headline? (yes/no)").strip().lower()
    if user_choice == "no":
        break

# print goodbye message

print("\nThanks for using the fake news Headline generator. Have a fun day")


