import discord
import Data as dt
import LogicExtensions as le
 
# Need Bot Token and Text channel ID
TOKEN = dt.TOKEN
 
# Logic
class HelperBot(discord.Client):
    async def on_ready(self):
        print(f'Bot Has started {self.user}')
        await self.change_presence(status=discord.Status.online, activity=discord.Game('Ask me Everything!'))

    # User Message with Prefix (!)
    async def on_message(self, message):
        # Don't answer myself
        if message.author == self.user:
            return
        
        # ignore sticker
        if message.stickers:
            return

        # ignore image or file
        if message.attachments:
            return

        # ignore no prefix message
        if not message.content.startswith('!'):
            return

        # ignore no message after prefix
        msg = message.content[1:]
        if msg == '':
            return

        # only Command
        msg = msg.split(' ', 1)[0]

        # Answer Logic Begin
        if msg == 'help' or msg == '도움말':
            await le.help(message, self)
            return

        if msg == 'ping' or msg == '핑':
            await le.ping(message, self)
            return
        
        if msg == 'pin' or msg == '고정':
            await le.pin(message)
            return
        
        if msg == 'vote' or msg == '투표':
            await le.pn_vote(message)
            return

        if msg == 'count' or msg == '몇명':
            await le.count_voice_member(message)
            return

        if msg == 'team' or msg == '팀':
            await le.make_team(message, self)
            return
        
        if msg == 'pick' or msg == '선택':
            await le.pick_member(message)
            return
        
        # for personal
        if msg == '일정':
            await le.read_database(message)
            return
        
        # not work
        if msg == 'qr':
            await le.make_qr(message)
            return
        # Answer Logic End
            
    # On Message End
    
# Main
def main():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.voice_states = True
    client = HelperBot(intents=intents)
    client.run(TOKEN)

if __name__ == '__main__':
    main()
