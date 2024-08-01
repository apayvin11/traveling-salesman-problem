import numpy as np
import random

# создаем популяцию и инициализируем случайными значениями
# с представлением тура в виде ссылок
def newPopulation(POPULATION_SIZE, NumOfCities):
    population = np.zeros((POPULATION_SIZE, NumOfCities), dtype=int)
    for individ in population:
        for i in range(NumOfCities):
            individ[i] = random.randint(0, NumOfCities - i - 1)
    return population