items = []
prices = []
print("\n***** welcome to ishop calculator *****\n")
number_of_items = int(input("How many items are there in your basket today...?"))

if number_of_items > 0:
     print("\nlet' get to counting them....")
     for i in range(0, number_of_items):
        name = input(f"please tell me the name of the item number {i+1}")
        items.append(name)
        price = float (input("what is the price of {name}\n$"))
        prices.append(price)
     choice = input("would you like to see your entire basket items? ")
     if choice=="yes":
        print(items)
        see_price = input("would you like to see how much it'll cost: ")
        if see_price=="yes":
            print("\nBuying these items will cost")
            print(sum(prices))
        else:
            input("press enter to exit")
     else:
        
        input("press enter to exit")
else:
    print("Sees like you are not in the mood for shooping today")