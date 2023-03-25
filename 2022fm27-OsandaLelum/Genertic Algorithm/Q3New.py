import random
# Parameters of the GA
POPULATION_SIZE = 50
NUM_GENERATIONS = 100
MUTATION_RATE = 0.1
ELITISM = True
MAX_DISTANCE = 800

# Distance matrix for the given cities
distances =[ [0 ,115 ,286 ,14 ,78 ,229 ,37 ,21 ,250 ,194 ,35 ,118 ,254 ,293 ,112 ,243 ,334 ,213] ,
           [115 ,0 ,179 ,101 ,40 ,136 ,152 ,136 ,160 ,112 ,80 ,10 ,186 ,192 ,138 ,152 ,240 ,328] ,
           [286 ,179 ,0 ,272 ,208 ,66 ,320 ,307 ,58 ,138 ,248 ,168 ,214 ,101 ,238 ,80 ,106 ,499 ],
           [14 ,101 ,272 ,0 ,64 ,214 ,51 ,35 ,235 ,179 ,21 ,104 ,240 ,278 ,98 ,229 ,320 ,227] ,
           [78 ,40 ,208 ,64 ,0 ,150 ,115 ,99 ,171 ,115 ,43 ,40 ,189 ,214 ,101 ,165 ,256 ,291] ,
           [229 ,136 ,66 ,214 ,150 ,0 ,262 ,250 ,29 ,72 ,190 ,136 ,149 ,67 ,173 ,16 ,109 ,363 ],
           [37 ,152 ,37 ,51 ,115 ,262 ,0 ,16 ,283 ,230 ,72 ,155 ,288 ,330 ,149 ,280 ,371 ,176] ,
           [21 ,136 ,307 ,35 ,99 ,250 ,16 ,0 ,270 ,214 ,56 ,136 ,304 ,314 ,165 ,264 ,355 ,192] ,
           [250 ,160 ,58 ,235 ,171 ,29 ,283 ,270 ,0 ,101 ,214 ,152 ,178 ,42 ,181 ,24 ,90 ,421] ,
           [194 ,112 ,138 ,179 ,115 ,72 ,230 ,214 ,101 ,0 ,158 ,104 ,77 ,139 ,141 ,90 ,181 ,291] ,
           [35 ,80 ,248 ,21 ,43 ,190 ,72 ,56 ,214 ,158 ,0 ,83 ,190 ,258 ,77 ,208 ,299 ,248] ,
           [118 ,10 ,168 ,104 ,40 ,136 ,155 ,136 ,152 ,104 ,83 ,0 ,181 ,210 ,141 ,152 ,246 ,331] ,
           [254 ,186 ,214 ,240 ,189 ,149 ,288 ,304 ,178 ,77 ,190 ,181 ,0 ,216 ,147 ,166 ,258 ,192] ,
           [292 ,192 ,101 ,278 ,214 ,67 ,330 ,314 ,42 ,139 ,258 ,210 ,216 ,0 ,240 ,67 ,128 ,376] ,
           [112 ,138 ,238 ,98 ,101 ,173 ,149 ,165 ,181 ,141 ,77 ,141 ,147 ,240 ,0 ,181 ,282 ,182] ,
           [243 ,152 ,80 ,229 ,165 ,16 ,280 ,264 ,24 ,90 ,208 ,152 ,166 ,67 ,181 ,0 ,109 ,445 ],
           [334 ,240 ,106 ,320 ,256 ,109 ,371 ,355 ,90 ,181 ,299 ,246 ,258 ,128 ,282 ,109 ,0 ,477] ,
           [213 ,328 ,499 ,227 ,291 ,363 ,176 ,192 ,421 ,291 ,248 ,331 ,192 ,376 ,182 ,445 ,477 ,0 ]]
# List of cities codes
#[AHUNGALLA 0 ,AIRPORT 1,ANURADHAPURA 2,BENTOTA 3,COLOMBO 4,DAMBULLA 5,GALLE 6,HIKKADUWA 7,HABARANA 8,KANDY 9,KALUTARA 10,NEGOMBO 11,NUWARAELIYA 12,POLONNARUWA 13,RATNAPURA 14,SIGIRIYA 15,TRINCOMALEE 16,YALA 17]

cities = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

# Helper function to calculate the distance traveled by a route
def calculate_distance(route):
    distance = 0
    for i in range(len(route)-1):
        distance += distances[route[i]][route[i+1]]
    distance += distances[route[-1]][route[0]]
    return distance

# Helper function to generate an initial population of routes
def generate_population():
    population = []
    for i in range(POPULATION_SIZE):
        route = cities.copy()
        random.shuffle(route)
        population.append(route)
    return population

# Helper function to apply mutation to a route
def mutate(route):
    i = random.randint(0, len(route)-1)
    j = random.randint(0, len(route)-1)
    route[i], route[j] = route[j], route[i]

# Helper function to apply crossover to two routes
def crossover(parent1, parent2):
    i = random.randint(0, len(parent1)-1)
    j = random.randint(0, len(parent2)-1)
    if i > j:
        i, j = j, i
    child = parent1[i:j]
    for city in parent2:
        if city not in child:
            child.append(city)
    return child

# Helper function to select routes for the next generation
def select(population):
    fitnesses = [calculate_distance(route) for route in population]
    total_fitness = sum(fitnesses)
    probabilities = [fitness / total_fitness for fitness in fitnesses]
    return random.choices(population, weights=probabilities, k=POPULATION_SIZE)

# Helper function to check if a route violates the distance constraint
def exceeds_distance(route):
    distance = calculate_distance(route)
    return distance > MAX_DISTANCE

# Main function to run the GA algorithm
def run_ga():
    population = generate_population()
    for generation in range(NUM_GENERATIONS):
        population = select(population)
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            if random.random() < MUTATION_RATE:
                mutate(child)
            if not exceeds_distance(child):
                new_population.append(child)
        if ELITISM:
            best_individual = min(population, key=calculate_distance)
            if best_individual not in new_population:
                new_population[0] = best_individual
        population = new_population
    return min(population, key=calculate_distance)
# Run the GA algorithm and print the result
best_route = run_ga()
print(f"Best route found: {best_route}. Total distance traveled: {calculate_distance(best_route)}.")


