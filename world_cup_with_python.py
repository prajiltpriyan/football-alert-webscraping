import requests
import time

while True:
    time.sleep(8)
    q=requests.get(input('paste sports keeda api here if u dont know go to readme file present in the unzipped file:'))
    a=q.json()
    
    game=a['basic']["match_comp_slug"]
    #print('*'+game.upper()+'*')
    loc=a['basic']["match_localteam_name"]
    vis=a['basic']["match_visitorteam_name"]
    date=a['basic']["match_date"]
    stad=a['basic']["match_stadium"]
    lscore=a['basic']["match_localteam_score"]
    vscore=a['basic']["match_visitorteam_score"]
    times=a['basic']["match_status"]
    #print(times)
    events=a['basic']["match_all_events"]
    l=len(events)
    for i in range(0,l):
     
     team=a['basic']["match_all_events"][i]["event_team"]
     event=a['basic']["match_all_events"][i]["event_type"]
     player=a['basic']["match_all_events"][i]["event_player"]
     tim=a['basic']["match_all_events"][i]["event_minute"]
     #print(team,event,player,tim)

    print('*'+game.upper()+'*')
    print('.'*len('*'+game.upper()+'*'))

    print(f'{loc} vs {vis}'.upper())

    print(f'DATE= {date}')
    print(f'STADIUM = {stad}')
    print(f'time={times}')
    print('SCORE CARD')
    print('-'*len('SCORE CARD'))
    print(f'{loc}= {lscore},{vis}= {vscore}')
    for i in range(0,l):
     
     team=a['basic']["match_all_events"][i]["event_team"]
     #event=a['basic']["match_all_events"][i]["event_type"]
     player=a['basic']["match_all_events"][i]["event_player"]
     tim=a['basic']["match_all_events"][i]["event_minute"]
     #print(team,event,player,tim)
     if event=='goal' and team=='visitorteam':
        print('*'+f'GOAL FOR {vis}'.upper()+'*')
        print('-'*len('*'+f'GOAL FOR {vis}'.upper()+'*'))
        print(f'at {tim} minutes {player} scored a goal')
     elif event== 'goal' and team=='localteam':
        asd=f'GOAL FOR {loc}'.upper()
        print('*'+asd+'*')
        print('-'*len('*'+asd+'*'))
        print(f'at {tim} minutes {player} scored a goal')
    if times!='FT' or times=='HT':
        if lscore==vscore:
            print('match draw still now')
            print('\n')
        elif lscore>vscore:
            print(f'{loc} leading')
            print('\n')
        elif lscore<vscore:
            print(f'{vis} leading')
            print('\n')
    else:
        if lscore==vscore:
            print('match ended draw')
            print('\n')
        elif lscore>vscore:
            print(f'{loc} won')
            print('\n')
        elif lscore<vscore:
            print(f'{vis} won')
            print('\n')
    #time.sleep(8)
