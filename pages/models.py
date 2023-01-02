from django.db import models

# Create your models here.
class TeamMembers(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=100)
    team_image = models.ImageField(upload_to='team_photos/%Y/%m/%d/')
    is_part_of_team = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.name
