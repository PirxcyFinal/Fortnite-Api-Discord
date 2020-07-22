import json, sys, os
try:
    from discord.ext import commands
    import discord
except:
    print(f'An error ocurred while trying to import third party library, run INSTALL.bat and try again!')
    sys.exit(1)

with open('config.json', 'r') as r:
    data = json.load(r)

P = data['Prefix']
bot = commands.Bot(command_prefix=P)

@bot.event
async def on_ready():
    print('\nBot Ready!\n')
    print(f'Name: {bot.user.name}#{bot.user.discriminator}')
    print(f'ID: {bot.user.id}\n')


FORTNITE_API_BASE = 'https://fortnite-api.com/v2/'

async def fortnite_api_request(url: str, params: dict = {}) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.request(
                method='GET', url=f'{FORTNITE_API_BASE}{url}',
                params=params) as r:
            return await r.json()


@bot.command(pass_context=True)
async def brnews(ctx, lang = 'en'):
    """Show the current battle royale news"""

    response = await fortnite_api_request(f'news/br?language={lang}')

    if response['status'] == 200:

        image = response['data']['image']

        embed = discord.Embed(title='Battle Royale News', description=None)
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    elif response['status'] == 400:

        error = response['error']

        embed = discord.Embed(title='Error', 
        description=f'``{error}``')

        await ctx.send(embed=embed)

    elif response['status'] == 404:

        error = response['error']

        embed = discord.Embed(title='Error', 
        description=f'``{error}``')

        await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def item(ctx, *args):
    """Search info for entered item name"""
    joinedArgs = ('+'.join(args))

    if joinedArgs == None:
        await ctx.send(f'Usage: ``{P}id <item name>``')
        
    else:
        response = await fortnite_api_request(f'cosmetics/br/search?name={joinedArgs}&matchMethod=contains')

        if response['status'] == 200:

            itemName = response['data']['name']
            itemID = response['data']['id']
            itemDesc = response['data']['description']
            itemImage = response['data']['images']['icon']


            embed = discord.Embed(title=f'**{itemName}**', description=None)
            embed.add_field(name='ID', value=f'``{itemID}``')
            embed.add_field(name='ID', value=f'``{itemDesc}``')
            embed.set_thumbnail(url=itemImage)

            await ctx.send(embed=embed)

        elif response['status'] == 400:

            error = response['error']

            embed = discord.Embed(title='Error', 
            description=f'``{error}``')

            await ctx.send(embed=embed)

        elif response['status'] == 404:

            error = response['error']

            embed = discord.Embed(title='Error', 
            description=f'``{error}``')

            await ctx.send(embed=embed)



T = data['Token']

try:
    bot.run(T)
except Exception as e:
    print(e)
    sys.exit(0)