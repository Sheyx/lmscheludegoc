import requests
import json
from datetime import datetime
import getusers



def handler(event, context):
    link = getusers.getiCal('PackmanDC')
    data = requests.get(link).text
    print(icsSplit(data))

    return {
        'statusCode': 200,
        'body': {}
    }

def sendInChannels(schelude):
    data = {}
    for teams in schelude:
        send = False
        data['text'] = "**Сегодня дежурит**: \n\n"
        for team in schelude[teams]:
            send = True
            data['text'] = data['text']+'**'+team['position']+'**: '+team['loop']+'\n'
        if send:
            sendMessageLoop(getusers.getChannel(teams),data)


def sendMessageLoop(channel='', data={}):
    data['channel'] = channel
    url = "https://leroymerlin.loop.ru/hooks/ua38gsaq8iy1inzfnz8rppnk4e"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps(data)
    response = requests.request('POST', url, headers=headers, data=payload)



#Обработка календаря из GOC
def icsSplit(ics_data):
    events = []
    in_event = False
    lines = ics_data.split('\r\n')
    for line in lines:
        if line == 'BEGIN:VEVENT':
            event = {}
            in_event = True
            continue
        if line == 'END:VEVENT':
            events.append(event)
            in_event = False
            continue
        if in_event:
            key, val = line.split(':')
            event[key] = val
    return events
