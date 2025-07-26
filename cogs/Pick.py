import discord
import random
import math
from discord.ext import commands
from Log import Log


class Pick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name='pick',
        aliases=['픽', '뽑']
    )
    async def pick_command(self, ctx):
        await Log(ctx, 'Call pick_memeber()')
        if not ctx.message.author.voice or not ctx.message.author.voice.channel:
            fail = 'not in voice channel'
            await Log(ctx, f'Failed pick_member() by {fail}')
            await ctx.message.reply(f'you are not {fail}')
            return
        
        voice_channel = ctx.message.author.voice.channel
        members = voice_channel.members
        
        if not members:
            fail = 'no members in voice channel'
            await Log(ctx, f'Failed pick_member() by {fail}')
            await ctx.message.reply(fail)
            return
        
        pick_count = ctx.message.content.split(maxsplit=1)
        if len(pick_count) < 2 or not is_inteager(pick_count[1]):
            fail = 'invalid parameter value (not inteager)'
            await Log(ctx, f'Failed pick_member() by {fail}')
            await ctx.message.reply(fail)
            return
        
        pick_count = int(pick_count[1])
        if(pick_count < 1):
            fail = 'invalid parameter value (out of range)'
            await Log(ctx, f'Failed pick_member() by {fail}')
            await ctx.message.reply(fail)
            return
        
        members_info = []
        for member in members:
            if member.bot:
                continue
            members_info.append(member.id)
        
        if(pick_count > len(members_info)):
            fail = 'invalid parameter value (out of range)'
            await Log(ctx, f'Failed pick_member() by {fail}')
            await ctx.message.reply(fail)
            return
        
        for i in range(0, 10):
            random.shuffle(members_info)
        
        picked_members = []
        for i in range(0, pick_count):
            picked_members.append(members_info[i])
           
        send_text = ''
        for member in picked_members:
            send_text += f'<@{member}>\n'
            
        embed = discord.Embed(title='Result')
        embed.add_field(name= 'Congratulations!', value= send_text)
        await ctx.message.channel.send(embed=embed)
        await Log(ctx, 'Success pick_member()')
        return    

    
    
        
async def setup(bot):
    await bot.add_cog(Pick(bot))
    
def is_inteager(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
