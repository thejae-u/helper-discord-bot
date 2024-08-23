from datetime import datetime
def Log(message, func_name):
    current_time = datetime.now()
    print(f'[{current_time}] {message.author.name} {func_name} Executed')
    return