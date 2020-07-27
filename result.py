from os.path import splitext, basename


class Result:
    def __init__(self, data: dict):
        self.endpoint = data.pop("endpoint")


class TextResult(Result):
    def __init__(self, data: dict, target: str="text"):
        super().__init__(data)

        self.text = data.pop(target)


class ImageResult(Result):
    def __init__(self, data: dict):
        super().__init__(data)
        
        self.url = url = data.pop("url")
        self.full_name = full_name = basename(url)
        self.name, self.extension = splitext(full_name)
        self.bytes = data.pop("bytes", None)


class EightBallResult(Result):
    def __init__(self, data: dict):
        super().__init__(data)

        self.text = data.pop("response")
        self.image_url = data.pop("url")
        self.image_bytes = data.pop("bytes", None)

