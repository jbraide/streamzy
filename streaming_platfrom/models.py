from django.db import models
import uuid


    
class Genre(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Artists'

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    year = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Albums'

    def __str__(self):
        return self.name

class Song(models.Model):
    song_id = models.UUIDField(primary_key=True, unique=True,  default=uuid.uuid4(), editable=False)
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=10)
    artist = models.ForeignKey(Artist, on_delete= models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Songs'

    def __str__(self):
        return self.title

