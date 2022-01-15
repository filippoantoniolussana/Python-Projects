# Empty dictionary and list used to store items
grocery_item = {}
grocery_history = []

# Variable used to check if the while loop condition is met
stop = 'c'

# While loop used to collect user items 
while stop == 'c':
  item_name = input("Item name:\n")
  quantity = input("Quantity purchased:\n")
  cost = input("Price per item:\n")
  grocery_item = {'name': item_name, 'number': int(quantity), 'price': float(cost)}

  grocery_history.append(grocery_item)
  
  stop = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")
  
  
grand_total = 0

# For loop used to calculate each item total and grand total
for grocery_item in grocery_history:
  item_total = grocery_item['number'] * grocery_item['price']
  grand_total += item_total
  print(str(grocery_item['number']) + " " + grocery_item['name'] + " @ $" + str(grocery_item['price']) + " ea $" + str(item_total))
  
# Display grand total
print("Grand total: " + "$%.2f"% grand_total)
