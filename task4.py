fruits = {
    "apple":10,
    "banana":6,
    "orange":"15",
    "watermelon":7,
    "manga":20
}
fruit_name = (input("Enter a fruit name to check for the price : "));

if(fruits.get(fruit_name)):
    print(f"{fruit_name}'s price is {fruits[fruit_name]}$")
else :print(f"Sorry, {fruit_name} is not available")