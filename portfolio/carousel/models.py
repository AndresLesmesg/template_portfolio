from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=60)
    info = models.CharField(max_length=120)
    description = models.TextField()
    image = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Link(models.Model):
    id_card = models.ForeignKey(Card, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class CardTag(models.Model):
    id_card = models.ForeignKey(Card, on_delete=models.CASCADE)
    id_tab = models.ForeignKey(Tag, on_delete=models.CASCADE)
