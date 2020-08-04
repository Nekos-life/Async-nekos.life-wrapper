import typing
import random

from . import http_client, enumeration, result

Tag = typing.Union[str, enumeration.SFWImageTags, enumeration.NSFWImageTags]


class NekosLifeClient:
    """
    Main client that makes requests and returns objects for better handling.
    
    Parametros:
        session (asyncio.ClientSession)
    """
    def __init__(self, *, session=None):
        self.http = http_client.HttpClient(session=session)

    async def image(self, tag: Tag, get_bytes: bool=False):
        """
        -> Coroutine
        Returns an image of a specific tag.

        Parameters
        ----------
        tag : Union[str, anekos.SFWImageTags, anekos.NSFWImageTags]
            The tag of the image.

        get_bytes : bool (optional)
            Gets the bytes of an image.
            You can get the bytes of the image by accessing the `bytes` attribute  of the returned object.

        Return
        ------
            anekos.result.ImageResult
        """
        if not isinstance(tag, (str, enumeration.SFWImageTags, enumeration.NSFWImageTags)):
            raise TypeError("'str' or 'Tag' expected")

        tag = tag if type(tag) is str else tag.value

        data_response = await self.http.endpoint("img/" + tag)

        if get_bytes:
            image_url = data_response["url"]
            image_bytes = await self.http.get_image_bytes(image_url)
            data_response["bytes"] = image_bytes

        return result.ImageResult(data_response)

    async def random_image(self, *, sfw: bool=True, nsfw: bool=False, get_bytes: bool=False):
        raise NotImplementedError()

        if not sfw and not nsfw:
            raise Exception()

        tags = []
        if sfw:
            sfw_tags = enumeration.SFWImageTags.to_list()
            tags.extend(sfw_tags)

        if nsfw:
            nsfw_tags = enumeration.NSFWImageTags.to_list()
            tags.extens(nsfw_tags)

        tag = random.choice(tags)

        if get_bytes:
            pass


    async def random_fact_text(self):
        """
        -> Coroutine
        Returns a random fact.

        Return
        -------
            anekos.result.TextResult
        """
        data_response = await self.http.endpoint("fact")
        return result.TextResult(data_response, target="fact")

    async def random_cat_text(self):
        """
        -> Coroutine
        Returns a random cat-like text.

        Return
        -------
            anekos.result.TextResult
        """
        data_response = await self.http.endpoint("cat")
        return result.TextResult(data_response, target="cat")

    async def random_why(self):
        """
        -> Coroutine
        Returns a random questionnaire.

        Return
        -------
            anekos.result.TextResult
        """
        data_response = await self.http.endpoint("why")
        return result.TextResult(data_response, target="why")

    #async def random_spoiler(self):
     #   return await self._get("spoiler")

    async def random_8ball(self, question, *, get_image_bytes: bool=False):
        """
        -> Coroutine
        Returns a random answer for the specified question.

        Return:
            anekos.result.EightBallResult
        """
        data_response = await self.http.endpoint("8ball")
        return result.EightBallResult(data_response)
