import random
import typing

from . import enumeration, http_client, result

Tag = typing.Union[str, enumeration.SFWImageTags]


class NekosLifeClient:
    """
    Main client that makes requests and returns objects for better handling.

    Parameters
    ----------
    session : asyncio.ClientSession
    """

    def __init__(self, *, session=None):
        self.http = http_client.HttpClient(session=session)

    async def image(self, tag: Tag, get_bytes: bool = False):
        """
        -> Coroutine
        Returns an image of a specific tag.

        Parameters
        ----------
        tag : Union[str, nekos.SFWImageTags]
            The tag of the image.
        get_bytes : bool (optional)
            Gets the bytes of an image.
            You can get the bytes of the image by accessing the `bytes` attribute  of the returned object.

        Returns
        -------
        nekos.result.ImageResult
        """
        if not isinstance(tag, (str, enumeration.SFWImageTags)):
            raise TypeError(f'{Tag} expected in `tag`')

        if type(get_bytes) is not bool:
            raise TypeError('bool expected in `get_bytes`')

        str_tag = tag if type(tag) is str else tag.value

        data_response = await self.http.endpoint('img/' + str_tag)

        data_response['tag'] = tag

        if get_bytes:
            image_url = data_response['url']
            image_bytes = await self.http.get_image_bytes(image_url)
            data_response['bytes'] = image_bytes

        return result.ImageResult(data_response)

    async def random_image(self, *, sfw: bool = True, get_bytes: bool = False):
        """
        -> Coroutine
        Returns an random image.

        Parameters
        ----------
        sfw : bool (optional, default is `True`)
            nekos.SFWImageTags will be used.
        get_bytes : bool (optional)
            Gets the bytes of an image.
            You can get the bytes of the image by accessing the `bytes` attribute  of the returned object.

        Returns
        -------
        nekos.result.ImageResult
        """
        if not sfw:
            raise RuntimeError("it is necessary to pass 'sfw'.")

        if type(sfw) != bool:
            raise TypeError('bool expected in `sfw`')

        if type(get_bytes) is not bool:
            raise TypeError('bool expected in `get_bytes`')

        tags = []
        if sfw:
            sfw_tags = enumeration.SFWImageTags.to_list()
            tags.extend(sfw_tags)

        tag = random.choice(tags)

        return await self.image(tag, get_bytes=get_bytes)

    async def random_fact_text(self):
        """
        -> Coroutine
        Returns a random fact.

        Returns
        -------
        nekos.result.TextResult
        """
        data_response = await self.http.endpoint('fact')
        return result.TextResult(data_response, target='fact')

    async def random_cat_text(self):
        """
        -> Coroutine
        Returns a random cat-like text.

        Returns
        -------
        nekos.result.TextResult
        """
        data_response = await self.http.endpoint('cat')
        return result.TextResult(data_response, target='cat')

    async def random_why(self):
        """
        -> Coroutine
        Returns a random questionnaire.

        Returns
        -------
        nekos.result.TextResult
        """
        data_response = await self.http.endpoint('why')
        return result.TextResult(data_response, target='why')

    async def spoiler(self, text: str):
        """
        -> Coroutine
        Creates an individual spoiler per letter for Discord.

        Paramaters
        ----------
        text : str
            It must be between 1 and 2000 characters.

        Returns
        -------
        nekos.result.TextResult
        """
        if type(text) is not str:
            raise TypeError('str expected in `text`')

        if not (0 < len(text) < 2000):
            raise TypeError("'text' must be between 1 and 2000 characters")

        data_response = await self.http.endpoint('spoiler', text=text)
        return result.TextResult(data_response, target='spoiler')

    async def random_name(self):
        """
        -> Coroutine
        Returns a random name.

        Returns
        -------
        nekos.result.TextResult
        """
        data_response = await self.http.endpoint('name')
        return result.TextResult(data_response, target='name')

    async def owoify(self, text: str):
        """
        -> Coroutine
        OwOify the `text`.

        Parameters
        text : str

        Returns
        -------
        nekos.result.TextResult
        """
        if type(text) is not str:
            raise TypeError('str expected in `text` parameter')

        if not (0 < len(text) < 200):
            raise IndexError("'text' must be between 1 or 200 characters")

        data_response = await self.http.endpoint('owoify', text=text)
        return result.TextResult(data_response, target='owo')

    async def random_8ball(self, question, *, get_image_bytes: bool = False):
        """
        -> Coroutine
        Returns a random answer for the specified question.

        Parameters
        ----------
        question : str
            The your question.
        get_image_bytes : bool
            Gets the bytes of the image.

        Returns
        -------
        nekos.result.EightBallResult
        """
        if type(question) is not str:
            raise TypeError('str expected in `question` parameter')

        if type(get_image_bytes) is not bool:
            raise TypeError('bool expected in `get_image_bytes` parameter')

        data_response = await self.http.endpoint('8ball')

        if get_image_bytes:
            image_url = data_response['url']
            image_bytes = await self.http.get_image_bytes(image_url)
            data_response['image_bytes'] = image_bytes

        return result.EightBallResult(data_response)

    async def endpoints(self):
        """Alias for nekos.HTTPClient.endpoints."""
        return await self.http.endpoints()
