
def length(t, is_forward: bool=True, is_backwards: bool=False):
    direction = 1 if is_forward or is_backwards else 0
    direction *= -1 if is_backwards else 1
    direction *= 2 if is_forward and is_backwards else 1
    """
    Idea:
        x(t) - x(0) = t * v(0) + 0.5 * a(0) t^2
        x(t)=integral(v(t))
        v(t)=integral(a(t))
        a(t)=integral(u(t))
        u(t)=i*t
        
        this means u(t) is potential time energy loop in light nexus
        means mxn volume tensor of power the potential time energy in light nexus time loop
        means uxv volume tensor of spacetime
        prove spacetime per time is the kinetic time energy in light nexus time loop 
        showing 1 kg of plasma gas is photons and electrons for 1 beam of nexus light
        showing 1 g of plasma gas to force of a(t)xm(t) in volume densities of particles
        proving mass relationship to light
    """

def area(t, is_forward: bool=True, is_backwards: bool=False):
    direction = 1 if is_forward or is_backwards else 0
    direction *= -1 if is_backwards else 1
    direction *= 2 if is_forward and is_backwards else 1
    time = length(t + direction) * length(t)

def volume(t, is_forward: bool=True, is_backwards: bool=False):
    direction = 1 if is_forward or is_backwards else 0
    direction *= -1 if is_backwards else 1
    direction *= 2 if is_forward and is_backwards else 1
    time = length(t + direction) * length(t)

def force(t):
    pass

def acceleration(t):
    return length(t)

def momentum(t):
    pass

def velocity(t, is_forward: bool=True, is_backwards: bool=False):
    direction = 1 if is_forward or is_backwards else 0
    velocity_momentum =
    return length(t + )

"""

at t = 0 particle is at rest
at t = 5 particle is at 1 m

"""

if __name__ == "__main__":
    asdf = position(0)
    fdsa = position(5)
    print(asdf, fdsa)

