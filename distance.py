import math
import numpy as np

# Создаем матрицу расстояний между городами
# получает на вход матрицу координат городов
def getDistancesBetweenCities(city_coordinates):
    NumOfCities = len(city_coordinates)
    distances_between_cities = np.zeros((NumOfCities, NumOfCities))
    for i in range(NumOfCities):
        for j in range(i, NumOfCities):
            distance = dist(city_coordinates[i], city_coordinates[j])
            distances_between_cities[i][j] = distance
            distances_between_cities[j][i] = distance
    return distances_between_cities

# подсчет расстояния между двумя точками
def dist(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

# функция которая возвращает общую длину пути
# принимает список индексов городов и матрицу расстояний между городами
def totalDist(path_index, distances_between_cities):
    NumOfCities = len(path_index)
    res = 0
    for i in range(1, NumOfCities):
        res += distances_between_cities[path_index[i]][path_index[i-1]]
    return res
