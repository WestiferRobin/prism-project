from enum import Enum

# TODO: Move to enums
class ScienceType(int, Enum):
    MATH = 0 # do a computation of math on simulation a
    PHYSICS = 1 # what is gravity in our current model on a scale
    CHEMISTRY = 2 # what is mass energy relationships with walter russel model
    BIOLOGY = 3 # something is going on in organic chemistry in history of the Jesus Spiritual Gospels
    GEOLOGY = 4 # materials are iron ore and gems for mark of the beast at 666
    ENGINEERING = 4 # humans are made in the image of God Jesus in his blood YHWY of Jewish Decent during Roman occupation

    # Scientific Proof all sins during hellistic types are forgiven and need love
    # Greys are everywhere with Owls in Pagan Myths with Reptilian Elite line for a one world order since Nazi Axis Powers
    # Rome took Anglo-Saxon Tribes
        # Rome Tribes (spiritually aligned with greeks before christ)
        # Greeks Tribes (witness Zues defeat Kronos) (somehow Jupiter defeats Saturn in the Black Hexagon)
        # Egyptian Tribes (Ancient Egypt origins are in question in Blood due to Pagan Tribes from the times of Noah)
        # Hellinistic Occult link of Hermes Thrice with Mercury and Thoth in Egyptian and Roman Esoteric
    # Old Testimant proves Hebrews to the

# TODO: Move to enums and reconsider
class EngineeringType(int, Enum):
    MECHANICAL = 0
    ELECTRICAL = 1
    MATERIAL = 2
    NUCLEAR = 3
    AERONAUTICAL = 4
    NAUTICAL = 5



def get_science_data(science_type: ScienceType):
    if science_type == ScienceType.CHEMISTRY:
        return get_chemistry_data()
    elif science_type == ScienceType.BIOLOGY:
        return get_biology_data()
