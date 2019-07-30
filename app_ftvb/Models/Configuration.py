from django.db import models

class Season(models.Model):
    first_year_season = models.IntegerField(null=False, blank=False)
    second_year_season = models.IntegerField(null=False, blank=False)



    def __str__(self):
        return 'Saison {}-{}'.format(self.first_year_season, self.second_year_season)


