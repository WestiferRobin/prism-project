===============================
🧪 Project Silver – Equation Reference
===============================

This document defines the physical model hierarchy, spatial-temporal dimensions,
and core classical mechanics equations guiding all Project Silver simulations.

-------------------------------
Dimensional Definitions (Topological Mechanics Framework)
-------------------------------

Position      : 1-D for { x, y, z, w }
Velocity      : 2-D for { xy, zw, ... }
Acceleration  : 3-D for { xyz, wxyz }
Time          : 4-D (ONLY): t = i * τ   (imaginary time layer)

This layering allows motion modeling under 1–5D perspectives, where:
5D = 4D (imaginary time) + 1D (spatial extension)

-------------------------------
Coordinate System Transformations
-------------------------------

Polar (1D and 2D):
    x = r * cos(θ)
    y = r * sin(θ)
    r² = sqrt(x² + y²)

Spherical (2D and 3D):
    z = p * cos(φ)
    r = p * sin(φ)
    p² = sqrt(r² + z²)

Hyperspherical (3D and 4D):
    q = u * cos(ψ)
    p = u * sin(ψ)
    u² = sqrt(p² + q²)

Imaginary Space-Time (4D and 5D):
    v = w * cos(ω)
    u = w * sin(ω)
    w² = sqrt(v² + u²)

-------------------------------
Position Modeling in 1–4D
-------------------------------

For <x>, <x, y>, <x, y, z>, <x, y, z, w> (3D + 1D = 4D):

    x(t) = x₀ + t * v₀ + (1/2) * a * t²
    v(t) = v₀ + a₀ * t
    a(t) = a₀ + a(t) * i     (imaginary acceleration component)

-------------------------------
Angular Quantities
-------------------------------

Apply angular versions of x(t), v(t), a(t) to:
    θ(t), φ(t), ψ(t), ω(t) for polar, spherical, and hyperspherical systems.

-------------------------------
Force Equations (Rectangular and Polar)
-------------------------------

    F = m * g
    F = m * a = dp/dt = d/dt(m * v)
    0 = m * a - m * g     (force balance)
    τ = r * F             (torque)

-------------------------------
Energy Equations (Rectangular and Polar)
-------------------------------

E(t):
    PE = m * g * h
    KE = (1/2) * m * v²
    KE₀ + PE₀ = KE_f + PE_f       (conservation of energy)
    Q(t) - Q(0) = m * c * (T(t) - T(0))    (thermal energy)

Work and Power:
    Work   = E(t) - E(0) = W(t) = F(t) * l(t)
    Power  = (W(t) - W(0)) / t

-------------------------------
Math Utilities
-------------------------------

    Length:     L(t) = sqrt((x(t) - x₀)² + (y(t) - y₀)²)
    Area:       A(t) = l(t) * l(t)
    Volume:     V(t) = A(t) * l(t)
    Linear Eq:  f(x) = m * x + b = y
    Plane Eq:   a * x(t) + b * y(t) + c * z(t) = 0

-------------------------------
Future Extensions
-------------------------------

    - Gravity       ✅
    - Spring Systems (Elastic / Inelastic)
    - Thermal Energy Modeling (pre-Maxwell)
    - Maxwell's Equations (E/M Field Systems)
    - Lorentz Force: F = q(E + v × B)
    - Imaginary Time Layering: t = i * τ
    - 5D Inertial Symmetry Frames

-------------------------------
End of Reference
Last updated: 2025-07-18
