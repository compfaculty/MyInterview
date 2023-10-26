from collections import namedtuple
from functools import partial
from random import choices, randint, randrange, random
from typing import List, Optional, Callable, Tuple, TypeAlias
import numpy as np
from numpy import ndarray
from numpy.typing import NDArray

Genome = NDArray
Population = NDArray
PopulateFunc = Callable[[], Population]
FitnessFunc = Callable[[Genome], int]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]
PrinterFunc = Callable[[Population, int, FitnessFunc], None]

GenLen = 4
Thing = namedtuple('Thing', ['name', 'value', 'weight'])


def generate_population(size: int, genome_len: int) -> Population:
    return np.random.randint(2, size=(size, genome_len))

def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("Genomes a and b must be of same length")

    length = len(a)
    if length < 2:
        return a, b

    p = randint(1, length - 1)
    return a[0:p] + b[p:], b[0:p] + a[p:]


def mutation(population: Population, num: int = 1, probability: float = 0.99):
    for row in population:
        for _ in range(num):
            index = randrange(GenLen)
            row[index] = row[index] if np.random.random() > probability else abs(row[index] - 1)
    return population


def population_fitness(population: Population, fitness_func: FitnessFunc) -> int:
    return np.apply_along_axis(fitness_func, 1, population).sum()


def fitness(genome: NDArray, things: [Thing], weight_limit: int) -> int:
    if len(genome) != len(things):
        raise ValueError("genome and things must be of same length")

    weight = 0
    value = 0
    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value

            if weight > weight_limit:
                return 0

    return value


def selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
    # pair = choices(
    #     population=population,
    #     weights=[fitness_func(gene) for gene in population],
    #     k=2
    # )
    pair  = np.apply_along_axis(fitness_func, 1, population).argmax()
    print(pair)
    # return pair
    # return pair


def sort_population(population: Population, fitness_func: FitnessFunc) -> Population:
    return sorted(population, key=fitness_func, reverse=True)


def genome_to_string(genome: Genome) -> str:
    return "".join(map(str, genome))


def print_stats(population: Population, generation_id: int, fitness_func: FitnessFunc):
    print("GENERATION %02d" % generation_id)
    print("=============")
    print("Population: [%s]" % ", ".join([genome_to_string(gene) for gene in population]))
    print("Avg. Fitness: %f" % (population_fitness(population, fitness_func) / len(population)))
    sorted_population = sort_population(population, fitness_func)
    print(
        "Best: %s (%f)" % (genome_to_string(sorted_population[0]), fitness_func(sorted_population[0])))
    print("Worst: %s (%f)" % (genome_to_string(sorted_population[-1]),
                              fitness_func(sorted_population[-1])))
    print("")

    return sorted_population[0]


def run_evolution(
        populate_func: PopulateFunc,
        fitness_func: FitnessFunc,
        fitness_limit: int,
        selection_func: SelectionFunc = selection_pair,
        crossover_func: CrossoverFunc = single_point_crossover,
        mutation_func: MutationFunc = mutation,
        generation_limit: int = 100,
        printer: Optional[PrinterFunc] = None) \
        -> Tuple[Population, int]:
    population = populate_func()

    for i in range(generation_limit):
        population = sorted(population, key=lambda genome: fitness_func(genome), reverse=True)

        if printer is not None:
            printer(population, i, fitness_func)

        if fitness_func(population[0]) >= fitness_limit:
            break

        next_generation = population[0:2]

        for j in range(int(len(population) / 2) - 1):
            parents = selection_func(population, fitness_func)
            offspring_a, offspring_b = crossover_func(parents[0], parents[1])
            offspring_a = mutation_func(offspring_a)
            offspring_b = mutation_func(offspring_b)
            next_generation += [offspring_a, offspring_b]

        population = next_generation

    return population, i

first_example = [
    Thing('Laptop', 500, 1000),
    Thing('Headphones', 150, 200),
    Thing('Coffee Mug', 60, 300),
    Thing('Notepad', 40, 400),
    # Thing('Water Bottle', 30, 192),
]
matrix1 = np.random.randint(2, size=(4, 4))
print(matrix1)
p = mutation(population=matrix1)

print(p)
fit = partial(fitness, weight_limit=1500, things=first_example)
r = population_fitness(p, fitness_func=fit)
selection_pair(p, fitness_func=fit)
print(r)