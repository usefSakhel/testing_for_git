fruits = ["Cherry", "Figs", "Apple", "Banana", "Blueberry"]
print(fruits)
print(f"First fruit is : {fruits[0]} \nLast fruit is : {fruits[-1]}")
fruits[1] = "Mango"
fruits.insert(2,"Watermelon")
print(fruits)
name = (input("Enter a fruit name to check : "))
print(fruits.count(name)!=0)


fruits.sort()
print(fruits)
