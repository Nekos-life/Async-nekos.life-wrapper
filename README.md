# Async-nekos.life-wrapper
Um wrapper assíncrono para a api nekos.life

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
