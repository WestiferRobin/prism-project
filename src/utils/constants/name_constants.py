from src.utils.enums.prism_enums import RaceType

# TODO: Consider on making this into a file... during solar-conquest


MALE_NAME_POOL = {
    RaceType.Human: [
        "Shinel", "Vorxim", "Narshi", "Quxim", "Nelmel", "Fertor", "Torqu", "Dravex", "Ximnar", "Zanmel",
        "Golnar", "Lundra", "Nartor", "Ximlun", "Torzan", "Kisdra", "Ferqu", "Shizor", "Narfer", "Quvor",
        "Tiknar", "Zorvik", "Ximtor", "Nelgla", "Raxlun", "Lunkal", "Zantor", "Zornar", "Melnel", "Kisnel"
    ],
    RaceType.Aeon: [
        "Fervor", "Zornar", "Nelxim", "Dramel", "Torzan", "Vorvek", "Quzorn", "Lundra", "Zanmel", "Tikvor",
        "Raxmel", "Narqu", "Zorgla", "Ferlon", "Ximnar", "Golzon", "Shirax", "Lunkis", "Draxim", "Vorqu",
        "Kalgol", "Torzor", "Tiklun", "Raxnar", "Shivor", "Kisnel", "Nelzor", "Zorvex", "Melkis", "Ximkal"
    ],
    RaceType.Archon: [
        "Tikmel", "Zornel", "Glafer", "Narkal", "Ximzor", "Golvek", "Dravex", "Ferkis", "Raxlun", "Quzon",
        "Tiknar", "Zantor", "Zorgol", "Narvor", "Lundra", "Ximkal", "Kiszon", "Melvor", "Shinel", "Vorxim",
        "Nelkal", "Torqu", "Dralun", "Narqu", "Lunkis", "Zorlan", "Kalvor", "Torzor", "Ferxim", "Glaqu"
    ],
    RaceType.Slug: [
        "Glibvor", "Slornax", "Zorxug", "Muktik", "Glozarn", "Narzub", "Ximslug", "Tragol", "Vorlub", "Splotor",
        "Klogar", "Drosqu", "Drigla", "Zanlub", "Slomel", "Tarnak", "Gruknar", "Qulug", "Raxgla", "Sligor",
        "Veklub", "Fergub", "Shiglub", "Tiknar", "Zurgla", "Mukvor", "Blobnar", "Zubgla", "Slikal", "Globruk"
    ],
    RaceType.Bug: [
        "Klikzor", "Zatchnar", "Trukvik", "Xorgla", "Skitzor", "Draklis", "Ferkik", "Zanbug", "Torklik", "Skrarn",
        "Narblip", "Glibtik", "Snarkal", "Zorbit", "Veklar", "Bugzor", "Kliknak", "Tiktik", "Chugor", "Glarnak",
        "Dronik", "Skavex", "Ximbur", "Zarnik", "Mektor", "Snorvak", "Xiklor", "Blitnak", "Krikzor", "Glomex"
    ],
    RaceType.Reptile: [
        "Szzar", "Varn", "Drako", "Scarn", "Thessik", "Xarnor", "Raviss", "Hissik", "Snakar", "Zarnis",
        "Veklor", "Karnix", "Slizzar", "Trask", "Grizzor", "Zorvess", "Darnak", "Kroth", "Liskarn", "Trogos",
        "Sarnax", "Heklor", "Zissarn", "Krivar", "Vornak", "Tregiss", "Marnok", "Tharnax", "Rekkar", "Xizzor"
    ],
    RaceType.Mammal: [
        "Rufus", "Koda", "Tharn", "Barro", "Lupo", "Farran", "Dargo", "Ronak", "Varko", "Marlon",
        "Bruno", "Jarn", "Tork", "Fenris", "Argo", "Wex", "Drogo", "Kelran", "Morvan", "Voss",
        "Karnak", "Talon", "Burkan", "Lexor", "Darnak", "Xarn", "Larnak", "Hark", "Sarnor", "Karro"
    ],
    RaceType.Ape: [
        "Gor", "Brak", "Ulmo", "Zan", "Krog", "Mogor", "Krash", "Lurak", "Bruno", "Ragor",
        "Throg", "Grak", "Urmak", "Tarr", "Klem", "Bronk", "Snarl", "Groth", "Zurg", "Maruk",
        "Torak", "Dronk", "Thorn", "Rango", "Kurg", "Morak", "Narg", "Bork", "Togar", "Zarn"
    ],
    RaceType.Raptor: [
        "Claw", "Rend", "Snarl", "Vrex", "Karn", "Razor", "Talon", "Strik", "Drakk", "Krarn",
        "Fang", "Vorn", "Xarn", "Tarruk", "Grizz", "Skarn", "Thrash", "Slith", "Gornak", "Ravak",
        "Zarnak", "Drok", "Velok", "Krath", "Skar", "Vornak", "Drask", "Krex", "Barrok", "Zorak"
    ],
    RaceType.Shark: [
        "Chomp", "Razor", "Finn", "Gnasher", "Vark", "Shred", "Mako", "Thorn", "Ravak", "Snash",
        "Krill", "Drift", "Slask", "Vexor", "Bite", "Jark", "Nashor", "Klash", "Skarf", "Wrex",
        "Vorak", "Kelro", "Gorak", "Trask", "Sharv", "Xarnor", "Marlin", "Barrak", "Karsh", "Reefor"
    ],
    RaceType.Fish: [
        "Bloop", "Gill", "Skim", "Ripple", "Mar", "Swimmy", "Wavo", "Sploosh", "Glint", "Flash",
        "Kelp", "Shoal", "Dart", "Minnie", "Finno", "Tidal", "Gurgle", "Splash", "Minnow", "Trekka",
        "Nemo", "Snook", "Brine", "Trouto", "Slick", "Krillo", "Flarp", "Jelly", "Spout", "Vento"
    ],
    RaceType.Squid: [
        "Ink", "Tentak", "Slerg", "Quarn", "Blip", "Squark", "Drouk", "Zolgar", "Squirm", "Nekthul",
        "Gloop", "Trekth", "Takk", "Zarnath", "Orlith", "Blorp", "Tentis", "Gronth", "Skult", "Krothul",
        "Narlux", "Shloop", "Yelgar", "Grib", "Krell", "Tharnax", "Wormak", "Zurath", "Clorp", "Varnul"
    ]
}

FEMALE_NAME_POOL = {
    RaceType.Human: [
        "Narkis", "Kalnel", "Kalmel", "Dranel", "Zorqu", "Lunmel", "Shiren", "Valexa", "Mirana", "Thessia",
        "Vala", "Aelira", "Serin", "Nyra", "Isolde", "Mira", "Talia", "Alia", "Rina", "Noelle",
        "Liora", "Celia", "Nexa", "Kira", "Elara", "Lyra", "Saria", "Tirra", "Zelene", "Faye"
    ],
    RaceType.Aeon: [
        "Drarax", "Melmel", "Golfer", "Lundra", "Narlun", "Quvor", "Zerena", "Valira", "Thyra", "Elsera",
        "Kyra", "Shaeli", "Orlena", "Mirel", "Tessal", "Vanya", "Zahra", "Linara", "Serel", "Arissa",
        "Trenna", "Myri", "Talexa", "Alindra", "Venara", "Korell", "Tavira", "Erysa", "Zanira", "Luneth"
    ],
    RaceType.Archon: [
        "Kalrax", "Tikqu", "Fertik", "Qulun", "Zantor", "Vorxim", "Nalexa", "Trisara", "Velixa", "Zolanna",
        "Kessira", "Telyra", "Soraya", "Nyrel", "Cassira", "Thirra", "Yllara", "Mirexa", "Sarnelle", "Dralexa",
        "Zirella", "Norrisa", "Kellira", "Vanyra", "Liriel", "Tiranna", "Ferexa", "Ormira", "Quinra", "Xanira"
    ],
    RaceType.Slug: [
        "Glatik", "Tikkal", "Glaxim", "Tikzor", "Raxshi", "Zanrax", "Melmel", "Golgla", "Zanqu", "Glaqu",
        "Ferlun", "Kiskis", "Zanvek", "Nelvek", "Kisgol", "Vorshi", "Narfer", "Vekshi", "Tikdra", "Tikdra",
        "Shinar", "Vorfer", "Vekfer", "Ferrax", "Kaltor", "Lunvek", "Kistik", "Shivek", "Tikshi", "Lungla"
    ],
    RaceType.Bug: [
        "Tikqu", "Vekgla", "Golnar", "Ximvek", "Ferkis", "Shifer", "Golvek", "Tikrax", "Tiknar", "Tikzan",
        "Golrax", "Glakis", "Golzan", "Tortor", "Shifer", "Golnar", "Kalzan", "Lunqu", "Zannar", "Torzan",
        "Zornar", "Torvek", "Dradra", "Torzan", "Lunzor", "Torgol", "Kalzor", "Vekshi", "Qugla", "Zorqu"
    ],
    RaceType.Reptile: [
        "Golrax", "Shidra", "Tikmel", "Golzan", "Lundra", "Vorvek", "Zannar", "Nelzor", "Golvek", "Nelfer",
        "Luntor", "Ximlun", "Raxqu", "Shivek", "Torshi", "Zanzor", "Narvek", "Kisrax", "Nardra", "Narvek",
        "Zorgol", "Torfer", "Kalrax", "Nelnar", "Kaldra", "Ferdra", "Golmel", "Torzan", "Kisqu", "Kisvek"
    ],
    RaceType.Mammal: [
        "Lungla", "Golzor", "Fervek", "Kisdra", "Ximfer", "Kaldra", "Zorzan", "Glarax", "Zorkis", "Melnel",
        "Drashi", "Dranar", "Dragla", "Shizan", "Vortik", "Narxim", "Shilun", "Kalshi", "Zordra", "Tikgla",
        "Ximnel", "Dralun", "Tikfer", "Tiknar", "Ferkal", "Kaltor", "Qutor", "Vekxim", "Glakal", "Luntik"
    ],
    RaceType.Ape: [
        "Zanrax", "Lungol", "Tikkis", "Kistor", "Nellun", "Vekgla", "Fertor", "Tiklun", "Zannar", "Drakal",
        "Tiknel", "Raxnar", "Zannel", "Zorkis", "Narlun", "Lungla", "Torvor", "Dranel", "Melgol", "Golkal",
        "Kiszan", "Glamel", "Narnel", "Narnel", "Shigol", "Golvek", "Luntor", "Qugol", "Vekkal", "Fermel"
    ],
    RaceType.Raptor: [
        "Lunmel", "Vektor", "Zorzor", "Dranel", "Neltor", "Tikkal", "Fermel", "Ferqu", "Narlun", "Golnar",
        "Golgol", "Drazan", "Lunnar", "Drator", "Nardra", "Glakal", "Lunmel", "Tikgla", "Drazor", "Golvek",
        "Lunkis", "Lungol", "Zanmel", "Shivor", "Vorlun", "Tikshi", "Lunlun", "Shishi", "Kisxim", "Tikrax"
    ],
    RaceType.Shark: [
        "Melmel", "Dratik", "Melgol", "Qufer", "Ferkal", "Tiktor", "Tormel", "Nelfer", "Dralun", "Zandra",
        "Zorfer", "Fernel", "Narkis", "Narkal", "Fernar", "Glarax", "Neldra", "Shimel", "Vekshi", "Lungla",
        "Fernel", "Raxzan", "Qukal", "Melnar", "Zanmel", "Vorkis", "Draqu", "Vekgol", "Quvor", "Ququ"
    ],
    RaceType.Fish: [
        "Raxgol", "Shidra", "Ximnel", "Narkal", "Vordra", "Kisvor", "Vekdra", "Drashi", "Lunkal", "Fertik",
        "Zannel", "Drazan", "Golqu", "Zordra", "Luntik", "Shinar", "Nelnar", "Vekgla", "Zanzor", "Zorvor",
        "Neldra", "Shikal", "Zanmel", "Ferrax", "Zanfer", "Vekqu", "Raxnar", "Nelgla", "Nelfer", "Zorvor"
    ],
    RaceType.Squid: [
        "Ferfer", "Ximmel", "Zantik", "Zanxim", "Kalnar", "Raxdra", "Shilun", "Qushi", "Ximzan", "Vorfer",
        "Glazan", "Kisnel", "Melzor", "Zornar", "Shikal", "Meltik", "Glazor", "Glavek", "Lunmel", "Ximtik",
        "Vektik", "Gladra", "Vekvek", "Torxim", "Lunqu", "Drakis", "Ximzor", "Ferkis", "Melnel", "Glavek"
    ]
}


