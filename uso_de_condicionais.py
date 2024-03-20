#uso de condicionais

userreply=input("Do you need to ship a package? (enter yes or no) ")
if userreply == "yes":
      print("we can help you ship that package!")


else:
    print("please come back when you need to ship a package. Thank you!")


    userreply = input("Would you like to buy stamps, buy an envelop, or make a copy? (enter stamps, envelop, or copy")
    if userreply == "stamps":
        print("We have many stamps design to choose from")
    elif userreply == "envelop":
        print("We have many envelop sizes to choose from")
    elif userreply == "copy":
        copies=input("How many copies would you like? (enter a number) ")
        print("Here are {} copies." .format(copies))
    else:
        print("Thank you, please come again")



