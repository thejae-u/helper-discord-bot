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
        
        if message.stickers:
            return

        prefix = message.content[0]
        if prefix != dt.PREFIX:
            return
        
        # Message has blank
        msg = message.content[1:]
        if msg == '':
            return

        # Answer Logic Begin
        if msg == 'ping' or msg == '핑':
            await le.ping(message, self)
            return
        
        if msg == 'vote':
            await le.pn_vote(message)
            return

        if msg == 'team':
            await le.make_team(message, self)
            return
        
        if 'pick' in msg:
            await le.pick_member(message)
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