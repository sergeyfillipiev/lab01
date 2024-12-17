def gcd(a, b):
    """Алгоритм Евклида для нахождения НОД."""
    while b:
        a, b = b, a % b
    return a

def main():
    print("Алгоритм Евклида для нахождения НОД двух чисел")
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    result = gcd(x, y)
    print(f"НОД чисел {x} и {y} равен {result}")

if __name__ == "__main__":
    main()
