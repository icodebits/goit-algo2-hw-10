import time
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Виконання QuickSort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

# Test Data Sizes
sizes = [10000, 50000, 100000, 500000]
results = []

for size in sizes:
    test_array = np.random.randint(0, 1000000, size).tolist()
    
    # Час Рандомізованого QuickSort
    random_times = []
    for _ in range(5):
        arr_copy = test_array[:]
        start_time = time.time()
        randomized_quick_sort(arr_copy)
        random_times.append(time.time() - start_time)
    avg_random_time = np.mean(random_times)
    
    # Час Детермінованого QuickSort
    deterministic_times = []
    for _ in range(5):
        arr_copy = test_array[:]
        start_time = time.time()
        deterministic_quick_sort(arr_copy)
        deterministic_times.append(time.time() - start_time)
    avg_deterministic_time = np.mean(deterministic_times)
    
    results.append([size, avg_random_time, avg_deterministic_time])

# Результати в DataFrame
df = pd.DataFrame(results, columns=["Розмір масиву", "Рандомізований QuickSort (s)", "Детермінований QuickSort (s)"])

# Таблиця
print(df.to_string())

# Графік
plt.figure(figsize=(8, 6))
plt.plot(df["Розмір масиву"], df["Рандомізований QuickSort (s)"], label="Рандомізований QuickSort", linewidth=2)
plt.plot(df["Розмір масиву"], df["Детермінований QuickSort (s)"], label="Детермінований QuickSort", linewidth=2)

# Настроїки графіка
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння рандомізованого та детермінованого QuickSort")
plt.legend()
plt.grid(True)

# Відображення графіка
plt.show()
