from os.path import splitext, basename, join

#from .enumeration import SFWImageTags, NSFWImageTags

try:
    from aiofile import AIOFile
except ModuleNotFoundError:
    has_aiofile = False
else:
    has_aiofile = True


class Result:
    """
    Base structure for API returns.

    Attributes
    ----------
    endpoint : str
        The endpoint in which the result was returned.
    """
    def __init__(self, data: dict):
        self.endpoint = data.pop("endpoint")


class TextResult(Result):
    """
    Structure used for endpoints that return texts.

    Attributes
    ----------
    endpoint : str
        The endpoint in which the result was returned.
    text : str
        The returned text.
    """
    def __init__(self, data: dict, target: str="text"):
        super().__init__(data)

        self.text = data.pop(target)


class ImageResult(Result):
    """
    Structure used for endpoints that return images.

    Attributes
    ----------
    endpoint : str
        The endpoint in which the result was returned.
    url : str
        Image URL.
    full_name : str
        Full image name.
    name : str
        Image name (without the extension).
    extension : str
        Image extension (PNG, JPG, ...).
    tag : Union[str, anekos.NSFWImageTags, anekos.SFWImageTags]
    bytes : bytes
        Image in bytes, it can be `None`.
    """
    def __init__(self, data: dict):
        super().__init__(data)
        
        self.url = url = data.pop("url")
        self.full_name = full_name = basename(url)
        self.name, self.extension = splitext(full_name)
        self.tag = data.pop("tag")
        self.bytes = data.pop("bytes", None)

    def sync_save(self, path: str):
        """Saves the image in `path`.

        Parameters
        ----------
        path : str
            The path there image will be saved.

        Notes
        -----
        THIS FUNCTION CAN "LOCK" YOUR CODE.
        TRY USE `save` METHOD INSTEAD.
        """
        path = join(path, self.full_name)
        with open(path, "wb") as file:
            try:
                file.write(self.bytes)
            except TypeError:
                raise RuntimeError("you need to get the image bytes to use this method")

    def sync_download(self, path: str):
        """Alias for `sync_save` method."""
        return self.sync_save()

    async def save(self, path: str):
        """Saves the image in the `path`.

        Parameters
        ----------
        path : str
            The path where the image will be saved.

        Notes
        -----
        THE `aiofile` LIBRARY IS NEEDED IN ORDER TO USE THIS METHOD.
        USE `sync_save` IF YOU DO NOT WANT TO INSTALL THE `aiofile` LIBRARY.
        """
        if not has_aiofile:
            raise RuntimeError("aiofile library is needed in order to use this method.")

        path = join(path, self.full_name)
        async with AIOFile(path, "wb") as file:
            try:
                await file.write(self.bytes)
            except ValueError:
                raise RuntimeError("you need to get the image bytes to use this method")

    async def download(self, path: str):
        """Alias for `save` method."""
        return await self.save(path)


class EightBallResult(Result):
    """
    Structure used for the endpoint `/8ball`

    Attributes
    ----------
    endpoint : str
        The endpoint in which the result was returned.
    text : str
        The returned text.
    image_url : str
        Returned image URL.
    image_bytes : bytes
        Image in bytes, it can be `None`.
    """
    def __init__(self, data: dict):
        super().__init__(data)

        self.text = data.pop("response")
        self.image_url = data.pop("url")
        self.image_bytes = data.pop("bytes", None)

