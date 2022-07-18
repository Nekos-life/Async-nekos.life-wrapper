from asyncio import get_event_loop

from anekos import NekosLifeClient

client = NekosLifeClient()

question = input(str('Question: '))


async def main():
    result = await client.random_8ball(question)
    print(result.text)


loop = get_event_loop()
loop.run_until_complete(main())
