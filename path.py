import distance
# функция конвертирования ссылочного представления пути в индексное
def refToIndexView(path_ref):
    NumOfCities = len(path_ref)
    indices = list(range(0,NumOfCities)) # индексы еще не добавленных городов
    res = [0] * NumOfCities
    for i in range(NumOfCities):
        index = path_ref[i]
        res[i] = indices[index]
        indices.pop(index)
    return res


# функция получения списка координат по порядковому пути
# принимает порядковое представление пути и список городов
def get_coordinates_from_ordinal_view(ordinal_view, city_coordinates):
     res = []
     for i in range(0, len(ordinal_view)):
         res.append(city_coordinates[ordinal_view[i]])
     return res

#порядковое представление решения
solve_ordinal_view = [0,7,37,30,43,17,6,27,5,36,18,26,16,42,29,35,45,32,19,46,20,31,38,47,4,41,23,9,44,34,3,25,1,28,33,40,15,21,2,22,13,24,12,10,11,14,39,8]

# получить координаты правильного решения
def getSolveCoordinates(city_coordinates):
    return get_coordinates_from_ordinal_view(solve_ordinal_view, city_coordinates)

# получить общее растояние для правильного решения
def getSolveTotalDist(distances_between_cities):
    return distance.totalDist(solve_ordinal_view, distances_between_cities)

def getSolve():
    return solve_ordinal_view