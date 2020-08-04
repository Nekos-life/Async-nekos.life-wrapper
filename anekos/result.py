from os.path import splitext, basename


class Result:
    """
    Base structure for API returns.
    
    Attributes:
        endpoint (str): The endpoint in which the result was returned.
    """
    def __init__(self, data: dict):
        self.endpoint = data.pop("endpoint")


class TextResult(Result):
    """
    Structure used for endpoints that return texts.
    
    Attributes:
        endpoint (str): The endpoint in which the result was return.
        text (str): The returned text.
    """
    def __init__(self, data: dict, target: str="text"):
        super().__init__(data)

        self.text = data.pop(target)


class ImageResult(Result):
    """
    Structure used for endpoints that return images.
    
    Attributes:
        endpoint (str): The endpoint in which the result was returned.
        url (str): Image URL.
        full_name (str): Full image name.
        name (str): Image name (without the extension).
        extension (str): Image extension.
        bytes (str): Image in bytes, it can be `None`.
    """
    def __init__(self, data: dict):
        super().__init__(data)
        
        self.url = url = data.pop("url")
        self.full_name = full_name = basename(url)
        self.name, self.extension = splitext(full_name)
        self.bytes = data.pop("bytes", None)


class EightBallResult(Result):
    """
    Structure used for the endpoint `/8ball`
    
    Attributes:
        endpoint (str): The endpoint in which the result was returned.
        text (str): The returned text.
        image_url (str): Returned image URL.
        image_bytes (bytes): Image in bytes, it can be `None`.
    """
    def __init__(self, data: dict):
        super().__init__(data)

        self.text = data.pop("response")
        self.image_url = data.pop("url")
        self.image_bytes = data.pop("bytes", None)

