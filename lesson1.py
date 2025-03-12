# ------------------------------------------LESSON #01 { CONTROL-FLOW & LOOPS } --------------------------------------------------------------

#** CONTROL-FLOW & LOOPS **

#** TYPES OF CONTROL-FLOW IN PYTHON **

# 1.IF STATEMENT
x = 15
if x > 6:
    print("x is greater than 6")

# 2. IF-ELSE STATEMENT

x = 10
if x > 6:
    print("x is greater than 6")
else:
    print("x is not greater than 6")

# 3. IF-ELIF-ELSE STATEMENT

x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is less than or equal to 5")

# 4.NESTED IF STATEMENT
num = 10
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is negative.")

# ------------------------------------------------------------------------------------------------------!!!

# LOOPS AND IT'S TYPE IN PYTHON

# 1. FOR LOOP
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
for i in range(5):  
    print(i)

 # 2. WHILE LOOP
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  

# 3.CONTROLLING LOOP

# *.BREAK STATEMENT

for i in range(10):
    if i == 5:
        break  # 
    print(i)

# *.CONTINUE STATEMENT

for i in range(5):
    if i == 3:
        continue 
    print(i)

# *.ELSE STATEMENT

for i in range(3):
    print(i)
else:
    print("Loop finished without a break")


# -------------------------------------------LESSON #01 [ END ]-----------------------------------------------------------

