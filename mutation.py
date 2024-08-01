import random

# функция мутации
# принимает популяцию и вероятность мутации
def mutation(P, prob):
    p_size = len(P)  # размер популяции
    len_ind = len(P[0])
    res = P.copy()
    for i in range(p_size):
        if random.random() > prob:
            continue
        # мутируем
        # копируем индивида
        swap_index = random.randint(1, len_ind - 1)
        res[i][swap_index] = random.randint(0, len_ind - swap_index - 1)
    return res