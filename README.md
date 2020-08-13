# Async-nekos.life-wrapper
An official async wrapper for nekos.life API!

# Requirements
- [aiohttp](https://docs.aiohttp.org/en/stable/#library-installation) (>=3.6.2)

> The library below is just required if you want to save an image asynchronously
- [aiofile](https://pypi.org/project/aiofile/)

# Cool Features
- You can download the images!
- You can take a random image from SFW and/or NSFW tags!
- Easy to use with an object oriented design.

# Install
Installing is done purely via git:
```sh
python -m pip install -U git+https://github.com/Nekos-life/Async-nekos.life-wrapper
```

# Quick Example
```python
from anekos import NekosLifeClient, SFWImageTags
from asyncio import get_event_loop

client = NekosLifeClient()

async def main():
    result = await client.image(SFWImageTags.WALLPAPER)
    print(result.url)

loop = get_event_loop()
loop.run_until_complete(main())
```


