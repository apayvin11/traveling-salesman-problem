import distance
import path

# функция для иценки приспособленности особей
# принимает популяцию и матрицу расстояний между городами
# возвращает список с приспособленностью каждой особи
def evaluation(P, distances_between_cities):
    p_size = len(P)  # размер популяции
    res = [0]*p_size
    for i in range(p_size):
        res[i] = distance.totalDist(path.refToIndexView(P[i]), distances_between_cities)
    return res
