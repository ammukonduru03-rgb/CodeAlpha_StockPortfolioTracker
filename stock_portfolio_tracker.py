stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "MSFT": 200
}

total = 0

while True:

    stock_name = input("Enter Stock Name: ").upper()
    
    if stock_name in stock_prices:
       quantity = int(input("Enter Quantity: "))

       price = stock_prices[stock_name]

       investment = price * quantity

       total = total + investment
       choice = input("Do you want to add another stock? (yes/no): ").lower()

       if choice == "no":
           break

    else:
          print("Invalid Stock Name! Please enter AAPL, TSLA, GOOGLE or MSFT.")
print("Total Investment is :", total)

#file handling starts here

file = open("investment.txt", "w")

file.write("Stock Portfolio Summary\n")
file.write("-----------------------\n")
file.write("Total Investment : ₹" + str(total))

file.close()
