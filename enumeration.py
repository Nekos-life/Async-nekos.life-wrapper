from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, *args):
        return name.lower()


#['HEAD,OPTIONS,GET     /api/hug -DEPRECATED',
# 'HEAD,OPTIONS,GET     /api/kiss -DEPRECATED',     
# 'HEAD,OPTIONS,GET     /api/lewd/neko -DEPRECATED',
# 'HEAD,OPTIONS,GET     /api/lizard -DEPRECATED',   
# 'HEAD,OPTIONS,GET     /api/neko -DEPRECATED',     
# 'HEAD,OPTIONS,GET     /api/pat -DEPRECATED',      
# 'HEAD,OPTIONS,GET     /api/v2/name',
# 'HEAD,OPTIONS,GET     /api/v2/owoify',
# 'HEAD,OPTIONS,GET     /api/v2/spoiler',
# 'HEAD,OPTIONS,GET     /api/why -DEPRECATED']


class NSFWImageTags(AutoName):
    FEMDOM = auto()
    CLASSIC = auto()
    EROFEET = auto()
    EROKITSUNE = "erok"
    LESBIAN = "les"
    #hololewd
    #lewdk
    KETA = auto()
    FEETGIF = "feetg"
    NSFW_NEKO_GIF = auto()
    EROYURI = auto()
    KUNI = auto()
    TITS = auto()
    PUSSY = "pussy_jpg"
    CUM = "cum_jpg"
    PUSSYGIF = "pussy"
    #lewdkemo
    #lewd
    CUM_GIF = "cum"
    SPANK = auto()
    SMALLBOOBS = auto()
    RANDOM_HENTAI_GIF = "Random_hentai_gif"
    AVATAR = auto()
    BOOBS = auto()
    FEET = auto()
    GIRL_SOLO_GIF = "solog"
    BLOWJOB_GIF = "bj"
    YURI = auto()
    TRAP = auto()
    ANAL = auto()
    BLOWJOB = auto()
    HOLOERO = auto()
    GASM = auto()
    HENTAI = auto()
    FUTANARI = auto()
    ERO = auto()
    GIRL_SOLO = "solo"
    PUSSY_WANK_GIF = "pwankg"
    ERONEKO = "eron"
    EROKEMONOMINI = "erokemo"
    

class SFWImageTags(AutoName):
    TICKLE = auto()
    NEKOGIF = "ngif"
    MEOW = auto()
    POKE = auto()
    KISS = auto()
    EIGHTBALL = "8ball"
    LIZARD = auto()
    SLAP = auto()
    CUDDLE = auto()
    GOOSE = auto()
    AVATAR = auto()
    FOX_GIRL = auto()
    HUG = auto()
    GECG = auto()
    PAT = auto()
    SMUG = auto()
    KEMONOMIMI = auto()
    HOLO = auto()
    WALLPAPER = auto()
    WOOF = auto()
    BAKA = auto()
    FEED = auto()
    NEKO = auto()
    WAIFU = auto()
