from aiohttp import ClientSession

from urllib.parse import urljoin, quote

from . import errors


base = "https://nekos.life/api/v2/"

def make_url(endpoint, parameters):
    url = urljoin(base, endpoint)
    if parameters:
        url += '?' + '&'.join(f"{k}={quote(v)}" for (k,v) in parameters.items())
    return url


class HttpClient:
    """Client for making API requests.

    Parameters:
        session (asyncio.ClientSession)
    """
    def __init__(self, *, session=None):
        if session:
            self._session = session
        else:
            self._session = ClientSession()

    async def get(self, endpoint: str, **parameters):
        url = make_url(endpoint, parameters)
        async with self._session.get(url) as response:
            status = response.status

            if status in [500, 404]:
                raise errors.NoResponse("endpoint not found")

            response = await response.json()
            
            if response.get("msg", None):
                raise errors.NoResponse("endpoint not found")

        return url, response
 
    async def get_image_bytes(self, image_url: str):
        """
        -> Coroutine
        Returns the image in bytes.
        
        Paremeters:
            image_url (str): Image URL.

        Return:
            bytes: Image in bytes.
        """
        async with self._session.get(image_url) as response:
            return await response.read()
 
    async def endpoint(self, endpoint: str, **parameters):
        """
        -> Coroutine
        Makes a GET request in the API's `endpoint`.
        
        Parameters:
            endpoint (str): The endpoint where the GET request will be made.

        Return:
            dict: The result of the request made.
        """
        url, response = await self.get(endpoint, **parameters)
        return {"endpoint": url, **response}

    async def endpoints(self):
        #'HEAD,OPTIONS,GET     /api/v2/endpoints',
        raise NotImplementedError()
