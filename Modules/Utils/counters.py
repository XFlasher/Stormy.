def coins_count(value):
    value = int(value)
    count = value - 100*(value//100)
    reminder = count % 10
    if count == 1 or reminder == 1:
        return f'{value} монета'
    elif reminder == 0 or reminder >= 5 or (10 <= count <= 19):
        return f'{value} монет'
    else:
        return f'{value} монеты'

def coins_count_send(value):
    value = int(value)
    count = value - 100*(value//100)
    reminder = count % 10
    if count == 1 or reminder == 1:
        return f'{value} монету'
    elif reminder == 0 or reminder >= 5 or (10 <= count <= 19):
        return f'{value} монет'
    else:
        return f'{value} монеты'

def members_count(value):
    value = int(value)
    count = value - 100*(value//100)
    reminder = count % 10
    if count == 1 or reminder == 1:
        return f'{value} пользователь'
    elif reminder == 0 or reminder >=5 or (10 <= reminder <=19):
        return f'{value} пользователей'
    else:
        return f'{value} пользователя'

def members_count_send(value):
    value = int(value)
    count = value - 100*(value//100)
    reminder = count % 10
    if count == 1 or reminder == 1:
        return f'{value} пользователя'
    elif reminder == 0 or reminder >=5 or (10 <= reminder <=19):
        return f'{value} пользователями'
    else:
        return f'{value} пользователями'

def guilds_count(value):
    value = int(value)
    count = value - 100*(value//100)
    reminder = count % 10
    if count == 1 or reminder == 1:
        return f'{value} сервер'
    elif reminder ==0 or reminder >=5 or (10 <= reminder <= 19):
        return f'{value} серверов'
    else:
        return f'{value} сервера'

def guilds_count_stats(value):
    value = int(value)
    count = value - 100*(value//100)
    reminder = count % 10
    if count == 1 or reminder == 1:
        return f'{value} сервером'
    elif reminder ==0 or reminder >=5 or (10 <= reminder <= 19):
        return f'{value} серверами'
    else:
        return f'{value} серверами'

def messages_count(value):
    value = int(value)
    count = value - 100*(value//100)
    reminder = count % 10
    if count ==1 or reminder == 1:
        return f'{value} сообщение'
    elif reminder ==0 or reminder >=5 or (10 <= reminder <= 19):
        return f'{value} сообщений'
    else:
        return f'{value} сообщения'

def trecks_count(value):
    value = int(value)
    count = value - 100*(value//100)
    reminder = count % 10
    if count ==1 or reminder == 1:
        return f'{value} трек'
    elif reminder ==0 or reminder >=5 or (10 <= reminder <= 19):
        return f'{value} треков'
    else:
        return f'{value} трека'

def hours_count(value):
    value = int(value)
    count = value - 100*(value//100)
    reminder = count % 10
    if count == 1 or reminder == 1:
        return f'{value} час'
    elif reminder == 0 or reminder >=5 or (10 <= reminder <=19):
        return f'{value} часов'
    else:
        return f'{value} часа'

def minutes_count(value):
    value = int(value)
    count = value - 100*(value//100)
    reminder = count % 10
    if count == 1 or reminder == 1:
        return f'{value} минута'
    elif reminder == 0 or reminder >=5 or (10 <= reminder <=19):
        return f'{value} минут'
    else:
        return f'{value} минуты'

def minutes_count_send(value):
    value = int(value)
    count = value - 100*(value//100)
    reminder = count % 10
    if count == 1 or reminder == 1:
        return f'{value} минуту'
    elif reminder == 0 or reminder >=5 or (10 <= reminder <=19):
        return f'{value} минут'
    else:
        return f'{value} минуты'

def seconds_count(value):
    value = int(value)
    count = value - 100*(value//100)
    reminder = count % 10
    if count == 1 or reminder == 1:
        return f'{value} секунда'
    elif reminder == 0 or reminder >=5 or (10 <= reminder <=19):
        return f'{value} секунд'
    else:
        return f'{value} секунды'

def seconds_count_send(value):
    value = int(value)
    count = value - 100*(value//100)
    reminder = count % 10
    if count == 1 or reminder == 1:
        return f'{value} секунду'
    elif reminder == 0 or reminder >=5 or (10 <= reminder <=19):
        return f'{value} секунд'
    else:
        return f'{value} секунды'

def cooldcounter(count):
    count = int(count)
    hours = int(count//3600)
    minutes = int(count//60)
    seconds = int(count%60)
    if hours != 0 and minutes != 0:
        minutes -= 60*hours
        return f'{hours_count(hours)} {minutes_count_send(minutes)} {seconds_count_send(seconds)}'
    elif hours == 0 and minutes != 0:
        return f'{minutes_count_send(minutes)} {seconds_count_send(seconds)}'
    else:
        return f'{seconds_count_send(seconds)}'

def uptime_counter(count):
    count = int(count)
    hours = int(count//3600)
    minutes = int(count//60)
    seconds = int(count%60)
    if hours != 0 and minets != 0:
        minutes -= 60*hours
        return f'{hours_count(hours)} {minutes_count(minutes)} {seconds_count(seconds)}'
    elif hours == 0 and minutes != 0:
        return f'{minutes_count(minutes)} {seconds_count(seconds)}'
    else:
        return f'{seconds_count(seconds)}'


def transact_count(value):
    value = int(value)
    count = value - 100*(value//100)
    reminder = count % 10
    if count == 1 or reminder == 1:
        return f'{value} транзакция'
    elif reminder == 0 or reminder >=5 or (10 <= reminder <=19):
        return f'{value} транзакций'
    else:
        return f'{value} транзакции'

def raw_bal_count(value):
    value = int(value)
    count = value - 100*(value//100)
    reminder = count % 10
    if count == 1 or reminder == 1:
        return f'{value} балл'
    elif reminder == 0 or reminder >=5 or (10 <= reminder <=19):
        return f'{value} баллов'
    else:
        return f'{value} балла'