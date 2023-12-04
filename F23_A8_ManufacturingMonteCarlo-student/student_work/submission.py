import random


def simulate(oring_diameter_mean, oring_tolerance,
             piston_groove_diameter_mean, piston_groove_tolerance,
             tolerance_range_min, tolerance_range_max):
    """
    Use `random.normalvariate(mean, std_deviation)`
    to simulate one instance of a manufactured part.
    This function should return a boolean value indicating
    if the piston o-ring is within the designated tolerance.
    """
    o_ring_diameter = random.normalvariate(oring_diameter_mean, oring_tolerance / 3)
    piston_groove_diameter = random.normalvariate(piston_groove_diameter_mean, piston_groove_tolerance / 3)

    x = o_ring_diameter + piston_groove_diameter - 25

    return tolerance_range_min <= x <= tolerance_range_max


if __name__ == '__main__':
    """
    As in Assessment 7, any code not in the simulate function 
    (aside from the import statement and code in other functions you optionally defined) 
    needs to be inside of this if branch for your program to work properly
    """

    values = input("SIMSEED> ").split()
    n = int(values[0])
    random.seed(values[1])

    o_ring_diameter_mean, o_ring_tolerance = map(float, input("O-RING> ").split())
    piston_groove_diameter_mean, piston_groove_tolerance = map(float, input("PISTON> ").split())
    tolerance_range_min, tolerance_range_max = map(float, input("XLIM> ").split())

    failures = 0

    for _ in range(n):
        if not simulate(o_ring_diameter_mean, o_ring_tolerance, piston_groove_diameter_mean,
                        piston_groove_tolerance, tolerance_range_min, tolerance_range_max):
            failures += 1

    failure_probability = (failures / n) * 100
    print(f"OUTPUT {failure_probability:.2f}")
