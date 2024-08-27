from datetime import datetime
async def Log(message, log_message):
    current_time = datetime.now().strftime('%y/%m/%d %H:%M:%S')
    save_log = f'[{current_time}] @{message.author.id} {log_message}\n'
    print(save_log)
    await write_log(save_log)
    return

async def write_log(log):
    try:
        f = open(file='Log/user-log.log', mode='a')
        f.write(log)
    except Exception as e:
        print(e)
    finally:
        f.close()
    return