import requests, json

#628615
#81441388b5d9924e3afaf15ee25884
#amessage = 'Hello World!'

#room = 'https://api.hipchat.com/v2/room/18REPLACE35/notification'
#headers = {'Authorization':'Bearer UGetYourOwnAuthKey', 'Content-type':'application/json'}
#requests.post(url = room, data = json.dumps({'message':amessage}), headers = headers)

#pip install python-simple-hipchat

import hipchat
hipster = hipchat.HipChat(token='81441388b5d9924e3afaf15ee25884')
#hipster.method('rooms/message', method='POST', parameters={'room_id': 628615, 'from': 'HAL', 'message': 'All your base...'})
hipster.method('rooms/message', method='POST', parameters={'room_id': 628615, 'from': 'HAL', 'message': 'You should put on pants.'})