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


from random import randint
import json
import requests
from django.http import HttpResponse
from api.models import user , DjSessions , Song , Playlist


def home(request):
	# OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
	
	# OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

	client_id = '486845874057-5l1khgmsrtp69eqtcp5r9hooml4mgak7.apps.googleusercontent.com'

	client_secret = 'Kcrlf5yDh4niKgJNublv3Gpu'

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
	det  = user.objects.get_or_create(Name  = 'Vishrut')[0]
	det.YoutubeToken = z
	det.Email = 'kohlivishrut@gmail.com'
	det.save()

	
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
	# responseobj = json.dumps(r, indent = 4)


	# return HttpResponse(responseobj,content_type = "application/json")
	return HttpResponse(r)

	# https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=486845874057-5l1khgmsrtp69eqtcp5r9hooml4mgak7.apps.googleusercontent.com&redirect_uri=https://musynco.herokuapp.com/home&scope=https://www.googleapis.com/auth/youtube



def sessionIdCreator(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    numberGenerated = randint(range_start, range_end)
    try:
    	Playlist.objects.all().filter(SessionId=numberGenerated)
    	sessionIdCreator(3)
    except:
    	a = True
    if(a):
    	return numberGenerated



def hostedsession(request):
	

	try:
		########################### EITHER YOU WILL HAVE YOUR POST REQUEST DATA IN REQUEST.BODY AND REQUEST.POST FROM WHERE YOU CAN PARSE it #######
		Name = request.GET.get('Name')
		u  = user.objects.get_or_create(Email  = 'kohlivishrut@gmail.com')[0]
		a = u.djsessions_set.get_or_create(SessionName = Name)
		a.SessionId = sessionIdCreator(3)
		a.save()

	

			
	except Exception as e:
		print e
		return HttpResponse("some error")
	return HttpResponse("Post Succcessful")


def songs_saver(request):
	# Create your views here.


	try:
		########################### EITHER YOU WILL HAVE YOUR POST REQUEST DATA IN REQUEST.BODY AND REQUEST.POST FROM WHERE YOU CAN PARSE it #######
		# print request.body
		x = json.loads(request.body)
		print request.body

		print json.loads(request.body)
		u  = user.objects.get_or_create(Email  = 'kohlivishrut@gmail.com')[0]
		a = u.djsessions_set.get_or_create(SessionName = x['Name'])
		f = djsessions.objects.get(hostedsession = x['hostedsession'])
		k = user.objects.get(hostname = x['hostname'])
		for i in range(10):
			x['song' + str(i)]
			# print i 
			

			u = f.hostsong_set.get_or_create(song = i)[0]
			u.song = i
			u.counter = str(int(u.counter) + 1)
			u.save()
		aa = djsessions.objects.all().filter(hostedsession=x['hostedsession'])
		songSorted = hostsong.objects.all().filter(hostedsession=aa).order_by('counter')
		finalList = songSorted.reverse()

		




			
	except Exception as e:
		print e
		return HttpResponse("some error")
	return HttpResponse("Post Succcessful")










def song(request):
	# aa = djsessions.objects.all().filter(hostedsession=foo)
	# songSorted = hostsong.objects.all().filter(hostedsession=aa).order_by('counter').reverse
	# data2  = {'hostname': 'Vishrut Kohli' , 'hostedsession' : 'vishrut1' , 'songs'  : [ 'Avicii - Did A Bad Bad Thing (Original Mix)' , 'Avicii - Dukkha (Original Mix)' , 'Avicii - Youre Gonna Love Again (Extended Mix)' , 'Avicii Ft. Project 46 & Daphne - Crime' , 'Avicii Ft. Project 46 & Daphne - Crime' , 'Avicii Ft. Taio Cruz - The Party Next Door (Vocal Mix)', 'Avicii ft Negin - Three Million (Your Love Is So Amazing)', ' Avicii - Fuck The Music', 'Avicii - Hello Miami', 'Avicii - ID (Original Mix)']}
	data3 = {'hostname': 'Vishrut Kohli' , 'hostedsession' : 'VishrutsBash' , 'songs'  : [  'Avicii Ft. Project 46 & Daphne - Crime' , 'Avicii Ft. Taio Cruz ', 'AviciiThree Million (Your Love Is So Amazing)',  'shape of you' , 'dont let me down' , 'one time' , 'sugar' , 'cold water' , 'closer']}

	w = requests.post('https://musync.herokuapp.com/song_saver' ,  data=json.dumps(data3))
	return HttpResponse(w.text)


def song2(request):
	# aa = djsessions.objects.all().filter(hostedsession=foo)
	# songSorted = hostsong.objects.all().filter(hostedsession=aa).order_by('counter').reverse
	# data2  = {'hostname': 'Vishrut Kohli' , 'hostedsession' : 'VishrutsBash' , 'songs'  : [  'Avicii Ft. Project 46 & Daphne - Crime' , 'Avicii Ft. Taio Cruz ', 'AviciiThree Million (Your Love Is So Amazing)',  'shape of you' , 'dont let me down' , 'one time' , 'sugar' , 'cold water' , 'closer']}
	data3 = {'hostname': 'Vishrut Kohli' , 'hostedsession' : 'VishrutsBash' , 'songs'  : [ 'shape of you' , 'dont let me down' , 'one time' , 'sugar' , 'cold water' , 'closer']}

	w = requests.post('https://musync.herokuapp.com/song_saver' ,  data=json.dumps(data3))
	return HttpResponse(w.text)

def song_d(request):
	# aa = djsessions.objects.all().filter(hostedsession=foo)
	# songSorted = hostsong.objects.all().filter(hostedsession=aa).order_by('counter').reverse
	# data2  = {'hostname': 'Vishrut Kohli' , 'hostedsession' : 'vishrut1' , 'songs'  : [ 'Avicii - Did A Bad Bad Thing (Original Mix)' , 'Avicii - Dukkha (Original Mix)' , 'Avicii - Youre Gonna Love Again (Extended Mix)' , 'Avicii Ft. Project 46 & Daphne - Crime' , 'Avicii Ft. Project 46 & Daphne - Crime' , 'Avicii Ft. Taio Cruz - The Party Next Door (Vocal Mix)', 'Avicii ft Negin - Three Million (Your Love Is So Amazing)', ' Avicii - Fuck The Music', 'Avicii - Hello Miami', 'Avicii - ID (Original Mix)']}
	data3 = {'hostname': 'Vishrut Kohli' , 'hostedsession' : 'VishrutsBash' , 'songs'  : [  'Avicii Ft. Project 46 & Daphne - Crime' , 'Avicii Ft. Taio Cruz ', 'AviciiThree Million (Your Love Is So Amazing)',  'shape of you' , 'dont let me down' , 'one time' , 'sugar' , 'cold water' , 'closer']}

	w = requests.post('https://musync.herokuapp.com/songs_deleter' ,  data=json.dumps(data3))
	return HttpResponse(w.text)


def song2_d(request):
	# aa = djsessions.objects.all().filter(hostedsession=foo)
	# songSorted = hostsong.objects.all().filter(hostedsession=aa).order_by('counter').reverse
	# data2  = {'hostname': 'Vishrut Kohli' , 'hostedsession' : 'VishrutsBash' , 'songs'  : [  'Avicii Ft. Project 46 & Daphne - Crime' , 'Avicii Ft. Taio Cruz ', 'AviciiThree Million (Your Love Is So Amazing)',  'shape of you' , 'dont let me down' , 'one time' , 'sugar' , 'cold water' , 'closer']}
	data3 = {'hostname': 'Vishrut Kohli' , 'hostedsession' : 'VishrutsBash' , 'songs'  : [ 'shape of you' , 'dont let me down' , 'one time' , 'sugar' , 'cold water' , 'closer']}

	w = requests.post('https://musync.herokuapp.com/songs_deleter' ,  data=json.dumps(data3))
	return HttpResponse(w.text)



