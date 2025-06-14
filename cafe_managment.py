def resturant_managment():
    print("_____WELCOME TO PYTHON RESTURENT_____")
    print('''Pizza 1500\nCoffee 80\nZinger Burger 320\nHot Wings 600\nCake 450''')
    Total_products = {"Pizza": 1500,
                      "Coffee": 80, 
                      "Zinger Burger": 320,
                      "Hot Wings": 600,
                      "Cake": 450}
    
    # list_of_products = ["Pizza", "Coffee", "Zinger Burger", "Hot Wings", "Cake"]
    total_order = 0
    
    item_1 = input("What you Want to order? \n")
    if item_1 in Total_products:
        print(f"You order ({item_1})  is added.")
        total_order += Total_products[item_1]
    else:
        print(f"Your order of ({item_1}) is not avaliable!")
    # print(total_order)
    
    while True:
        item_2 = input("You want to order something more else type (NO).\n")
        # print("_____________________________________________")
        
        if item_2 == "NO" or item_2 == "No" or item_2 == "no":
            print("Thanks for using it!")
            break
        else:
            total_order +=   Total_products[item_2]
            
            
    print(f"Your Total Bill is ----- RS: {total_order}")  
      
resturant_managment()
