hi all i am prajil
this program works based on api from sportskeeda website
so u need to paste the api link on the url space 
ie open that world_cup_with_python.py in edit with idle mode or on vs studio
 q=requests.get(input('paste sports keeda api here if u dont know go to readme file present in the unzipped file:')) u will see a request option like this
 go to https://www.sportskeeda.com/football select any football league like laliga ,worldcup etc
 select the upcoming match or completed match

 inspect that page and from network find api link paste it as shown below
 api will be like this :-https://fmc1.sportskeeda.com/en/v2/scores/football/v3/match_full/valladolid-vs-real-madrid-cf-la-liga-31-dec-2022

modify request like this in that py file
 q=requests.get('https://fmc1.sportskeeda.com/en/v2/scores/football/v3/match_full/valladolid-vs-real-madrid-cf-la-liga-31-dec-2022')

 save and run this u will get all details 

 enjoy all football matches from your offices,schools,colleges etc
 
 have a nice day thanks for using my program

 if u have any doubt msg/call at 6282513596




