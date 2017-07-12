tacos = []
# Taco Class
class Taco():
    def __init__(self,customer,meat,topping):
        self.customer = customer
        self.meat = meat
        self.topping = topping

    def finalyzeOrder(self):
        taco = self.meat, "and" ,self.topping
        tacos.append(taco)
        print("Hey",self.customer,"you ordered", tacos,"taco")

    def addTaco(self):
        print("I see you wanted another taco, what would you like?")

# Menu Items
meat = ["pork", "beef","chicken"]
toppings = ["cheese", "lettuce", "beans","carrots"]

addTaco = True

while addTaco == True:
    # Asks customer what their name is
    nameInput = input("What's your name? ")

    # Asks Customer what type of meat they want
    meatInput = input("What type of meat do you want? ")

    # Checks if the customer is asking for meat that is available
    if meatInput not in meat:
        meatInput = input("I'm sorry but we don't have the meat that your looking for, we only have pork, chicken, and beef." )

    # Asks customer what topping
    toppingInput = input("What type of topping would you like?" )

    # Asks customer if they want another taco
    if toppingInput not in toppings:
        toppingInput = input("We only have cheese, salad, carrots, and beans" )

    addTaco = input("Add tacos? Yes or No?" )

    if addTaco == "no":
        print("case1")
        addTaco = False
        tacoOrder = Taco(nameInput, meatInput, toppingInput)
        tacoOrder.finalyzeOrder()

    elif addTaco == "yes":
        print("case2")
        addTaco = True
