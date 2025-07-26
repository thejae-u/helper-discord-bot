import discord
from datetime import datetime
from discord.ext import commands
from Log import Log
import qrcode
from PIL import Image
    
class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(
        name='ping',
        aliases=['핑', '지연시간']
    )
    async def ping_command(self, ctx):
        await Log(ctx, 'Call ping()')
        
        latency = self.bot.latency * 1000
        txt = str(round(latency, 3)) + ' ms'
        
        embed = discord.Embed(
            title='🏓 Pong!',
            description=f'**{txt}**',
            color=discord.Color.blue()
        )
        
        await ctx.reply(embed=embed)
        
    @commands.command(
        name='qrcode',
        aliases=['큐알', 'qr']
    )
    async def make_qr_command(self, ctx):
        await Log(ctx, 'Call make_qr()')
        try:
            before_qr = ctx.message.content.split(maxsplit=1)[1]
            img = qrcode.make(before_qr)
            img.save('qr_image/qrcode.png')
            img_file = discord.File('qr_image/qrcode.png', filename='send_image.png')
            await ctx.message.reply(file=img_file)
            await Log(ctx, 'Success make_qr()')
        except IndexError as e:
            await Log(ctx, f'Failed make_qr() by {e}')
            await ctx.message.add_reaction('❌')
        except Exception as e:
            await Log(ctx, f'Failed make_qr() by {e}')
            await ctx.message.add_reaction('❌')
        return
    
    @commands.command(
        name='serverinfo',
        aliases=['서버정보', '서버']
    )
    async def guild_info(self, ctx):
        guild = ctx.guild

        embed = discord.Embed(
            title=f'✨ {guild.name} 서버 정보 ✨',
            description=f'{guild.description or "서버 설명이 없습니다."}',
            color=discord.Color.blue()
        )

        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        embed.add_field(name='🆔 서버 ID', value=guild.id, inline=True)
        if guild.owner:
            embed.add_field(name='👑 소유자', value=guild.owner.mention, inline=True)
        else:
            embed.add_field(name='👑 소유자', value='', inline=True)

        embed.add_field(name='📅 생성일', value=guild.created_at.strftime("%Y년 %m월 %d일"), inline=True)
        
        embed.add_field(name='👥 총 멤버 수', value=f'{guild.member_count}명', inline=True)
        embed.add_field(name='🤖 봇 수', value=f'{len([m for m in guild.members if m.bot])}개', inline=True)
        embed.add_field(name='👤 사람 수', value=f'{len([m for m in guild.members if not m.bot])}명', inline=True)

        embed.add_field(name='📝 채널 수', value=f'{len(guild.channels)}개', inline=True)
        embed.add_field(name='🗣️ 텍스트 채널', value=f'{len(guild.text_channels)}개', inline=True)
        embed.add_field(name='🔊 음성 채널', value=f'{len(guild.voice_channels)}개', inline=True)

        embed.add_field(name='💎 부스트 레벨', value=f'레벨 {guild.premium_tier} ({guild.premium_subscription_count} 부스트)', inline=True)
        embed.add_field(name='🏷️ 역할 개수', value=f'{len(guild.roles)}개', inline=True)

        embed.set_footer(text=f'{self.bot.user.name} | 요청: {ctx.author.display_name}', icon_url=self.bot.user.avatar.url if self.bot.user.avatar else None)
        
        await ctx.reply(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Utility(bot))
    
    
