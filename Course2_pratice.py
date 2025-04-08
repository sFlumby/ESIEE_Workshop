pasta = {"type" : "macaroni", "amount" : "500g"}
cheese = {"type" : "cheddar", "amount" : "250g"}

def favorite_dish(pasta : dict = {"type" : "cheddar", "amount" : "750g"}, cheese : dict = {"type" : "cheddar", "amount" : "750g"}) :
    answer = input("Did you boil water ? (Y/N) = ")
    if answer == "Y" :
        print("Nice add the " + str(pasta["amount"]) + " of " + pasta["type"] + " into the boiling water to cook it")
    elif answer == "N" :
        print("Boil water")
    else :
        print("Answer not recognised")
        pass
    answer = input("The pasta are cooked ? (Y/N) = ")
    if answer == "Y":
        print("Nice add the "+ str(cheese["amount"]) + " of " + cheese["type"] + " into your cooked pasta")
    elif answer == "N":
        print("Wait for the pasta to cook")
    else:
        print("Answer not recognised")
        pass
    print("Bon appetit !")

favorite_dish(pasta, cheese) # you choose your parameter
favorite_dish() # choose defaut parameter of your functions