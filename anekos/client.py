import typing

from . import http_client, enumeration, result

Tag = typing.Union[str, enumeration.SFWImageTags, enumeration.NSFWImageTags]


class NekosLifeClient:
    def __init__(self, *, session=None):
        self.http = http_client.HttpClient(session=session)

    async def image(self, tag: Tag, get_bytes: bool=False):
        """
        -> Coroutine

        Parameters
        ----------
        tag : Union[str, anekos.SFWImageTags, anekos.NSFWImageTags]
            The tag of image.

        get_bytes : bool (optional)
            Gets the byte of image.
            You can take the bytes in `bytes` attribute of object returned.

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

    async def random_fact_text(self):
        data_response = await self.http.endpoint("fact")
        return result.TextResult(data_response, target="fact")

    async def random_cat_text(self):
        data_response = await self.http.endpoint("cat")
        return result.TextResult(data_response, target="cat")

    async def random_why(self):
        data_response = await self.http.endpoint("why")
        return result.TextResult(data_response, target="why")

    #async def random_spoiler(self):
     #   return await self._get("spoiler")

    async def random_8ball(self, *, get_image_bytes: bool=False):
        data_response = await self.http.endpoint("why")
        return result.EightBallResult(data_response)
