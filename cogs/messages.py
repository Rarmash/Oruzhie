import json
import discord
from discord.ext import commands
from options import admin_role_id, insider_id

messageCount = json.load(open('data.json', 'r'))

class MessagesCounter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, ctx):
        with open('data.json', 'r') as file:
            messageCount = json.load(file)
            author = str(ctx.author.id)
        if author in messageCount:
            messageCount[author] += 1
        else:
            messageCount[author] = 1
        with open('data.json', 'w') as update_file:
            json.dump(messageCount, update_file, indent=4)
                

    @commands.command()
    async def leaderboard(self, ctx, guild: discord.Guild = None):
        guild = guild or ctx.guild
        with open('data.json', 'r') as file:
            leaderboard = json.load(file)
        user_ids = list(leaderboard.keys())
        user_message_counts = list(leaderboard.values())
        new_leaderboard = []
        for index, user_id in enumerate(user_ids, 1):
            new_leaderboard.append([user_id, user_message_counts[index - 1]])
        new_leaderboard.sort(key=lambda items: items[1], reverse=True)
        desk = ''
        kolvo = 0
        print(type(new_leaderboard))
        for users in new_leaderboard:
            desk+=f'<@{users[0]}>: {users[1]}\n'
            kolvo+=int(users[1])
        embed = discord.Embed(title = 'Лидеры по сообщениям', description=desk, color = 0x209af8)
        #embed.set_thumbnail(url=guild.icon_url)
        embed.set_footer(text=f"Всего отправлено {kolvo} сообщений")
        if discord.utils.get(ctx.guild.roles, id=admin_role_id) in ctx.author.roles or discord.utils.get(ctx.guild.roles, id=insider_id) in ctx.author.roles:
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(MessagesCounter(bot))