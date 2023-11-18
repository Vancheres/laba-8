def calculate_expenses(distances, tariffs):
    total_expenses = []
    for i in range(len(distances)):
        expenses_for_employee = []
        for j in range(len(tariffs)):
            expenses_for_employee.append(distances[i] * tariffs[j])
        total_expenses.append(expenses_for_employee)
    return total_expenses

def find_optimal_assignment(total_expenses):
    assignments = []
    for i in range(len(total_expenses[0])):
        total_cost = 0
        assignment = []
        for j in range(len(total_expenses)):
            total_cost += total_expenses[j][i]
            assignment.append(i + 1)
        assignments.append((total_cost, assignment))

    min_cost, optimal_assignment = min(assignments, key=lambda x: x[0])
    return optimal_assignment, min_cost

def number_to_words(number):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    rubles = 'рубль' if number % 10 == 1 and number % 100 != 11 else 'рублей'
    return f'{number} {rubles}'

# Ввод данных
N = int(input())
distances = list(map(int, input().split()))
tariffs = list(map(int, input().split()))

# Расчет общих затрат и оптимального варианта
total_expenses = calculate_expenses(distances, tariffs)
optimal_assignment, min_cost = find_optimal_assignment(total_expenses)

# Вывод результатов
print(*optimal_assignment)
print(min_cost)
print(number_to_words(min_cost))