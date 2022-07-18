from asyncio import get_event_loop

from anekos import NekosLifeClient, SFWImageTags

client = NekosLifeClient()


async def main():
    result = await client.image(SFWImageTags.WALLPAPER)
    print(result.url)


loop = get_event_loop()
loop.run_until_complete(main())
