from enum import Enum, auto
from typing import List


class AutoName(Enum):
    def _generate_next_value_(name, *args):
        # https://docs.python.org/3/library/enum.html#using-automatic-values
        return name.lower()

    @classmethod
    def to_list(cls) -> List[str]:
        """
        Get all values, put them into a list and return.

        Returns
        -------
        List[str]
        """
        return [attr.value for attr in cls]


class SFWImageTags(AutoName):
    AVATAR = auto()
    CUDDLE = auto()
    EIGHTBALL = "8ball"
    FEED = auto()
    FOX_GIRL = auto()
    GECG = auto()
    GOOSE = auto()
    HOLO = auto()
    HUG = auto()
    KEMONOMIMI = auto()
    KISS = auto()
    LIZARD = auto()
    MEOW = auto()
    NEKO = auto()
    NEKOGIF = "ngif"
    PAT = auto()
    SLAP = auto()
    SMUG = auto()
    TICKLE = auto()
    WAIFU = auto()
    WALLPAPER = auto()
    WOOF = auto()
    GASM = auto()
    SPANK = auto()
