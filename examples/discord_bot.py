import discord
from discord.ext import commands

from anekos import NekosLifeClient, SFWImageTags

bot = commands.AutoShardedBot(commands.when_mentioned_or('!'), allowed_mentions=None)
client = NekosLifeClient()


@bot.event
async def on_ready():
    print(bot.user.name)


@bot.command()
async def kiss(ctx, user: discord.Member = None):
    if user == ctx.author or user is None:
        await ctx.reply('Mention someone!')
    else:
        img = await client.image(SFWImageTags.KISS)
        await ctx.reply(img.url)


@bot.command(name='8ball')
async def eightball(ctx, *, question: str):
    ball = await client.random_8ball(question)
    await ctx.reply(ball.text)


@bot.command()
async def fact(ctx):
    fact = await client.random_fact_text()
    await ctx.reply(fact.text)


@bot.command()
async def owoify(ctx, *, text: str):
    owo = await client.owoify(text)
    await ctx.reply(owo.text)


bot.run('TOKEN')
