# Fortnite-Api-Discord github.com/BayGamerYT/Fortnite-Api-Discord | Coding UTF-8
"""
MIT License

Copyright (c) 2020 BayGamerYT

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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

P = data['Prefix']
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

    if args == None:
        await ctx.send(f'Usage: ``{P}id <item name>``')
        
    else:
        response = await fortnite_api_request(f'cosmetics/br/search?name={joinedArgs}&matchMethod=contains')

        if response['status'] == 200:

            itemName = response['data']['name']
            itemID = response['data']['id']
            itemDesc = response['data']['description']
            itemImage = response['data']['images']['icon']
            itemIntroduction = response['data']['introduction']['text']

            embed = discord.Embed(title=f'**{itemName}**', description=None)
            embed.add_field(name='ID', value=f'``{itemID}``')
            embed.add_field(name='Description', value=f'``{itemDesc}``')
            embed.add_field(name='Introduction', value=f'``{itemIntroduction}``')
            try:
                itemSet = response['data']['set']['text']
                embed.add_field(name='Set', value=f'``{itemSet}``')
            except:
                embed.add_field(name='Set', value=f'``None``')

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


T = data['Token']

try:
    bot.run(T)
except Exception as e:
    print(e)
    sys.exit(0)