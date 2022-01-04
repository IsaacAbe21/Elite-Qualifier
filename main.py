#This code is taken from a previous project of mine and was continued
import random

fname = input("What is your first name?")
lname = input("What is your last name?")

print("Hi there, " + fname + " " + lname + ". Nice to meet you!")

feeling = input("How are you?")
randresp1 = random.randint(1,2)
randresp2 = random.randint(1,2)

if feeling == "happy" or feeling == "Happy" or feeling == "Delighted" or feeling == "Great" or feeling == "Good":
    if randresp1 == 1:
        print("That's great!")
    elif randresp1 == 2:
        print("Wonderful!")
elif feeling == "sad" or feeling == "down" or feeling == "depressed":
    if randresp2 == 1:
        print("I'm sorry to hear that! \n Keep your head up, it will get a little better soon enough!")
    elif randresp2 == 2:
        print("That's terrible!")
        wrong = input("What's wrong?")
        if wrong == "Nothing" or wrong == "I don't want to talk about it" or wrong == "It's okay":
            print("Alright, let's move on.")
        else:
            print("We don't have to continue if you don't want to. \n If you do, continue onto the age portion. \n Otherwise, you can leave.")
else:
    print("Alrighty. Let's continue.")
        
age = int(input("What is your age?"))
response3 = random.randint(1, 2)

if age <= 15:
    if response3 == 1:
        print("You are so young! What are your interests?")
    elif response3 == 2:
        print("That's great that you are still young!")
        
elif age >= 15 and age < 18:
    print("You are almost an adult! That's crazy!")
elif age >= 18 and age < 55:
    print("I hope your adult life is good so far!")
elif age >= 55:
    print("Wow! You are in your older years but I'm glad you are familiar with technology and have come to talk with us!")
else:
    print("You can't be that old. Try again.")
    age2 = int(input("What is your age?"))
    
sport = input("Do you like sports?")
if sport == "yes" or sport == "Yes" or sport == "Yes." or sport == "yes.":
    favorite_sport = input("Which sport is your favorite?")
    if favorite_sport == "basketball":
        print("Cool! I heard that Lebron is a nice player.")
    elif favorite_sport == "soccer":
        print("Cool! I heard that Messi is a nice player.")
    elif favorite_sport == "track" or favorite_sport == "cross country" or favorite_sport == "tennis" or favorite_sport == "hockey" or favorite_sport == "swimming":
        print("Really? That must take a lot of endurance!")
    elif favorite_sport == "gaming":
        print("Whoah! I'm a gamer too! That's so cool that we have something in common!")
elif sport == "no" or sport == "No" or sport =="No.":
    print("That's okay. We all have our own interests.")
elif sport == "sorta" or sport == "sort of" or sport == "sortof":
    sortof_favoritesport = input("That's alright. What kind of sport are you sort of into?")
    if sortof_favoritesport == "basketball":
        favorite_bball_player = input("Nice! Which player is your favorite?")
        if favorite_bball_player == "Jordan" or favorite_bball_player == "MJ" or favorite_bball_player == "Michael Jordon":
            print("I heard he's goated at basketball, that's pretty cool.")
else:
    print("Not to worry. This is not a required section. Let's move on.")

day = input("What day of the week is it today?")
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("Weekday, huh. Lets hope the weekend roles around quickly. \nWe're done here. Take care.")
elif day == "Saturday" or day == "Sunday":
    print("Nice! Go and enjoy the weekend, we are done here.")