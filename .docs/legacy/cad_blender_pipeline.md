## TODO(s)

    Goal: Get a pipeline going to Blender/Sprite and CAD formats
    - Get GIMP to Photoshop
    - Get Blender to Maya
    - Get FreeCAD to AutoCAD
    - Get CAD to Printer in Metal


# Model Foundation (Math + Physics + Programming)
- Define your vehicle (Speeder, Shuttle) as a RigidBody with mass, velocity, acceleration, center of mass, shape, and orientation.

- Start with core classical mechanics:

- Implement:
  - x(t) = x₀ + v₀·t + ½·a·t² (position in motion)
    - When t = i * τ_time
    - also for x with { y, z, w }
      - Coordinates:
        - 0-D: Point/Vertex, Null/Origin
        - 1-D: Line, Vector
        - 2-D: Rectangular, Polar
        - 3-D: Spherical, Cylindrical
        - 4-D: Hyper Coordinates
  - F = m(t) * a(t), (force in motion)
    - Math Requirements:
      - Length = sqrt((x(i) - x(0))^2 - (y(i) - y(0))^2) for xy plane
      - Area = Length(t) * Length(t)
      - Volume = Area(t) * Length(t)
      - Space = Volume(t) * Length(t)
      - HyperSpace = Space(t) * Length(t)
    - Motion Requirements:
      - When a(t) = a(0) + i * t and assume a(0) = 0
        - And v(t) = v(0) + a(t) * t and assume v(0) = 0
        - And x(t) = x(0) + v₀·t + ½·a·t² and assume x(0) = 0
    - Mass Requirements:
      - density units: grams and total length volume
        - density: grams per cm^3
        - density: kilograms per m^3
      - Mass = m(t) = density(t) * Volume(t)
    - And L(t) = sqrt((x(i) - x(0)))
    - F(t) = m(t) * a(t) = d(m(t) * v(t))/dt
    - F(t) = -k * Length(t)
  - Work W(t) = F(t) * Length(t) (force to energy)
    - E(t) = m(t) * a(t) * Length(t) - (1/2) * m(t) * v(t)^2
    - W(t) = E(t) - E(0)
    - Q(t) = m(t) * c * (T(t) - T(0)) (heat to energy with density)
    - Power = P(t) = (W(t) - W(0)) / t (example of thermal to mechanical energies' problem)
  - τ = r × F (torque)
    - Angular Motion Equations based on Classic Motion in Spaces
    - Ensure Trigonometry dependence
    - centripetal force and acceleration
    - spring oscillation formula with spring force formula (google it)

Energy, work, power, thermodynamics, etc.

Use your Nexus Labs codebase (in cli/project_silver.py) to simulate physical motion, control parameters, and record data.
