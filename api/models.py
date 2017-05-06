from django.db import models

# Create your models here.

class user(models.Model):
    YoutubeToken = models.CharField(max_length = 250 , default = 'NULL')
    Name = models.CharField(max_length = 250 , default = 'NULL')
    Email = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.Email

class DjSessions(models.Model):
    SessionName=models.CharField(max_length = 250 , default = 'NULL')
    Email = models.ForeignKey(user, on_delete=models.CASCADE)
    NetworkName = models.CharField(max_length = 250 , default = 'NULL')
    SessionId = models.CharField(max_length = 250 , default = 'NULL')
  
    def __str__(self):
        return self.SessionId




class Song(models.Model):
    SongName = models.CharField(max_length = 250 , default = 'NULL') 
    SongUrl = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.SongName 


       
class Playlist(models.Model):
    SongName = models.ForeignKey(Song, on_delete=models.CASCADE)
    SessionId = models.ForeignKey(DjSessions, on_delete=models.CASCADE)
    Email = models.ForeignKey(user, on_delete=models.CASCADE)
    