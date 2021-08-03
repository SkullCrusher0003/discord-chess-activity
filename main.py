import discord, requests, json
from discord.ext import commands

bot = commands.Bot(command_prefix = "sc!")

@bot.event
async def on_ready():
    print("Online")

@bot.command()
async def chess(ctx):
    try:
        voiceChannel = ctx.author.voice.channel
        if voiceChannel != None:
            url = f"https://discord.com/api/v9/channels/{voiceChannel.id}/invites"
            body = {
                "max_age": 1800,
                "max_uses": 0,
                "target_application_id": "832012774040141894",
                "target_type": 2,
                "temporary": False,
                "validate": None
            }
            auth = {
                "Authorization": "Bot TOKEN_HERE",
                "Content-Type": "application/json",
                "X-Ratelimit-Precision": "millisecond"
            }

            obj = json.dumps(body, separators=(',', ':'), ensure_ascii=True)
            code = (requests.post(url, data = obj, headers = auth))
            code = json.loads(code.text)["code"]
            invite = f"https://discord.gg/{code}"
            await ctx.send(invite)
        else:
            await ctx.send("Connect to VC first")
    except:
        await ctx.send("Connect to VC first")

bot.run("TOKEN_HERE")
