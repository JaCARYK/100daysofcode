print("The score is 73 to 72. You're losing by 1 point. There are 10 seconds left on the clock.")
print("You need to score the winning point!")

choice_one = input("Do you pass the ball or dribble it?\n  \t Type 'pass' or 'dribble'")

if choice_one == "pass":
    print("the ball got stolen! try again")

elif choice_one == "dribble":
   print("you blow by your defender")


   choice_two = input("do you choose to stop dribbling or shoot?\n  \t Type 'stop' or 'shoot' ")

   if choice_two == "shoot":
       print("you shot the ball from too far away and missed! try again")

   elif choice_two == "stop":
        
        choice_three = input("You are now surrounded! Do you shoot a tough shot or try to find someone to pass too\n  \t Type 'shoot' or 'pass' ")

        if choice_three == "pass":
            print("the ball got stolen! better luck next time")
            
        elif choice_three == "shoot":
            print("The ball goes up and...You made the shot! Great job, you won!")
       
        else:
            print("not a valid option, try again")



   else:
        print("not a valid option try again")
    
else:
    print("not a valid option, try again")
       
