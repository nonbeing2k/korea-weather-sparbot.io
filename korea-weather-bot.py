#-*- coding: utf-8 -*-


import urllib
from bs4 import BeautifulSoup
import requests
import datetime

def spark2(pay11,pay33):
 url = "https://api.ciscospark.com/v1/messages"
 pay1 = "{\n  \"roomId\": \""+pay11+"\","
 pay2 = "\n  \"text\": \""
 pay4 = "\""
 pay5 = "\n\n}"
 payload1 = pay1+pay2+pay33+pay4+pay5

 print "oooo", type ( payload1 )
 print "pppp payload1   ", payload1
 print

 #payload1 = payload1.encode('utf-8')

 #print "QQQQ", type ( payload1 )
 #print "RRRR payload1   ", payload1
 #print

 headers = {'authorization': "Bearer ----bot token----",'content-type': "application/json",    }
 response = requests.request("POST", url, data=payload1, headers=headers)
 #print response.text
 print " ================================ "

#
# start
#

print "================================================="
print datetime.datetime.now()
print "================================================="


data = urllib.urlopen('http://www.kma.go.kr/weather/forecast/summary.jsp?stnId=109&x=4&y=15')
soup = BeautifulSoup(data,"html.parser",from_encoding='utf-8')
raw = soup.findAll('td',attrs={'style':'vertical-align:top'})
pay3=raw[1]

print "aaaa", pay3
print "bbbb", type (pay3)
pay3= str(pay3)
pay3= pay3.decode('utf-8').encode('utf-8')
print "ccc", type(pay3),pay3
#pay3 = pay3.encode('utf-8')
print "ccc-222", type(pay3), pay3


for i in (0,1):

 pay3=pay3.replace("\n","")
 pay3=pay3.replace("<br","")
 pay3=pay3.replace("/>","")
 pay3=pay3.replace("<p>","")
 pay3=pay3.replace("</p>","")
 pay3=pay3.replace("\"","")
 pay3=pay3.replace("<td style=","")
 pay3=pay3.replace("vertical-align:top","")
 pay3=pay3.replace(">","")
 pay3=pay3.replace("<","")
 pay3=pay3.replace("/td","")

print "dddd", type(pay3), pay3

#
#


url = "https://api.ciscospark.com/hydra/api/v1/rooms"

headers = {
    'authorization': "Bearer YzUxMTJlMDMtMzhkNS00ZjYyLTg0MTktZmEwOGNhY2I3NGRjMTkyYjg1M2YtZDBl",
    'cache-control': "no-cache",
    'postman-token': "fdf40e39-026c-4aef-0e8d-746085973d6d"
    }

response = requests.request("GET", url, headers=headers)


t = response.text

t = t.split("id\":\"")

k = len(t)
print "number of room", k

for j in range (1,k):
  room = t[j]
  room = room[0:76]
  room = room.encode("utf-8")
  print "room is ", type(room), room

  spark2(room, pay3)
