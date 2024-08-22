import discord

def ping(embed:discord.Embed):
    embed.add_field(name='!ping or !핑', 
                    value='지연 시간을 알려줍니다',
                    inline=False)
    return embed

def pin(embed:discord.Embed):
    embed.add_field(name='!pin or !고정',
                    value='메시지를 고정 할 수 있습니다\n사용방벙 : !pin (고정할 메시지)',
                    inline=False)

def vote(embed:discord.Embed):
    embed.add_field(name='!vote or !투표',
                    value='찬반 투표를 할 수 있습니다',
                    inline=False)
    return embed

def team(embed:discord.Embed):
    embed.add_field(name='!team or !팀',
                    value='음성 채널에 있는 모든 인원을 두 팀으로 나눕니다 (봇 제외)',
                    inline=False)
    return embed

def pick(embed:discord.Embed):
    embed.add_field(name='!pick',
                    value='!pick (인원수) 를 입력하면 음성 채널에 있는 인원 중 인원 수 만큼 뽑습니다 (봇 제외)',
                    inline=False)
    return embed