prices = []
bought = []
total= 0
 
print("Enter prices of 6 items:")
for i in range(6):
    price = int(input("Item " + str(i+1) + ": "))
    prices.append(price)

budget = int(input("\nEnter total budget: "))

print()

for i in range(6)
    if total + prices[i] <= budget:
        print(f"Item {i+1} = {prices[i]} -> buy")
        total += prices[i]
        bought.append(prices[i])
    else:
        print(f"Item {i+1} = {price[i]} -> cannot buy")

    print(f"Current total = {total}\n")
    
print(f"Bought item: {bought}")
print(f"Total spent: {total}")
print(f"Remaining budget: {budget - total}")