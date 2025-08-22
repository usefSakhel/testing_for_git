name = (input("Enter your name : "))
password = (input("Enter your password : "))
low_name = name.lower();
fixed_name = low_name.replace(" ", "_")
pass_len = len(password)


x = "1234"
adm = "admin"
print(f"Password length >= 8: {pass_len >= 8}")
print(f"Username is 'admin': {fixed_name==adm}")
print(f"Password is '1234':  {password == x}")
print(f"Default account (admin & 1234): {fixed_name==adm and password==x}")

print(f"Hello {fixed_name}, your password length is {pass_len}")

