from enum import Enum

class PrefixType(str, Enum):
    YOCTO = "yocto"   # 10^-24
    ZEPTO = "zepto"   # 10^-21
    ATTO = "atto"     # 10^-18
    FEMTO = "femto"   # 10^-15
    PICO = "pico"     # 10^-12
    NANO = "nano"     # 10^-9
    MICRO = "micro"   # 10^-6
    MILLI = "milli"   # 10^-3
    CENTI = "centi"   # 10^-2
    DECI = "deci"     # 10^-1
    NONE = ""         # 10^0 (no prefix)
    DECA = "deca"     # 10^1
    HECTO = "hecto"   # 10^2
    KILO = "kilo"     # 10^3
    MEGA = "mega"     # 10^6
    GIGA = "giga"     # 10^9
    TERA = "tera"     # 10^12
    PETA = "peta"     # 10^15
    EXA = "exa"       # 10^18
    ZETTA = "zetta"   # 10^21
    YOTTA = "yotta"   # 10^24

    @property
    def factor(self) -> float:
        return {
            PrefixType.YOCTO: 1e-24,
            PrefixType.ZEPTO: 1e-21,
            PrefixType.ATTO:  1e-18,
            PrefixType.FEMTO: 1e-15,
            PrefixType.PICO:  1e-12,
            PrefixType.NANO:  1e-9,
            PrefixType.MICRO: 1e-6,
            PrefixType.MILLI: 1e-3,
            PrefixType.CENTI: 1e-2,
            PrefixType.DECI:  1e-1,
            PrefixType.NONE:  1e0,
            PrefixType.DECA:  1e1,
            PrefixType.HECTO: 1e2,
            PrefixType.KILO:  1e3,
            PrefixType.MEGA:  1e6,
            PrefixType.GIGA:  1e9,
            PrefixType.TERA:  1e12,
            PrefixType.PETA:  1e15,
            PrefixType.EXA:   1e18,
            PrefixType.ZETTA: 1e21,
            PrefixType.YOTTA: 1e24,
        }[self]

    @property
    def symbol(self) -> str:
        return {
            PrefixType.YOCTO: "y",
            PrefixType.ZEPTO: "z",
            PrefixType.ATTO:  "a",
            PrefixType.FEMTO: "f",
            PrefixType.PICO:  "p",
            PrefixType.NANO:  "n",
            PrefixType.MICRO: "μ",
            PrefixType.MILLI: "m",
            PrefixType.CENTI: "c",
            PrefixType.DECI:  "d",
            PrefixType.NONE:  "",
            PrefixType.DECA:  "da",
            PrefixType.HECTO: "h",
            PrefixType.KILO:  "k",
            PrefixType.MEGA:  "M",
            PrefixType.GIGA:  "G",
            PrefixType.TERA:  "T",
            PrefixType.PETA:  "P",
            PrefixType.EXA:   "E",
            PrefixType.ZETTA: "Z",
            PrefixType.YOTTA: "Y",
        }[self]
