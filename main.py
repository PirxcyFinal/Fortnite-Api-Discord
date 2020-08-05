# Fortnite-Api-Discord github.com/BayGamerYT/Fortnite-Api-Discord | Coding UTF-8
print('Fortnite-Api-Discord | Made by BayGamerYT')
print('\nSupport Server: discord.gg/5TVU3n7')


import json, sys, os
try:
    from discord.ext import commands
    from threading import Thread
    from flask import Flask
    import aiohttp
    import discord
except:
    print(f'An error ocurred while trying to import third party library, run INSTALL.bat and try again!')
    sys.exit(1)

with open('config.json', 'r') as r:
    data = json.load(r)
    
if data['Api response lang'] == '':
    response_lang = 'en'
else:
    response_lang = data['Api response lang']
if data['Api request lang'] == '':
    request_lang = 'en'
else:
    request_lang = data['Api request lang']
if data['Prefix'] == '':
    P = 'f!'
else:
    P = data['Prefix']
if data['Token'] == '':
    error = 'You need to put your bot token in config.json file.'
    print(error)
    sys.exit(1)
else:
    T = data['Token']


bot = commands.Bot(command_prefix=P)

app=Flask("")

@app.route("/")
def index():
    return "<h1>Bot is running</h1>"


@bot.event
async def on_ready():
    print('\nBot Ready!\n')
    print(f'Name: {bot.user.name}#{bot.user.discriminator}')
    print(f'ID: {bot.user.id}\n')
    Thread(target=app.run,args=("0.0.0.0",8080)).start()


FORTNITE_API_BASE = 'https://fortnite-api.com/v2/'

async def fortnite_api_request(url: str, params: dict = {}) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.request(
                method='GET', url=f'{FORTNITE_API_BASE}{url}',
                params=params) as r:
            return await r.json()


@bot.command(pass_context=True)
async def brnews(ctx, l = None):
    """Show the current battle royale news"""

    res_lang = response_lang
    if l == None:
        res_lang = response_lang

    response = await fortnite_api_request(f'news/br?language={res_lang}')
        
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

    if args != None:
        response = await fortnite_api_request(f'cosmetics/br/search/all?name={joinedArgs}&matchMethod=starts&language={response_lang}&searchLanguage={request_lang}')

        if response['status'] == 200:

            embed_count=0
            item_left_count=0
            for item in response['data']:
                if embed_count != data['Max_Search_Results']:
                    embed_count+=1
                    item_id = item['id']
                    item_name = item['name']
                    item_description = item['description']
                    item_icon = item['images']['icon']
                    item_introduction = item['introduction']['text']
                    if item['set'] == None:
                        item_set = 'None'
                    else:
                        item_set = item['set']['text']

                    embed = discord.Embed(title=f'{item_name}')
                    embed.add_field(name='Description', value=f'``{item_description}``')
                    embed.add_field(name='ID', value=f'``{item_id}``')
                    embed.add_field(name='Introduction', value=f'``{item_introduction}``')
                    embed.add_field(name='Set', value=f'``{item_set}``')
                    embed.set_thumbnail(url=item_icon)
                    await ctx.send(embed=embed)
                else:
                    item_left_count+=1
            if item_left_count:
                max_srch = data['Max_Search_Results']
                await ctx.send(f'There are ``{item_left_count}`` more results but I\'m set to show ``{max_srch}``')

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
async def cc(ctx, code = None):
    """Search info for requested creator code"""
    if code is not None:

        response = await fortnite_api_request(f'creatorcode?name={code}')

        if response['status'] == 200:
            codeAcc = response['data']['account']['name']
            codeAccID = response['data']['account']['id']
            codestatus = response['data']['status']
            codeverified = response['data']['verified']

            embed = discord.Embed(title='Creator Code info', description=None)
            embed.add_field(name='Code', value=f'``{code}``', inline=True)
            embed.add_field(name='Account', value=f'``{codeAcc}``', inline=True)
            embed.add_field(name='Account ID', value=f'``{codeAccID}``')
            if codestatus == 'ACTIVE':
                embed.add_field(name='Status', value='``Active``', inline=True)
            else:
                embed.add_field(name='Status', value='``Inactive``', inline=True)
            
            if codeverified == True:
                embed.add_field(name='Verified?', value='``Yes``')
            else:
                embed.add_field(name='Verified?', value='``Yes``')

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

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'```\n{error}```')

try:
    bot.run(T)
except Exception as e:
    print(e)
    sys.exit(0)