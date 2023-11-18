def assign_taxi(n, distances, rates):
    # Сортировка списка расстояний по убыванию и сохранение исходных индексов
    sorted_distances = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)

    # Сортировка списка тарифов по возрастанию и сохранение исходных индексов
    sorted_rates = sorted(enumerate(rates), key=lambda x: x[1])
    assignment = [0] * n
    for i, (distance_idx, _) in enumerate(sorted_distances):
        assignment[distance_idx] = sorted_rates[i][0] + 1  # +1 для корректного отображения номера такси

    # Расчет общей стоимости
    total_cost = sum(distances[i] * rates[assignment[i] - 1] for i in range(n))

    return assignment, total_cost

n = int(input("Введите количество сотрудников: "))
distances = list(map(int, input("Введите расстояния до домов сотрудников через пробел: ").split()))
rates = list(map(int, input("Введите тарифы такси за километр через пробел: ").split()))

assignment, total_cost = assign_taxi(n, distances, rates)
print("Номера такси для каждого сотрудника:", ' '.join(map(str, assignment)))
print("Общая стоимость поездок:", total_cost)
