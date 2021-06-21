from django.db import models

# Create your models here.
class Movies(models.Model):
    def __init__(self):
        # title = unique, variable character chain, 64 quit maximum size, non null.
        title = models.CharField(max_length=64, default="", unique=True)
        # episode_nb: full, PRIMARY KEY.
        episode_nb = models.DecimalField(decimal_places=2, max_digits=1000, primary_key=True)
        # opening_crawl: text, can be null, no size limit.
        opening_crawl = models.TextField(null=True, blank=True)
        # director: variable character chain, non null, 32 bytes maximum size.
        director = models.CharField(max_length=32, default="")
        # producer: variable character chain, non null, 128 bytes maximum size.
        director = models.CharField(max_length=128, default="")
        # release_date: date (without time), non null.
        release_date = models.DateField(default="")
    def __str__(self):
        return self.title