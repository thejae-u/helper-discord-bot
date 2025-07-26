from datetime import datetime
import discord

async def Log(ctx, log_text):
    current_time = datetime.now().strftime('%y/%m/%d %H:%M:%S')
    save_log = f'[{current_time}] @{ctx.message.author.id} {log_text}\n'
    print(save_log)
    await write_log(save_log)
    return

async def write_log(log):
    try:
        f = open(file='Log/user-log.userlog', mode='a')
        f.write(log)
    except Exception as e:
        print(e)
    finally:
        f.close()
    return