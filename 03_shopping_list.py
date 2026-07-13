# ==============================================================================================================
# Project: Shopping List
# Day: 9
# Author: Pleng
# Language: Python
# Description: A shopping list application using list, while loop, if-elif-else, append(), remove(), and len().
# ==============================================================================================================

print("===== Shopping List =====")
print()
shopping_list = []
choose = 0

while choose != 4:
  print("1. Add item")
  print("2. Remove item")
  print("3. Show items")
  print("4. Exit")
  print()
  choose = int(input("Choose: "))

  if choose == 1:
    item = input("Add: ")
    shopping_list.append(item)
  elif choose == 2:
    if len(shopping_list) == 0:
      print("We don't have anything yet :(")
    else:
      item = input("Remove: ")
      if item not in shopping_list:
        print("It is not in your list!")
      else:
        shopping_list.remove(item)
  elif choose == 3:
    if len(shopping_list) == 0:
      print("Shopping list is empty")
    else:
      print("Shopping List: ", shopping_list)
  elif choose > 4 or choose <1:
    print("Please enter your correct choose!")
  else:
    print("Have a nice day!")
  print()
