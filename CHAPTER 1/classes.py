# ============================
# FACTORIAL PROGRAM + CLASSES
# ============================

# 🔹 Factorial calculator
def factorial(n):
    """Function to calculate factorial of a number"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print("=== Factorial Calculator ===")
    num = int(input("Enter a number: "))
    result = factorial(num)
    print(f"Factorial of {num} is: {result}")

# 🔹 Class Example
class Myclass:
    common = 10  # class variable (shared by all instances)

    def __init__(self):
        self.myvariable = 3  # instance variable

    def myfunction(self, arg1, arg2):
        return self.myvariable


# 🔹 Testing Myclass
instance = Myclass()
print("instance.myfunction(1, 2) =>", instance.myfunction(1, 2))

instance2 = Myclass()
print("instance.common =>", instance.common)
print("instance2.common =>", instance2.common)

Myclass.common = 30

print("instance.common =>", instance.common)
print("instance2.common =>", instance2.common)

instance.common = 10
print("instance.common =>", instance.common)
print("instance2.common =>", instance2.common)

Myclass.common = 50
print("instance.common =>", instance.common)
print("instance2.common =>", instance2.common)


# 🔹 Inherited Class Example
class AnotherClass(Myclass):
    def __init__(self, arg1):
        self.myvariable = 3
        print(arg1)


instance = AnotherClass("hello")
print("instance.myfunction(1, 2) =>", instance.myfunction(1, 2))

instance.test = 10
print("instance.test =>", instance.test)


# 🔹 Run main function
if __name__ == "__main__":
    main()
