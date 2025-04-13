# main.py

# ✅ 1. Variables and Data Types
name = "Md. Tanvir Ahmed"
age = 19
is_student = True

print("✅ Variable Types:")
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of is_student:", type(is_student))

# ✅ 2. Arithmetic Operations
print("\n✅ Arithmetic Operations:")
print("Age + 5 =", age + 5)
print("Age - 2 =", age - 2)
print("Age * 2 =", age * 2)
print("Age / 2 =", age / 2)

# ✅ 3. Comparison Operators
print("\n✅ Comparison Operators:")
print("Is age > 18:", age > 18)
print("Is age == 20:", age == 20)
print("Is age != 25:", age != 25)
print("Is age < 30:", age < 30)

# ✅ 4. Logical Operators
print("\n✅ Logical Operators:")
condition1 = age > 18
condition2 = is_student

print("condition1 and condition2:", condition1 and condition2)
print("condition1 or condition2:", condition1 or condition2)
print("not condition1:", not condition1)

# ✅ 5. Assignment Operators
print("\n✅ Assignment Operators:")
x = 10
print("Initial value of x:", x)
x += 5
print("After += 5:", x)
x -= 2
print("After -= 2:", x)
x *= 3
print("After *= 3:", x)
x /= 4
print("After /= 4:", x)

# ✅ 6. Identity Operators
print("\n✅ Identity Operators:")
a = 100
b = 100
c = 200

print("a is b:", a is b)
print("a is not c:", a is not c)

# ✅ 7. Membership Operators
print("\n✅ Membership Operators:")
my_list = [10, 20, 30, 40, 50]

print("Is 20 in my_list?", 20 in my_list)
print("Is 99 not in my_list?", 99 not in my_list)

