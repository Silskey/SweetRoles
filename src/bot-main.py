import discord
from discord.ext import commands
TOKEN = '' #to make read venv for this

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True  
bot = commands.Bot(intents=intents)
discord.Permissions.all()
guildslist = bot.guilds

@bot.event
async def on_ready():
    print(f"Bot is logged in as {bot.user}")


@bot.slash_command(guild=guildslist, name="giverole",description="assigns a role to a given user")
@discord.option("user",type=discord.SlashCommandOptionType.user,required=True,description="the user to assign the role to")
@discord.option("role",type=discord.SlashCommandOptionType.role,required=True,description="the role to give the user")
async def giverole(ctx,user,role):
    await ctx.respond(f"trying to assign {role} to {user}")
    await user.add_roles(role,reason=f"{ctx.author} command call to add {role} to {user}")
    return 0

def get_similar_guilds(user):
    guilds =[]
    for guild in bot.guilds:
        if user in guild.members:
            guilds.append(guild)
    return guilds
def get_channels(guild):
    return guild.voice_channels



bot.run(TOKEN)





