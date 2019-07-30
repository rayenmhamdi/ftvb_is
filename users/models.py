from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Admin'),
        (2, 'FTVB_Agent'),
        (3, 'Ligue_Agent'),
        (4, 'Team'),
        (5, 'Player'),
        (5, 'Referee'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=USER_TYPE_CHOICES[0][0])


class Team(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='team')
    team_name = models.CharField(max_length=100, null=False, blank=False)
    team_short = models.CharField(max_length=10, null=False, blank=False)
    location = models.CharField(max_length=200, null=False, blank=False)
    foundation_year = models.DateField(null=False, blank=False)
    logo = models.ImageField(upload_to='teams_logo', null=True, blank=True)

    def __str__(self):
        return '{} ({})'.format(self.team_name, self.team_short)


'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('****', created)
    if instance.user_type == 4:
        TeamProfile.objects.get_or_create(user=instance)
'''