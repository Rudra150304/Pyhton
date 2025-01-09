sentence = input("Enter a sentence: ")
digits = 0
lower = 0
upper = 0

for var in sentence:
    if var.isdigit():
        digits+=1
    elif var.islower():
        lower+=1
    elif var.isupper():
        upper += 1


print("Number of digits = ", digits)
print("Number of lowercase = ", lower)
print("Number of uppercase = ", upper)