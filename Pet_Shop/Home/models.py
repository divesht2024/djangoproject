from django.db import models
class Products(models.Model):
    name = models.CharField(max_length=220, null=True)
    price = models.FloatField()
    description = models.TextField()
    digital = models.BooleanField(default=True, null=True, blank=False)
    image = models.ImageField(null=True, blank=False)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
            return url
