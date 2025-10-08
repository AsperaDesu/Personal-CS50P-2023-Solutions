E = 300000000
mass = int(input('m : '))

def energy(mass):
    return (mass * (E**2))

print(f'E : {energy(mass)}')