import discord, requests, json
from discord.ext import commands

bot = commands.Bot(command_prefix = "!!") # I just like this one better
token = "YOUR_TOKEN"

app_ids = {
    "chess": 832012774040141894,
    "fish": 814288819477020702,
    "poker": 755827207812677713,
    "yt": 755600276941176913,
    "betrayal": 773336526917861400
    }

def make(t, vcid):
    t = app_ids[t.lower()]
    url = f"https://discord.com/api/v9/channels/{vcid}/invites"
    body = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": f"{t}",
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    auth = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json",
        "X-Ratelimit-Precision": "millisecond"
    }

    obj = json.dumps(body, separators=(',', ':'), ensure_ascii=True)
    code = (requests.post(url, data = obj, headers = auth))
    code = json.loads(code.text)["code"]

    invite = f"https://discord.gg/{code}"
    return invite

@bot.event
async def on_ready():
    print("Online")

@bot.command()
async def play(ctx, game):
    try:
        voiceChannel = ctx.author.voice.channel
        if voiceChannel != None:
            await ctx.send(make(game, voiceChannel.id))
        else:
            await ctx.send("Connect to VC first")
    except:
        await ctx.send("Connect to VC first")
    
bot.run(token)
