def lcg(seed, c=1349, m=349302):
    while True:
        seed = c*seed%m
        yield seed/m

gen = lcg(5)

with open("linear_congruent_random_numbers.txt", 'a') as outfile:
    for _ in range(1000000):
        outfile.write(f"{next(gen)}\n")
    
