from datetime import datetime
async def Log(message, func_name):
    current_time = datetime.now()
    log_message = f'[{current_time}] {message.author.name} {func_name} Executed\n'
    print(log_message)
    await write_log(log_message)
    return

async def write_log(log):
    try:
        f = open(file='Log/log', mode='a')
        f.write(log)
    except Exception as e:
        print(e)
    finally:
        f.close()
    return