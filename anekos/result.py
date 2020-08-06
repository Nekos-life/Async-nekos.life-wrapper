from os.path import splitext, basename, join

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
        endpoint : :class:`str`
            The endpoint in which the result was returned.
    """
    def __init__(self, data: dict):
        self.endpoint = data.pop("endpoint")


class TextResult(Result):
    """
    Structure used for endpoints that return texts.

    Attributes
    ----------
        endpoint : :class:`str`
            The endpoint in which the result was returned.

        text : :class:`str`
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
        endpoint : :class:`str`
            The endpoint in which the result was returned.

        url : :class:`str`
            Image URL.

        full_name : :class:`str`
            Full image name.

        name : :class:`str`
            Image name (without the extension).

        extension : :class:`str`
            Image extension (PNG, JPG, ...).

        bytes : :class:`bytes`
            Image in bytes, it can be `None`.
    """
    def __init__(self, data: dict):
        super().__init__(data)
        
        self.url = url = data.pop("url")
        self.full_name = full_name = basename(url)
        self.name, self.extension = splitext(full_name)
        self.bytes = data.pop("bytes", None)

    def sync_save(self, path: str):
        """Saves the image in `path`.

        THIS FUNCTION CAN "LOCK" YOUR CODE.
        TRY USE `SAVE` METHOD INSTEAD.

        Parameters
        ----------
            path : str
                The path there image will be saved.
        """
        path = join(path, self.full_name)
        with open(path, "wb") as file:
            file.write(self.bytes)

    def sync_download(self, path: str):
        """Alias for `sync_save` method."""
        return self.sync_save()

    async def save(self, path: str):
        """Saves the image in the `path`.

        THE `aiofile` LIBRARY IS NEEDED IN ORDER TO USE THIS METHOD.
        USE `sync_save` IF YOU DO NOT WANT TO INSTALL THE `aiofile` LIBRARY.

        Parameters
        ----------
            path : str
                The path where the image will be saved.
        """
        if not has_aiofile:
            raise RuntimeError("aiofile library is needed in order to use this method.")

        path = join(path, self.full_name)
        async with AIOFile(path, "wb") as file:
            await file.write(self.bytes)

    async def download(self, path: str):
        """Alias for `save` method."""
        return await self.save(path)


class EightBallResult(Result):
    """
    Structure used for the endpoint `/8ball`
    
    Attributes
    ----------
        endpoint : :class:`str`
            The endpoint in which the result was returned.

        text : :class:`str`
            The returned text.

        image_url : :class:`str`:
            Returned image URL.

        image_bytes : :clasS:`bytes`
            Image in bytes, it can be `None`.
    """
    def __init__(self, data: dict):
        super().__init__(data)

        self.text = data.pop("response")
        self.image_url = data.pop("url")
        self.image_bytes = data.pop("bytes", None)

