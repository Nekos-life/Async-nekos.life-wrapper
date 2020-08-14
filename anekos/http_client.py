from aiohttp import ClientSession

from urllib.parse import urljoin, quote
from collections import namedtuple

from . import errors


base = "https://nekos.life/api/v2/"
Endpoint = namedtuple("Endpoint", "methods url is_deprecated")


def _make_url(endpoint, parameters):
    url = urljoin(base, endpoint)
    if parameters:
        url += '?' + '&'.join(f"{k}={quote(v)}" for (k,v) in parameters.items())
    return url


class HttpClient:
    """Client for making API requests.

    Parameters
    ----------
    session : asyncio.ClientSession
    """
    def __init__(self, *, session=None):
        if session:
            self._session = session
        else:
            self._session = ClientSession()

        self._endpoints = None

    async def get(self, endpoint: str, **parameters):
        url = _make_url(endpoint, parameters)
        async with self._session.get(url) as response:
            status = response.status

            if status in [500, 404]:
                raise errors.NoResponse("endpoint not found")

            response = await response.json()
            # the response can be a list or a dict
            # a list when the request is in /api/v2/endpoints

            if type(response) is dict:
                if response.get("msg", None):
                    raise errors.NoResponse("endpoint not found")

        return url, response
 
    async def get_image_bytes(self, url: str):
        """
        -> Coroutine
        Returns the image in bytes.

        Paremeters
        ----------
        url : str
            Image URL.

        Returns
        -------
        bytes
            Image in bytes.
        """
        async with self._session.get(url) as response:
            return await response.read()
 
    async def endpoint(self, endpoint: str, **parameters):
        """
        -> Coroutine
        Makes a GET request in the API's `endpoint`.

        Parameters
        ----------
        endpoint : str
            The endpoint where the GET request will be made.

        Returns
        -------
        dict
            The result of the request made.
        """
        url, response = await self.get(endpoint, **parameters)
        return {"endpoint": url, **response}

    async def endpoints(self):
        """
        -> Coroutine
        Returns all endpoints of the API.

        Returns
        -------
        List[anekos.Endpoint]
        """
        if self._endpoints:
            return self._endpoints

        _, endpoints_ = await self.get("endpoints")
        for _ in range(len(endpoints_)):
            endpoint = endpoints_.pop(-1)
            methods, right = endpoint.split('     ')

            if right.endswith("-DEPRECATED"):
                is_deprecated = True
                url, _ = right.split(' ', 1)
            else:
                is_deprecated = False
                url = right

            url = "https://nekos.life" + url

            endpoint = Endpoint(methods.split(','), url, is_deprecated)
            endpoints_.insert(0, endpoint)

        self._endpoints = endpoints_
        return endpoints_
