from functools import partial
from problems import knapsack
from algorithms import genetic

import time

weight_limit = 3000

for i in range(2, 85):
    things = knapsack.generate_things(i)
    target_value = sum([x for x in range(i + 1)])
    fitness = partial(knapsack.fitness, things=things, weight_limit=weight_limit)

    start = time.time()
    population, generations = genetic.run_evolution(
        populate_func=partial(genetic.generate_population, size=10, genome_length=len(things)),
        fitness_func=fitness,
        fitness_limit=sum([x for x in range(i + 1)]),
        generation_limit=10000,
        # printer=print
    )
    end = time.time()
    # sack = knapsack.from_genome(population[0], things)
    # knapsack.print_stats(sack)
    print(
        f"{i}\t|\t{generations}\t|\t{(end - start):e}s\t|\t{(fitness(population[0]) / target_value * 100):.2f}%\t|\t{genetic.genome_to_string(population[0])}")
