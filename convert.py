def convert(C):
    F = 32 + (9*C)/5
    return F

def main():
    c = int(input("Enter temperature in Celsius: "))
    f = convert(c)
    print(f"{f} is the value in Farenhite")

if __name__ == '__main__':
    main()