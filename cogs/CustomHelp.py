import discord
from discord.ext import commands
from Log import Log

# help commands
def ping_help(embed:discord.Embed):
    embed.add_field(name='!ping or !핑 or !지연시간', 
                    value='지연 시간을 알려줍니다',
                    inline=False)
    return embed

def pin_help(embed:discord.Embed):
    embed.add_field(name='!pin or !고정',
                    value='메시지를 고정 할 수 있습니다\n사용방벙 : !pin (고정할 메시지)',
                    inline=False)

def vote_help(embed:discord.Embed):
    embed.add_field(name='!찬반 투표 or !찬반',
                    value='찬반 투표를 할 수 있습니다',
                    inline=False)
    return embed

def pick_help(embed:discord.Embed):
    embed.add_field(name='!pick or !뽑',
                    value='!pick (인원수) 를 입력하면 음성 채널에 있는 인원 중 인원 수 만큼 뽑습니다 (봇 제외)',
                    inline=False)
    return embed
    
def qr_help(embed:discord.Embed):
    embed.add_field(name='!qrcode or !큐알',
                    value='!qrcode (문자열) 을 입력하면 QR 코드 이미지를 생성합니다.',
                    inline=False)
    return embed

class CustomHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(
        name='help',
        aliases=['도움말', '헬프']
    )
    async def help_command(self, ctx):
        await Log(ctx, 'Call help()')
        
        embed = discord.Embed(title='How to Use')
        ping_help(embed)
        qr_help(embed)
        vote_help(embed)
        pick_help(embed)
        
        try:
            dm = await ctx.message.author.create_dm()
            await dm.send(embed=embed)
        except Exception as e:
            await Log(ctx, f'Failed help() by {e}')
            return
        
        await Log(ctx, f'Success help()')
        
async def setup(bot):
    await bot.add_cog(CustomHelp(bot))
        