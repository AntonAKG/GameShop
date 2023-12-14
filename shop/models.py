from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255)
    main_image = models.ImageField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.title


class GalleryGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='gallery_games')
    image = models.ImageField()
