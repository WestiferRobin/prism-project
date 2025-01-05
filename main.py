from grid.builder import build_sector
from grid.printer import print_sector

if __name__ == "__main__":
    sector = build_sector(m=4, n=4)
    print_sector(sector)

"""
Config: SolarConquest(4x4), SwiftConquest(3x3),

ConquestSector:
    a~~~
    ~~a~
    ~A~~
    ~~~~
    
    0211
    2301
    1021
    111~

ClassicSector:
~~~
~A~
~~a

311
1A2
12a

SwiftSector:
~~
~~




"""