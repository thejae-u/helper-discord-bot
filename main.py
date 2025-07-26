import discord
from discord.ext import commands
import os
import Data as DT

# 봇의 접두사 설정
COMMAND_PREFIX = '!'

# Intents 설정
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True

# commands.Bot 인스턴스 생성
bot_activity = discord.Game(name='ask me everyting')
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents, activity=bot_activity, help_command=None)

@bot.event
async def on_ready():
    print(f'봇이 로그인했습니다: {bot.user.name}')
    print(f'명령어 접두사: {COMMAND_PREFIX}')
    await load_extensions()
    
async def load_extensions():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            extension = 'cogs.' + filename[:-3]
            await bot.load_extension(extension)

bot.run(DT.TOKEN)