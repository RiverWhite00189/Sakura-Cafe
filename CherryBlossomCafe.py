print ("You’re going about a regular day going day to day trudging along trying to figure out what to do today, with your life.")
print("You look up and you’ve never seen this place on campus before. You glance at your watch, you have time. “I'll check it out”")
print("you think to yourself. When you step inside you squint against a bright light and when you open your eyes you’re enveloped in soft pink light.")
print("“Wait, is it already sunset!?” You ask yourself, you're about to turn away when you hear a voice.")

responses = []
personality1 = 0
personality2 = 0


def talkitalkirumba ():
    choice = 0
    print("Welcome, would you like to order?\n")
    print("You have two choices\n")
    print("1: Wait, where am I?")
    print("2: What do you recommend?")
    choice = input("Please choose 1 or 2 by entering the coresponding number ")
    if (choice == "1"):
        print("Wait you're not from around here? I swear I saw you earlier at the apothocary.")
        print("Well you can't leave until you're ready to leave.") 
    else: 
        print ("That depends,")  
    print ("What were you palanning on doing today?")
    print("1: I really didn't know")
    print("2: I had a really good plan!")
    choice = input("Please choose 1 or 2 by entering the coresponding number ")
    if (choice == "1"):
        print("What type of day did you want to have?")
        print("1: A fun day")
        print("2: A productive day")
        choice = input("Please choose 1 or 2 by entering the coresponding number ")
        if (choice == "1"):
            print ("Did you want 1. a going out fun day or a 2. stay at home fun day?")
            choice = input("Please choose 1 or 2 by entering the coresponding number ")
            if (choice == "1"):
                print("Ideas for a fun going out day: Catching a movie, going to the library, going to a park")
            else:
                print("Ideas for a fun stay at home day: read a book, try baking or cooking a new dish, find a new TV show, start a new craft or finish an old one")
            print("We can also add any tasks you have to do today to your list!")
       
            

        else: 
            print(" If you have any small chores like laundry or tidying those could be something to tackle before doing something bigger like a project")
            print(" Think if there are some small tasks you'd want to get done today :)")
            print("Consider adding some fun things to your list too!")

   
    task = ""
    print("What did you want to do?")
    print("please enter your tasks: ")
    print("When you're done adding your tasks, please press 4")
    while(exit == False):
        task = input("please enter a task: ")
        if (task == "4"):
            exit  = True
        else:
            responses.append(task)
            
    global vibes
    vibes = input("What is your main goal / intent / focus for today? ")
    


def results():
    print("Today you'd like to do these things: ")
    for i in responses:
        print(i + "\n")
    print ("and what you want your today to achomplish is: " + vibes)



def coffee_order(person1, person2):
    #sweet or spicy order
    print("\"Let's see then. Do you like your drinks sweet or spicy?\"")
    print("1. Sweet")
    print("    You like to ease into things, prefer staying where you're comfortable,"
    " and like to go with the flow.")
    print("2. Spicy")
    print("    You like to jolt into action, and are fine being a little uncomfortable."
    " Challenges spur you on.")

    #input and iteration
    answer = input()
    if answer == "1":
        person1 += 1
    elif answer == "2":
        person2 += 1
    
    print()

    #sparkles dialouge
    print("I see, now would you like some sparkles in your drink or none?")
    print("\"Huh? What are sparkles?\" You ask.")
    print("The barista replies \"Oh, sparkles just give you a little "
    "extra burst of energy to get through the day. I, personally, can't "
    "get through a shift without a good cup of sparkling sweet rain-mist.\"")
    print("\"Good to know,\" You respond.")

    #sparkles ask and input
    print("1. Sparkles")
    print("    You need that bit of extra energy in motivation in the morning. "
    "You're not the type of person to willingly take 8am classes everyday.")
    print("2. No Sparkles")
    print("    You don't have much trouble getting up and getting started with your day."
    "When you get up, you feel ready to go out and get stuff done.")
    answer = input()
    if answer == "1":
        print("You nod, asking for sparkles, you need a little extra energy today"
        "to get through everything you gotta do.")
        person1 += 1
    elif answer == "2":
        print("You shake your head no. You're alredy wired enough and don't need any "
        "more energy today.")
        person2 += 2

    print()
    print("\"Great!,\" the barista exclaims. \"Would you like any bubbles in that? They give"
    " your drink a bit of extra chew.\"")
    print("1. No Bubbles")
    print("   You feel more comfortable staying where you know you're safe. You'd rather "
    "stick to what you know")
    print("2. With Bubbles")
    print("    You want to explore new things and have an adventure. You aren't scared of "
    "the unknown")

    #answer and interation
    answer = input()
    if answer == "1":
        person1 += 1
        print("\"No bubbles, please,\" you say. The barista nods and smiles at you.")
    if answer == "2":
        person2 += 1
        print("\"Yeah, I'd like some bubbles,\" you say, smiling. You're excited to try this new"
        " fantasy coffee.")

    #fizzles path
    print()
    print("The barista taps away at her screen then looks up at you with a smile. \"And would you "
    "also like some fizz?\"")
    print("You hesitate. You're not sure if fizz is the same in this world or some strange "
    "new flavor.")
    print("The barista takes mercy on you and says with a slight smile \"It just adds a bit "
    "of texture to the drink.")

    print("1. No Fizz")
    print("    You aren't seeking out a new experience, and new expreiences tend to frighten you"
    " a bit")
    print("2. Fizz")
    print("    You're on an adventure! You're excited to try out something new, and want "
    "to seek out more new experiences in the future.")

    #answer and iteration
    answer = input()
    if answer == "1":
        person1 += 1
        print("\"No fizz for me, thanks,\" you say. You've had enough adventure, what with "
        "the teleportation and fantasy world.")
    elif answer == "2":
        person2 += 1
        print("You nod excitedly. This is going to be the best drink ever.")

    print()
    print("\"I can tell you're getting sick of me, but this drink is almost done, don't worry!\""
    "The barista looks up from her screen again.")
    print("\"Would you like some cream of the crop in this? It's super tasty, it'll "
    "definitely raise your spirits!\"")

    print("1. ")
    print("    You feel like you're missing something. You don't know what, but you're "
    "craving something.")
    print("2. ")
    print("    You feel like you have all your cards together. You're collected and "
    "ready to go face the world")

    #answers
    answer = input()
    if answer == "1":
        person1 += 1
        print("\"Yeah, cream of the crop sounds good,\" you respond. Maybe this will be "
        "the thing to fill that missing part of you.")
    elif answer == "2":
        person2 += 1
        print("\"No thanks, I've got all the happiness I need!\" You flash a charming smile at "
        "the barista. She doesn't seem impressed.")

    #root/leaf
    print()
    print("\"Now would you like some root or leaf with that? I hope I don't have to explain "
    "this one, it's exactly what it sounds like.\"")
    print("1. Leaf")
    print("    You feel like you're blowing away in the wind. You don't have anything to "
    "keep you grounded and focused.")
    print("2. Root")
    print("    You're grounded, you're on task, you're ready to get going. You don't need "
    "any more help getting set and moving on.")

    #answer/calculations
    answer = input()
    if answer == "1":
        person1 += 1
        print("\"I'd like leaf with that, please,\" you respond. You're not sure how "
        "well leaf is going to translate into a drink")
    elif answer == "2":
        person2 += 1
        print("\"Could I have that with root?\" You ask with confidence. This is without a doubt,"
        "the best drink you'll ever have in you're life. Or the most interesting at least.")

    print()
    print("\"All right, one more question and then I can get started making this,\" "
    "the barista looks down at her tablet and asks you \"Would you like your drink foggy?\"")
    print("1. Foggy")
    print("    You're not sure about what you want to do. You don't have a clear direction "
    "goal, or don't know how to get there.")
    print("2. No Fog")
    print("    You know what you want and how to get it. All you need is the tools, and then "
    "there's nothing that can stop you.")

    #answers
    answer = input()
    if answer == "1":
        person1 += 1
        print("\"I'd like it foggy please.\"")
    elif answer == "2":
        person2 += 1
        print("\"Not foggy, thank you.\"")

    print("The barista makes one final selection on her tablet, then looks up at you with a "
    "bright smile.")
    print("\"It'll be ready in just a few minutes! Please ahve a seat and feel free to pet "
    "the cat!\"")
    print()
    print("You walk over to a small table in the corner currently occupied by a "
    "medium-sized white cat.")
    #debugging
    person2 -= 1
    #print(person1, person2)





talkitalkirumba()
coffee_order(personality1, personality2)
results()
