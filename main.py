import random
import time

import crossover
import distance
import population
import path
import mutation
import evaluation
import selection
from datetime import datetime

import matplotlib.pyplot as plt

# genetic algorithm constants
POPULATION_SIZE = 50        # Population size
P_CROSSOVER = 0.5           # Crossover probability
P_MUTATION = 0.2            # Probability of mutation
MAX_GENERATIONS = 100000    # Number of generations
NumOfCities = 48            # in our case equal to the size of the chromosome

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

city_coordinates = [
    [6734, 1453],
    [2233, 10],
    [5530, 1424],
    [401, 841],
    [3082, 1644],
    [7608, 4458],
    [7573, 3716],
    [7265, 1268],
    [6898, 1885],
    [1112, 2049],
    [5468, 2606],
    [5989, 2873],
    [4706, 2674],
    [4612, 2035],
    [6347, 2683],
    [6107, 669],
    [7611, 5184],
    [7462, 3590],
    [7732, 4723],
    [5900, 3561],
    [4483, 3369],
    [6101, 1110],
    [5199, 2182],
    [1633, 2809],
    [4307, 2322],
    [675, 1006],
    [7555, 4819],
    [7541, 3981],
    [3177, 756],
    [7352, 4506],
    [7545, 2801],
    [3245, 3305],
    [6426, 3173],
    [4608, 1198],
    [23, 2216],
    [7248, 3779],
    [7762, 4595],
    [7392, 2244],
    [3484, 2829],
    [6271, 2135],
    [4985, 140],
    [1916, 1569],
    [7280, 4899],
    [7509, 3239],
    [10, 2676],
    [6807, 2993],
    [5185, 3258],
    [3023, 1942],
]

# Создаем матрицу расстояний между городами
distances_between_cities = distance.getDistancesBetweenCities(city_coordinates)

# создаем популяцию
P = population.newPopulation(POPULATION_SIZE, NumOfCities)

Stat = []

plt.ion() # включаем интерактивный режим
# создаем график
plt.figure(figsize=(10, 6)) # устанавливаем размер графика
# распаковываем координаты городов (для графика)
x_cities, y_cities = zip(*city_coordinates)
# получаем координаты правильного решения (для графика)
x_right_solve, y_right_solve = zip(*path.getSolveCoordinates(city_coordinates))
# получаем общее расстояние правильного решения
totalDistanceRightSolve = path.getSolveTotalDist(distances_between_cities)
best_solve = 0
plot_period = MAX_GENERATIONS // 1000 # количество поколений как период рисо-вания графика
start = time.time() # точка отсчета времени
print('Start time: ', datetime.now().strftime("%H:%M:%S"))
# запускаем генетический алгоритм
for i in range(MAX_GENERATIONS):
    # получаем скрещенных индивидуумов
    individuals = crossover.crossover(P, P_CROSSOVER)
    # запускаем мутацию
    individuals = mutation.mutation(individuals,P_MUTATION)
    # добавляем новых индивидуумов в конец популяции
    P = [*P, *individuals]
    # считаем приспособленность
    fitness = evaluation.evaluation(P, distances_between_cities)
    # запускаем отбор
    P, fitness = selection.selection(P, fitness, POPULATION_SIZE)
    # считаем среднюю приспособленность
    avg_fitness = sum(fitness) / POPULATION_SIZE;
    best_fitness = fitness[0] # лучшая приспособленность
    Stat.append([avg_fitness, best_fitness])

    # отображаем на графике
    if i%plot_period == 0:
        plt.clf()
        plt.subplot(2, 1, 1)
        plt.scatter(x_cities, y_cities, marker='o', color='red', s=50,
                    label='Города')  # отображаем точки городов на графике
        plt.plot(x_right_solve, y_right_solve, color='green', linewidth=4,
                 label='Правильный путь')  # рисуем правильное решение
        # получаем координаты  решения генетического алгоритма и отображаем на графике
        # лучшее решение находится в P[0] так как сначала отбираем элит
        x_ga, y_ga = zip(*path.get_coordinates_from_ordinal_view(path.refToIndexView(P[0]), city_coordinates))
        plt.plot(x_ga, y_ga, color='blue', linewidth=2, label='Путь генетического алгоритма')
        plt.title('Графическое представление пути между городами')
        plt.xlabel('X координата города')
        plt.ylabel('Y координата города')
        plt.legend(loc=2)  # местоположение легенды
        plt.grid()

        # на втором графике отображаем статистику - средняя / лучшая приспо-собленность и правильное решение
        plt.subplot(2, 1, 2)
        meanFitnessValues, minFitnessValues = zip(*Stat)
        plt.plot(meanFitnessValues, color='blue', label='Средняя приспособленность')
        plt.plot(minFitnessValues, color='red', label='Экстремумы')
        plt.plot([0, len(Stat) - 1], [totalDistanceRightSolve, totalDistanceRightSolve], color='green',
                 label='Правильное решение')
        plt.xlabel('Поколение')
        plt.ylabel('Экстремум/средняя приспособленность')
        plt.title('Зависимость лучшего решения и средней приспособленности от поколения')
        plt.legend(loc=9)  # местоположение легенды
        plt.tight_layout()  # устанавливаем диапазон между графиками
        plt.grid()

        plt.draw()
        plt.gcf().canvas.flush_events()
    if best_solve != 0:
        if best_solve > best_fitness:
            best_solve = best_fitness
            print("New solve! fitness: ", best_solve, " num gen: ", i, " time : ", time.time() - start)
    else:
        best_solve = best_fitness

plt.ioff() # выключаем интерактивный режим

# подводим итоги
print("Общее время выполнения программы: ",  round(time.time() - start), " s")
min_fitness_ga = fitness[0]  # оно первое, так как сначала отбирали элит
Best_solve_ga = P[0]  # Best chromosome
print('Путь генетического алгоритма: ', Best_solve_ga)
print('Наименьшее расстояние генетического алгоритма: ', min_fitness_ga)
print('Правильное решение: ', path.getSolve())
print('Общее расстояние правильного решения: ', totalDistanceRightSolve)
plt.show()
