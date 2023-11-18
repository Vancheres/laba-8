def assign_taxi(n, distances, rates):
    # Сортировка списка расстояний по убыванию и сохранение исходных индексов
    sorted_distances = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)

    # Сортировка списка тарифов по возрастанию и сохранение исходных индексов
    sorted_rates = sorted(enumerate(rates), key=lambda x: x[1])
