# Async-nekos.life-wrapper
Um wrapper assíncrono para a api nekos.life

# Requirements
- [aiohttp](https://docs.aiohttp.org/en/stable/#library-installation) (>=3.6.2)

# Install
Installing is done purely via git:
```python
python -m pip install -U git+https://github.com/Rapptz/discord-ext-menus
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


