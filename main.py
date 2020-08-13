# Fortnite-Api-Discord github.com/BayGamerYT/Fortnite-Api-Discord | Coding UTF-8
print('Fortnite-Api-Discord | Made by BayGamerYT')
print('Support Server: discord.gg/5TVU3n7')
import json, sys, os

if sys.platform == 'win32':
    os.system("py -3 -m pip install -U -r requirements.txt")
else:
    os.system("pip install -U -r requirements.txt")

with open('config.json', 'r') as r:
    data = json.load(r)

if data['bot_lang'] == 'en':
    with open('lang/en.json', 'r', encoding='utf-8') as txt:
        text = json.load(txt)

elif data['bot_lang'] == 'es':
    with open('lang/es.json', 'r', encoding='utf-8') as txt:
        text = json.load(txt)

try:
    from discord.ext import commands
    from threading import Thread
    from flask import Flask
    import aiohttp
    import discord
except:
    print(text['module_not_found'])
    sys.exit(1)
    

if data['Search lang'] == '':
    response_lang = 'en'
else:
    response_lang = data['Search lang']

if data['Request lang'] == '':
    request_lang = 'en'
else:
    request_lang = data['Request lang']


if data['Prefix'] == '':
    P = 'f!'
else:
    P = data['Prefix']
if data['Token'] == '':
    error = text['token_not_set_error']
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
    print('\n' + text['bot_ready'])
    print(text['name'] + f': {bot.user.name}#{bot.user.discriminator}')
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
    res_lang = response_lang
    if l == None:
        res_lang = response_lang

    response = await fortnite_api_request(f'news/br?language={res_lang}')
        
    if response['status'] == 200:

        image = response['data']['image']

        embed = discord.Embed(title=text['br_news'], description=None)
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
                        item_set = text['none']
                    else:
                        item_set = item['set']['text']

                    name = text['name']
                    desc = text['description']
                    intro = text['introduction']
                    of_set = text['set']
                    txt_id = text['id']

                    embed = discord.Embed(title=f'{item_name}')
                    embed.add_field(name=desc, value=f'``{item_description}``')
                    embed.add_field(name=txt_id, value=f'``{item_id}``')
                    embed.add_field(name=intro, value=f'``{item_introduction}``')
                    embed.add_field(name=of_set, value=f'``{item_set}``')
                    embed.set_thumbnail(url=item_icon)
                    await ctx.send(embed=embed)
                else:
                    item_left_count+=1
            if item_left_count:
                max_srch = data['Max_Search_Results']
                mx_txt = text['max_results_exceed_text']
                await ctx.send(mx_txt.format(item_left_count, max_srch))

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
    if code is not None:

        response = await fortnite_api_request(f'creatorcode?name={code}')

        if response['status'] == 200:
            codeAcc = response['data']['account']['name']
            codeAccID = response['data']['account']['id']
            codestatus = response['data']['status']
            codeverified = response['data']['verified']

            code = text['code']
            account = text['account']
            text_id = text['id']
            active = text['active']
            inactive = text['inactive']
            verified_bool = text['verified_bool']
            account_id = text['account_id']
            yes = text['text_yes']
            no = text['text_no']
            status = text['status']

            embed = discord.Embed(title='Creator Code info', description=None)
            embed.add_field(name=code, value=f'``{code}``', inline=True)
            embed.add_field(name=account, value=f'``{codeAcc}``', inline=True)
            embed.add_field(name=account_id, value=f'``{codeAccID}``')
            if codestatus == 'ACTIVE':
                embed.add_field(name=status, value=f'``{active}``', inline=True)
            else:
                embed.add_field(name=status, value=f'``{inactive}``', inline=True)
            
            if codeverified == True:
                embed.add_field(name=verified_bool, value=f'``{yes}``')
            else:
                embed.add_field(name=verified_bool, value=f'``{no}``')

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
    
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(text['command_not_found_error'])
    else:
        raise error

try:
    bot.run(T)
except Exception as e:
    print(e)
    sys.exit(0)