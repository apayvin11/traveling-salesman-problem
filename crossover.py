import random

# принимает популяцию и вероятность скрещивания
# возвращает список новых особей
def crossover(P, prob):
    p_size = len(P) # размер популяции
    len_ind = len(P[0])
    res = []
    for individ in P:
        # выбираем родителей
        parent_1_index = random.randint(0, p_size - 1)
        parent_2_index = random.randint(0, p_size - 1)
        while parent_1_index == parent_2_index:
            parent_2_index = random.randint(0, p_size - 1)
        parent_1 = P[parent_1_index].copy()
        parent_2 = P[parent_2_index].copy()

        # отобрали два родителя, теперь решим, будут ли они скрещиваться
        if random.random() > prob:
            continue

        cut_point = random.randint(1, len_ind - 2) # random cutting point
        B1 = parent_1[cut_point:]
        parent_1[cut_point:] = parent_2[cut_point:]
        parent_2[cut_point:] = B1
        res.append(parent_1)
        res.append(parent_2)
    return res