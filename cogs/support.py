import discord
from discord.ext import commands
from options import admin_role_id, mod_role_id, admin_channel
from time import sleep
import os

class Support(commands.Cog):
    def __init__(self, bot):
        self.Bot = bot

    @commands.slash_command(description='Отправить Тикет')
    async def ticket(self, ctx, text):
        embed = discord.Embed(
            description=f'**<@{ctx.author.id}> открывает Тикет**\n**Причина:** {text}\n**В канале:** <#{ctx.channel.id}>',
            color=0x209af8
        )
        name = 'Тикеты'
        category = discord.utils.get(ctx.guild.categories, name=name)
        channel = await ctx.guild.create_text_channel(f'тикет-<@{ctx.author.name}>', topic=text, category=category)
        await channel.set_permissions(ctx.author,speak=True,send_messages=True,read_message_history=True,read_messages=True)
        await channel.send(f'<@&{mod_role_id}>ы, надо обкашлять пару вопросиков.', embed=embed)
        await channel.send(f'<@{ctx.author.id}>, вам слово.')
        embed = discord.Embed(description='Ваш Тикет был успешно отправлен!', color = 0x209af8)        
        await ctx.respond(embed = embed, delete_after=5.0)
    
    @commands.slash_command(description='Добавить пользователя в Тикет')
    async def adduser(self, ctx, user: discord.Member):
        if ctx.channel.category_id == 1006910617833177118:
            await ctx.channel.set_permissions(user,speak=True,send_messages=True,read_message_history=True,read_messages=True)
            await ctx.respond(f'<@{user.id}>, вас добавили в чат Тикета для решения вопроса.')
        else:
            await ctx.respond('Не сюда', delete_after = 5.0)
            
    @commands.slash_command(description='Удалить Тикет')
    async def deleteticket(self, ctx):
        if ctx.channel.category_id == 1006910617833177118:
            embed = discord.Embed(description='Удаление Тикета через 10 секунд.', color=0x209af8)
            await ctx.respond(embed=embed)
            sleep(10)
            filename=f'{ctx.channel.name}.txt'
            with open(filename, "w") as file:
                async for msg in ctx.channel.history(limit=None):
                    file.write(f"{msg.created_at} - {msg.author.display_name}: {msg.clean_content}\n")
            channel = self.Bot.get_channel(admin_channel)
            await channel.send(f'{ctx.channel.name} закрыт.', file=discord.File(filename))
            os.remove(filename)
            await ctx.channel.delete()
        else:
            await ctx.respond('Не сюда', delete_after = 5.0)
        
def setup(bot):
    bot.add_cog(Support(bot))