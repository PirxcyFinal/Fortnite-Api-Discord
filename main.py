# Fortnite-Api-Discord github.com/BayGamerYT/Fortnite-Api-Discord | Coding UTF-8
print('Fortnite-Api-Discord | Made by BayGamerYT')
import json, os


def data():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def text():
    try:
        with open(f'lang/{data()["bot_lang"]}.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        print('Invalid lang in settings')
        exit()


try:
    from discord.ext import commands
    from threading import Thread
    from flask import Flask
    import requests
    import aiohttp
    import discord
except:
    print(text()['module_not_found_error'])
    exit()
    

response_lang = 'en' if data()['Response lang'] == '' else data()['Response lang']
request_lang = 'en' if data()['Search lang'] == '' else data()['Search lang']

T = os.getenv('Token') if data()['Token'] == 'ENV' else data()['Token']


bot = commands.Bot(command_prefix=data()['Prefix'])


app=Flask("")
@app.route("/")
def index():
    return "Running"


@bot.event
async def on_ready():
    print('\n' + text()['bot_ready'])
    print(text()['name'] + f': {bot.user.name}#{bot.user.discriminator}')
    print(f'ID: {bot.user.id}\n')
    Thread(target=app.run,args=("0.0.0.0",8080)).start()



@bot.command(pass_context=True)
async def brnews(ctx, l = None):
    res_lang = response_lang
    if l == None:
        res_lang = response_lang

    response = requests.get(f'https://fortnite-api.com/v2/news/br?language={res_lang}')

    geted = response.json()
        
    if response.status_code == 200:

        image = geted['data']['image']

        embed = discord.Embed(title=text()['br_news'])
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    elif response.status_code == 400:
 
        error = geted['error']

        embed = discord.Embed(title='Error', 
                description=f'`{error}`')

        await ctx.send(embed=embed)

    elif response.status_code == 404:

        error =geted['error']

        embed = discord.Embed(title='Error', 
        description=f'``{error}``')

        await ctx.send(embed=embed)

def color(value):
    if value == 'legendary':
        return 0xf0b132
    elif value == 'epic':
        return 0x9d4dbb
    elif value == 'rare':
        return 0x0086FF
    elif value == 'uncommon':
        return 0x65b851
    elif value == 'common':
        return 0x575757
    elif value == 'icon':
        return 0x00FFFF
    elif value == 'marvel':
        return 0xED1D24
    elif value == 'shadow':
        return 0x292929
    elif value == 'dc':
        return 0x2b3147
    elif value == 'slurp':
        return 0x09E0F0
    elif value == 'dark':
        return 0xFF00FF
    elif value == 'frozen':
        return 0x93F7F6
    elif value == 'lava':
        return 0xF55F35
    elif value == 'starwars':
        return 0xCCCC00
    else:
        return 0xffffff

@bot.command(pass_context=True)
async def item(ctx, *args):
    joinedArgs = ('+'.join(args))

    if args != None:
        response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search/all?name={joinedArgs}&matchMethod=starts&language={response_lang}&searchLanguage={request_lang}')

        geted = response.json()

        if response.status_code == 200:

            embed_count=0
            item_left_count=0

            for item in geted['data']:

                if embed_count != data()['Max_Search_Results']:

                    embed_count+=1
                    item_id = item['id']
                    item_name = item['name']
                    item_description = item['description']
                    item_icon = item['images']['icon']
                    item_introduction = item['introduction']['text']
                    item_rarity = item['rarity']['displayValue']

                    if item['set'] == None:
                        item_set = text()['none']
                    else:
                        item_set = item['set']['text']

                    name = text()['name']
                    desc = text()['description']
                    intro = text()['introduction']
                    of_set = text()['set']
                    txt_id = text()['id']
                    rarity = text()['rarity']


                    embed = discord.Embed(title=f'{item_name}', color=color(item['rarity']['value']))

                    embed.add_field(name=desc, value=f'`{item_description}`')
                    embed.add_field(name=txt_id, value=f'`{item_id}`')
                    embed.add_field(name=intro, value=f'`{item_introduction}`')
                    embed.add_field(name=of_set, value=f'`{item_set}`')
                    embed.add_field(name=rarity, value=f'`{item_rarity}`')
                    embed.set_thumbnail(url=item_icon)

                    await ctx.send(embed=embed)

                else:
                    item_left_count+=1
            if item_left_count:
                max_srch = data()['Max_Search_Results']
                mx_txt = text()['max_results_exceed_text']
                await ctx.send(mx_txt.format(item_left_count, max_srch))

        elif response.status_code == 400:
            error = geted['error']

            embed = discord.Embed(title='Error', 
            description=f'``{error}``')

            await ctx.send(embed=embed)

        elif response.status_code == 404:
            error = geted['error']

            embed = discord.Embed(title='Error', 
            description=f'``{error}``')

            await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def cc(ctx, code = None):
    if code != None:

        response = requests.get(f'https://fortnite-api.com/v2/creatorcode?name={code}')
        geted = response.json()

        if response.status_code == 200:

            codeAcc =geted['data']['account']['name']
            codeAccID =geted['data']['account']['id']
            codestatus =geted['data']['status']
            codeverified =geted['data']['verified']

            code = text()['code']
            account = text()['account']
            text_id = text()['id']
            active = text()['active']
            inactive = text()['inactive']
            verified_bool = text()['verified_bool']
            account_id = text()['account_id']
            yes = text()['text_yes']
            no = text()['text_no']
            status = text()['status']

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
        
        elif response.status_code == 400:

            error = geted['error']

            embed = discord.Embed(title='Error', 
            description=f'``{error}``')

            await ctx.send(embed=embed)

        elif response.status_code == 404:

            error = geted['error']

            embed = discord.Embed(title='Error', 
            description=f'``{error}``')

            await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(text()['command_not_found_error'])
    else:
        raise error
    

try:
    bot.run(T)
except Exception as e:
    print(e)
    exit()