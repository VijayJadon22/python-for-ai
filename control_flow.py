temperature=25

if temperature>25:
    print("Its hot!")
elif temperature==25:
    print("Its Okay Okay!")
else:
    print("Its pleasant weather")



#next example
score=86

if score>=95:
    print("Excellent!")
elif score>=90:
    print("Very Good!")
elif score>=80:
    print("Good")
elif (score>=70):
    print("Satisfactory!")
else:
    print("Work hard!")

#combine and or not with if elif else

age=12
has_license=True

if age>=18 and has_license:
    print("You Can Drive!")
else:
    print("You can not drive")


has_ticket=False
age=15

if has_ticket:
    if age>=18:
        print("Enjoy the movie!")
    else:
        print("Needs supervision!")
else:
        print("Please buy a ticket!")
        

