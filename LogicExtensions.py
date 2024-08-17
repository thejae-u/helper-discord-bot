import requests
import json
import discord
import random
import math

# check latency
async def ping(message, client):
    latency = client.latency * 1000
    txt = str(round(latency, 3)) + ' ms'
    embed = discord.Embed(title='Pong!', description=txt)
    await message.reply(embed=embed)

# vote positive or negative
async def pn_vote(message):
    embed = discord.Embed(title='찬반 투표', description='원하는 곳에 투표하세요')
    msg = await message.channel.send(embed=embed)
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')
    
# voice channel team made (only 2 team)
async def make_team(message, client):
    if message.author.voice and message.author.voice.channel:
        voice_channel = message.author.voice.channel
        members = voice_channel.members
        
        if members:
            member_info = []
            for member in members:
                if member.bot:
                    continue
                member_info.append(member.id)
            
            for i in range(random.randrange(0, 10)): 
                random.shuffle(member_info)
            
            team1 = []
            team2 = []
            count = len(member_info)
            print(count)

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
        else:
            await message.channel.send('No Members in voice channel')
    else:
        await message.channel.send('you are not in voice channel')
   
# member draw lots
async def pick_member(message):
    if not message.author.voice and not message.author.voice.channel:
        await message.reply('you are not in voice channel')
        return

    voice_channel = message.author.voice.channel
    members = voice_channel.members

    if not members:
        await message.reply('no members in voice channel')
        return 
    
    pick_count = message.content.split(maxsplit=1)
    if len(pick_count) < 2 or not is_inteager(pick_count[1]):
        await message.reply('invalid parameter value (not inteager)')
        return

    pick_count = int(pick_count[1])
    members_info = []
    for member in members:
        if member.bot:
            continue
        members_info.append(member.id)
    
    if(pick_count > len(members_info)):
        await message.reply('invalid parameter value (out of range)')
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


def is_inteager(s):
    try:
        int(s)
        return True
    except ValueError:
        return False