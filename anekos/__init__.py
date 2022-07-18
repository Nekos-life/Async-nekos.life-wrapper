"""
Async Nekos.Life API Wrapper

An asynchronous wrapper for nekos.life API
"""

__title__ = 'anekos'
__author__ = 'NiumXP'
__license__ = 'MIT'
__version__ = '1.0.1'

from . import errors, result
from .client import NekosLifeClient
from .enumeration import SFWImageTags
from .http_client import Endpoint
