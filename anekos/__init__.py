"""
Async Nekos.Life API Wrapper

A basic wrapper for Nekos.Life API.
"""

__title__ = "anekos"
__author__ = "NiumXp"
__license__ = "MIT"
__version__ = "1.0.0"

from .client import NekosLifeClient
from .enumeration import NSFWImageTags, SFWImageTags
from . import result, errors
from .http_client import Endpoint
