
def position(time):
    acceleration = 9.8
    v_zero = 0
    formula = 0 + v_zero * time + ((1/2) * acceleration * time ** 2)
    return formula

def velocity(time, acceleration):
    acceleration = 9.8
    v_zero = 0
    formula = v_zero + acceleration * time
    return formula

def acceleration():
    return 9.8

"""

at t = 0 particle is at rest
at t = 5 particle is at 1 m

"""

if __name__ == "__main__":
    asdf = position(0)
    fdsa = position(5)
    print(asdf, fdsa)

