# Traveling-salesman-problem

The travelling salesman problem, also known as the travelling salesperson problem (TSP), asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?  

## Task

Implement a solution to the traveling salesman problem using genetic algorithm, compare the found solution with the optimal one presented in the problem conditions.  

|    | City coordinates | Optimal solution |
| -- | ---------------- | ---------------- |
| 1  | 6734 1453        | 1                |
| 2  | 2233 10          | 8                |
| 3  | 5530 1424        | 38               |
| 4  | 401 841          | 31               |
| 5  | 3082 1644        | 44               |
| 6  | 7608 4458        | 18               |
| 7  | 7573 3716        | 7                |
| 8  | 7265 1268        | 28               |
| 9  | 6898 1885        | 6                |
| 10 | 1112 2049        | 37               |
| 11 | 5468 2606        | 19               |
| 12 | 5989 2873        | 27               |
| 13 | 4706 2674        | 17               |
| 14 | 4612 2035        | 43               |
| 15 | 6347 2683        | 30               |
| 16 | 6107 669         | 36               |
| 17 | 7611 5184        | 46               |
| 18 | 7462 3590        | 33               |
| 19 | 7732 4723        | 20               |
| 20 | 5900 3561        | 47               |
| 21 | 4483 3369        | 21               |
| 22 | 6101 1110        | 32               |
| 23 | 5199 2182        | 39               |
| 24 | 1633 2809        | 48               |
| 25 | 4307 2322        | 5                |
| 26 | 675 1006         | 42               |
| 27 | 7555 4819        | 24               |
| 28 | 7541 3981        | 10               |
| 29 | 3177 756         | 45               |
| 30 | 7352 4506        | 35               |
| 31 | 7545 2801        | 4                |
| 32 | 3245 3305        | 26               |
| 33 | 6426 3173        | 2                |
| 34 | 4608 1198        | 29               |
| 35 | 23 2216          | 34               |
| 36 | 7248 3779        | 41               |
| 37 | 7762 4595        | 16               |
| 38 | 7392 2244        | 22               |
| 39 | 3484 2829        | 3                |
| 40 | 6271 2135        | 23               |
| 41 | 4985 140         | 14               |
| 42 | 1916 1569        | 25               |
| 43 | 7280 4899        | 13               |
| 44 | 7509 3239        | 11               |
| 45 | 10 2676          | 12               |
| 46 | 6807 2993        | 15               |
| 47 | 5185 3258        | 40               |
| 48 | 3023 1942        | 9                |

Optimal solution:

```txt
# genetic algorithm constants
POPULATION_SIZE = 50        # Population size
P_CROSSOVER = 0.5           # Crossover probability
P_MUTATION = 0.2            # Probability of mutation
MAX_GENERATIONS = 100000    # Number of generations
NumOfCities = 48            # in our case equal to the size of the chromosome
```

![running](resources/running.png)  
