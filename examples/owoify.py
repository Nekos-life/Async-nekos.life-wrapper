from asyncio import get_event_loop

from anekos import NekosLifeClient

client = NekosLifeClient()

text = input(str('Text: '))


async def main():
    result = await client.owoify(text)
    print(result.text)


loop = get_event_loop()
loop.run_until_complete(main())
