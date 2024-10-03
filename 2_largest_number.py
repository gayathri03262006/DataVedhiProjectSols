#Aim - Write a program to find the largest of three numbers in python/c/java

def largest_num(a, b, c):
    if a == b == c:
        return None
    return max(a, b, c)

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    large = largest_num(num1, num2, num3)
    if large == None:
        print("All are equal")
    else:
        print(f"Largest number of {num1}, {num2}, {num3} is {large}")

if __name__ == "__main__":
    main()
