from options import token as discordToken
from options import log_channel as logger
from options import admin_id as administrator
import discord
from discord.ext import commands
from bannedChannels import bannedChannels
from bannedUsers import bannedUsers
import os

intents = discord.Intents.default()
intents.members=True
intents.messages=True

bot = commands.Bot(command_prefix='!', case_insensitive=True)

@bot.event
async def on_ready():
    print("------")
    print("Bot is ready!")
    print(f"Logged in as: {bot.user.name}")
    print(f"Bot ID: {str(bot.user.id)}")
    for guild in bot.guilds:
        print(f"Connected to server: {guild}")
    print("------")
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Halo Infinite Battle Royale'))

@bot.event
async def on_message_delete(ctx):
    channel = bot.get_channel(logger)
    embed = discord.Embed(
        title = 'Удалённое сообщение',
        description = ctx.content,
        color = 0x209af8
    )
    embed.add_field(
        name = 'Автор',
        value = f'<@{ctx.author.id}>'
    )
    embed.add_field(
        name = 'Канал',
        value = f'<#{ctx.channel.id}>'
    )
    print(ctx.content)
    if (ctx.channel.id not in bannedChannels) and (ctx.author.id not in bannedUsers) and (str(ctx.content)[1:5] != 'poll')  and (not ctx.author.bot):
        await channel.send(embed = embed)
        
@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == administrator:
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send("Ког выгружается...")
    else:
        await ctx.send("Недостаточно прав для выполнения данной команды.")


@bot.command()
async def load(ctx, extension):
    if ctx.author.id == administrator:
        bot.load_extension(f"cogs.{extension}")
        await ctx.send("Ког запускается...")
    else:
        await ctx.send("Недостаточно прав для выполнения данной команды.")


@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == administrator:
        bot.unload_extension(f"cogs.{extension}")
        bot.load_extension(f"cogs.{extension}")
        await ctx.send("Ког перезапускается...")
    else:
        await ctx.send("Недостаточно прав для выполнения данной команды.")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')
    
bot.run(discordToken)