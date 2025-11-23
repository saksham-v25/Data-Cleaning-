# 1>Import the randopm module 
import random

#2 .- create subjects list
subjects = [
    "A grumpy gnome",
    "The legendary phoenix",
    "The last dragon",
    "A powerful sorceress",
    "The forgotten deity",
    "A trio of brave knights",
    "The enchanted sword"
]
# 3.- create verbs list
actions = [
    "awakens",
    "challenges",
    "restores",
    "forges",
    "steals",
    "curses",
    "befriends"
]

# 4.- create objects list
places_or_things = [
    "the kingdom of Eldoria",
    "a vial of liquid starlight",
    "the ancient prophecy",
    "the lost soul of a king",
    "a portal to another realm",
    "the sacred grimoire",
    "a herd of unicorns"
]

while True:
    subjects = random.choice(subjects)
    actions = random.choice(actions)
    places_or_things = random.choice(places_or_things)

    headline = f"BREAKING NEEWS :{subjects} {actions} {places_or_things}"
    print("\n" + headline)
    

    user_input = input("\nDo ypu want to generate another headline? (yes/no): ").strip().lower()
    if user_input != "yes":
        break


print('\nThank you for using the Fake Headline Generator! Have aa fun day ')