from datetime import datetime

week = {0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг', 4: 'пятница', 5: 'суббота', 6: 'воскресенье'}

months = {
    '01': 'янв', '02': 'фев',
    '03': 'мар', '04': 'апр', '05': 'май',
    '06': 'июн', '07': 'июл', '08': 'авг',
    '09': 'сен', '10': 'окт', '11': 'ноя',
    '12': 'дек'}

date_now = datetime.now()

def what_day_of_week(message):
    try:
        data = ''
        for x in message:
            if x.isdigit():
                data += x
        if len(data) == 4:
            data += str(date_now.year)
        if len(data) == 2:
            for key, value in months.items():
                if value in message:
                    data += key + str(date_now.year)
                    break
            else:
                data += str(date_now.month) + str(date_now.year)
        answer = f'Это будет {week[datetime.strptime(data, "%d%m%Y").weekday()]}'
        if data == date_now.strftime("%d%m%Y"):
            answer += '\nИ это кстати сегодня)'
        return answer

    except:
        return 'мне так не понятно...'

