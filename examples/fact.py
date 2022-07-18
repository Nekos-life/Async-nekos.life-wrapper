from asyncio import get_event_loop

from anekos import NekosLifeClient

client = NekosLifeClient()


async def main():
    result = await client.random_fact_text()
    print(result.text)


loop = get_event_loop()
loop.run_until_complete(main())
