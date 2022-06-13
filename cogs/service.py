import discord
from discord.ext import commands
from options import admin_id as administrator
import os
from time import time

class Service(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        st = time()
        message = await ctx.send(f"Понг! :ping_pong: Задержка: {self.bot.latency*1000:,.0f} ms.")
        end = time()
        await message.edit(content=f"Понг! :ping_pong: Задержка: {self.bot.latency*1000:,.0f} ms. Задержка DWSP: {(end-st)*1000:,.0f} ms.")

    @commands.command()
    async def avatar(self, ctx):
        author = ctx.message.author
        
        embed = discord.Embed(title=f"Аватарка {author}"[:-5],
                                color=discord.Color.dark_gray())
        link = author.avatar_url
        embed.set_image(url = link)

        await ctx.send(embed=embed)

    @commands.command()
    async def pateufeek(self, ctx):
        await ctx.message.delete()
        await ctx.send("https://media.discordapp.net/attachments/964614960325992478/982716016184410122/4c8de376-2ee8-4938-b3bb-38f51b823875-4.gif")

    @commands.command()
    async def hello(self, ctx):
        author = ctx.message.author
        await ctx.send(f'Привет, {author.mention}!')

    @commands.command(pass_context=True)
    async def say(self, ctx, arg):
        await ctx.send(arg)

    @commands.command()
    async def shutdown(self, ctx):
        if ctx.author.id == administrator:
            await ctx.send("Завершение работы... :wave:")
            os.abort()
        else:
            await ctx.send("Недостаточно прав для выполнения данной команды.")

def setup(bot):
    bot.add_cog(Service(bot))