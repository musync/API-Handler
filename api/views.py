from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.shortcuts import render


from django.http import HttpResponse
import urllib2
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests
from django.http import HttpResponse
import urllib2
from django.utils.decorators import method_decorator
import json
import requests
import sys
import base64

from django.db.models import Count


from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from api.models import user , Song , DjSessions , Playlist 


def home(request):
	# OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
	
	# OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

	client_id = '33704938095-g3uhslf1enbgg84hb40k0924mgea5arm.apps.googleusercontent.com'

	client_secret = 'nOylsHNF81OOE5MwdUf2zhLv'

	redirect_uri = 'https://musynco.herokuapp.com/home'

	code = request.GET.get('code')
	print code 
	payload = {'grant_type' : 'authorization_code' , 'code':code  ,'redirect_uri' : redirect_uri  , 'client_id':client_id , 'client_secret' : client_secret  }
	# headers = {"Authorization": 'Basic' +  base64.b64encode(bytes( 'f9b9538acdb94eb8ae5fe30216b60b44:09cfe4fd21dd44c9b7fd7cdd672fd751'))}

	r = requests.post('https://www.googleapis.com/oauth2/v4/token' , params = payload)
	print r
	t = json.loads(r.text)
	global z 
	z = t['access_token']
	# det  = user.objects.get_or_create(access_token  = z)[0]
	
	# # aheaders = {'Host' : 'gdata.youtube.com' , 'Content-Type' : 'application/json' , 'Content-Length': 'CONTENT_LENGTH'  ,"Authorization": "Bearer " + z , 'GData-Version': '2' , 'X-GData-Key': 'key=DEVELOPER_KEY' } 
	# data  = {
	# # 'part' : 'contentDetails' , 
 #    'snippet': {
 #      'title': 'DJ.me', 
 #      'description': 'Sample playlist for Data API',


 #     }

   
 #  }

	# headers = {'Content-type': 'application/json', 'Accept': 'text/plain' , "Authorization": "Bearer " + z}
	# q = requests.post('https://www.googleapis.com/youtube/v3/playlists?part=snippet' , headers = headers , data=json.dumps(data))


	# print q 
	# a  = json.loads(q.text)
	
	# p_id = a['id']
	# det.playid = p_id
	# det.playurl = 'https://www.youtube.com/embed/playlist?list=' + p_id
	# det.hostname = a['snippet']['channelTitle']
	# det.save()
	# det.djsessions_set.get_or_create(hostedsession = 'VishrutsBash')

	# # s = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&order=viewCount&q=shape+of+you&type=video&videoDefinition=high' , headers = headers )
	# # songs  = json.loads(s.text)
	# # v_id  = songs['items'][0]['id']['videoId']


	# # data2 =   {
 # #    'snippet': {
 # #      'playlistId': p_id, 
 # #      'resourceId': {
 # #          'kind': 'youtube#video',
 # #          'videoId': v_id
 # #        },
 # #     'position': '0'
 # #      }
 # #   }

	# # w = requests.post('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet' , headers = headers , data=json.dumps(data2))

	# name = {'name' : det.hostname}
	responseobj = json.dumps(r, indent = 4)


	return HttpResponse(responseobj,content_type = "application/json")