responses = []

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

    exit = False
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

    
talkitalkirumba()
results()
   
