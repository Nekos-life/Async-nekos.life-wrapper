"""
Async Nekos.Life API Wrapper

An asynchronous wrapper for nekos.life API
"""

__title__ = "anekos"
__author__ = "NiumXp"
__license__ = "MIT"
__version__ = "2.0.0"

from . import errors, result
from .client import NekosLifeClient
from .enumeration import SFWImageTags
from .http_client import Endpoint
