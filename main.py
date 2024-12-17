import numpy as np
import matplotlib.pyplot as plt

def fibonacci_sequence(n):
    """Вычисление первых N чисел Фибоначчи."""
    fib = np.zeros(n, dtype=int)  # Инициализация массива из N элементов
    fib[0] = 0
    if n > 1:
        fib[1] = 1
        for i in range(2, n):
            fib[i] = fib[i-1] + fib[i-2]
    return fib

def plot_fibonacci(fib_numbers):
    """Построение графика чисел Фибоначчи."""
    x = np.arange(1, len(fib_numbers) + 1)  # Номера чисел Фибоначчи
    y = fib_numbers  # Значения чисел Фибоначчи

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='b', label="Fibonacci Numbers")
    plt.title("Числа Фибоначчи")
    plt.xlabel("Номер числа Фибоначчи")
    plt.ylabel("Величина числа Фибоначчи")
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    N = int(input("Введите количество чисел Фибоначчи: "))
    fib_numbers = fibonacci_sequence(N)
    print(f"Первые {N} чисел Фибоначчи: {fib_numbers}")
    plot_fibonacci(fib_numbers)

if __name__ == "__main__":
    main()
