import requests
import json
import discord
import random
import math
import qrcode
import Data as dt
import Help as hp
from Log import Log
from notion_client import Client

# check latency Begin
async def ping(message, client):
    await Log(message, 'Call ping()')
    latency = client.latency * 1000
    txt = str(round(latency, 3)) + ' ms'
    embed = discord.Embed(title='Pong!', description=txt)
    await message.reply(embed=embed)

# check latency End

# vote positive or negative Begin
async def pn_vote(message):
    await Log(message, 'Call pn_vote()')
    embed = discord.Embed(title='찬반 투표', description='원하는 곳에 투표하세요')
    msg = await message.channel.send(embed=embed)
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')

# vote positive or negative End
    
# voice channel team made (only 2 team) Begin
async def make_team(message, client):
    await Log(message, 'Call make_team()')
    if not message.author.voice or not message.author.voice.channel:
        fail = 'not in voice channel'
        await Log(message, f'Failed make_team() by {fail}')
        await message.reply(f'you are {fail}')
        return
    voice_channel = message.author.voice.channel
    members = voice_channel.members
        
    if not members:
        fail = 'no members in voice channel'
        await Log(message, f'Failed make_team() by {fail}')
        await message.reply(fail)
        return
    
    member_info = []
    for member in members:
        if member.bot:
            continue
        member_info.append(member.id)
    
    if len(member_info) <= 1:
        fail = 'not enough members'
        await Log(message, f'Failed make_team() by {fail}')
        await message.reply(fail)
        return
            
    for i in range(random.randrange(0, 10)): 
        random.shuffle(member_info)
            
    team1 = []
    team2 = []
    count = len(member_info)

    for i in range(0, math.ceil(count / 2)):
        team1.append(member_info[i])
            
    for i in range(math.ceil(count / 2), count):
        team2.append(member_info[i])
            
    embed = discord.Embed(title= 'Result')
            
    team1_result = ''
    team2_result = ''
    count = 1
    for member in team1:
        team1_result += f'{count} : <@{member}>\n'
        count += 1

    count = 1
    for member in team2:
        team2_result += f'{count} : <@{member}>\n'
        count += 1
                

    embed.add_field(name='team 1', value= team1_result)
    embed.add_field(name='team 2', value= team2_result, inline=False)
    await message.channel.send(embed=embed)
    await Log(message, 'Success make_team()')
    return

# voice channel team made (only 2 team) End

async def count_voice_member(message):
    await Log(message, 'Call count_voice_memeber()')
    if not message.author.voice or not message.author.voice.channel:
        fail = 'not in voice channel'
        await Log(message, f'Failed count_voice_member() by {fail}')
        await message.reply(f'you are {fail}')
        return
    
    voice_channel = message.author.voice.channel
    members = voice_channel.members

    if not members:
        fail = 'no members in voice channel'
        await Log(message, f'Failed count_voice_member() by {fail}')
        await message.reply(fail)
        return
    members_info = []
    for member in members:
        if member.bot:
            continue
        members_info.append(member)
    
    await message.reply(f'현재 {len(members_info)}명이 {voice_channel.name}에 있습니다.')
    await Log(message, 'Success count_voice_member()')
    return
   
# member draw lots Begin
async def pick_member(message):
    await Log(message, 'Call pick_member()')
    if not message.author.voice or not message.author.voice.channel:
        fail = 'not in voice channel'
        await Log(message, f'Failed pick_member() by {fail}')
        await message.reply(f'you are {fail}')
        return

    voice_channel = message.author.voice.channel
    members = voice_channel.members

    if not members:
        fail = 'no members in voice channel'
        await Log(message, f'Failed pick_member() by {fail}')
        await message.reply(fail)
        return 
    
    pick_count = message.content.split(maxsplit=1)
    if len(pick_count) < 2 or not is_inteager(pick_count[1]):
        fail = 'invalid parameter value (not inteager)'
        await Log(message, f'Failed pick_member() by {fail}')
        await message.reply(fail)
        return

    pick_count = int(pick_count[1])

    if(pick_count < 1):
        fail = 'invalid parameter value (out of range)'
        await Log(message, f'Failed pick_member() by {fail}')
        await message.reply(fail)
        return

    members_info = []
    for member in members:
        if member.bot:
            continue
        members_info.append(member.id)
    
    if(pick_count > len(members_info)):
        fail = 'invalid parameter value (out of range)'
        await Log(message, f'Failed pick_member() by {fail}')
        await message.reply(fail)
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
    await message.channel.send(embed=embed)
    await Log(message, 'Success pick_member()')
    return

# member draw lots End

# help Message Begin
async def help(message, client):
    await Log(message, 'Call help()')
    embed = discord.Embed(title='How to Use')
    
    hp.ping(embed)
    hp.pin(embed)
    hp.vote(embed)
    hp.count(embed)
    hp.team(embed)
    hp.pick(embed)

    try:
        dm = await message.author.create_dm()
        await dm.send(embed=embed)
    except Exception as e:
        await Log(message, f'Failed help() by {e}')
        return
    await Log(message, f'Success help()')

# help Message End

# pin Begin
async def pin(message):
    await Log(message, 'Call pin()')
    str = message.content.split(' ', 1)[1]
    send_message = f'메시지 고정 : {str}\n요청자 : {message.author.mention}'
    await message.delete()
    sent_message = await message.channel.send(send_message)
    await sent_message.pin() 
    await Log(message, 'Success pin()')

# pin End


# Notion Schedule Begin
notion = Client(auth=dt.NOTION_API_KEY)

async def read_database(message):
    await Log(message, 'Call read_database()')
    result = query_database(dt.NOTION_DATABASE_ID)

    schedules = []
    embed = discord.Embed(title='최근 5개 일정')
    if result:
        for page in result:
            properties = page.get('properties', {})
            date_property = properties.get('날짜', {}).get('date', {})
            name = properties.get('이름', {}).get('title', {})
            name = name[0].get('text', {}).get('content', '')

            if date_property:
                start_date = date_property.get('start')
                end_date = date_property.get('end')
            schedules.append([name, start_date, end_date])
        
        count = 0
        for schedule in schedules:
            if count == 5:
                break
            if schedule[2]:
                embed.add_field(name=schedule[0], value=f'{schedule[1]} ~ {schedule[2]}', inline=False)
            else:
                embed.add_field(name=schedule[0], value=f'{schedule[1]}')
            count += 1
        await message.channel.send(embed=embed)
        await Log(message, 'Success read_database()')
    else:
        await Log(message, 'Failed read_database() by No Data')
    
def query_database(database_id):
    try:
        response = notion.databases.query(database_id=database_id)
        return response.get('results', [])
    except Exception as e:
        print(f'Error : {e}')
        return None

# notion Schedule End

# make qr Begin
async def make_qr(message):
    await Log(message, 'Call make_qr()')
    try:
        before_qr = message.content.split(maxsplit=1)[1]
        img = qrcode.make(before_qr)
        img.save('qr_image/qrcode.png')
        img_file = discord.File('qr_image/qrcode.png', filename='send_image.png')
        await message.reply(file=img_file)
        await Log(message, 'Success make_qr()')
    except IndexError as e:
        await Log(message, f'Failed make_qr() by {e}')
        await message.add_reaction('❌')
    except Exception as e:
        await Log(message, f'Failed make_qr() by {e}')
        await message.add_reaction('❌')
    return

# make qr End

def is_inteager(s):
    try:
        int(s)
        return True
    except ValueError:
        return False