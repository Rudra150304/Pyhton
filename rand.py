import random

def rand(x):
    return random.randint(0,20) == x
    
def main():
    a = int(input("Enter a number between 0 to 20: "))
    if rand(a) == True:
        print("Aapko milte hai 7 crore!!")
    else:
        print("Aap mujhe denge 7 crore!!")

if __name__ == '__main__':
    main()