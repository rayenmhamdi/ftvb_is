import os

from django.conf import settings
from django.db import models
import datetime

# Create your models here.
from Library.CategoryFunctions import getCategory
from users.models import Team


def fileUploadPlayer(self, filename):
    ext = filename.split('.')[-1]
    ts = datetime.datetime.now().timestamp()
    return ('players/{}/{}'.format(self.team.id, '{}.{}'.format(str(ts), ext)))

class Player(models.Model):
    firstname = models.CharField(max_length=100, null=False, blank=False)
    lastname = models.CharField(max_length=100, null=False, blank=False)
    birthday = models.DateField(null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    nationality = models.CharField(max_length=50, null=False, blank=False)

    sexe = models.CharField(max_length=10, null=False, blank=False)

    STATUS_FIELDS = (
        ('Inactif', 'Inactif'),
        ('Actif', 'Actif'),
        ('Suspendu', 'Suspendu'),
    )
    status = models.CharField(max_length=100, null=False, blank=False, choices=STATUS_FIELDS, default=STATUS_FIELDS[0][0])
    qualification_date = models.DateField(null=True, blank=True)
    licence_number = models.CharField(max_length=50, null=True, blank=True, unique=True)

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='players'
    )

    photo  = models.ImageField(upload_to=fileUploadPlayer, null=False, blank=False)
    proof = models.ImageField(upload_to=fileUploadPlayer, null=False, blank=False)

    def deleteUploadedPhotoFile(self):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.photo.name))

    def deleteUploadedProofFile(self):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.proof.name))


    def setLicenceNumber(self):
        temp = self.birthday.year
        temp = str(temp)
        temp = temp[-2:]
        temp = int(temp)

        teamID = str(self.team.id).zfill(2);
        playerID = str(self.id).zfill(5);

        print('{}{}{}-{}-{}'.format(temp, str(self.birthday.month).zfill(2),str(self.birthday.day).zfill(2),teamID,playerID))

    def displayCategory(self):
        year = self.birthday.year
        x= getCategory(year, self.sexe)
        temp1=''
        temp2=''

        if x[0]=='S' :
            temp1 = 'Séniors'
        if x[0]=='J' :
            temp1 = 'Juniors'
        if x[0]=='C' and x[1]=='F':
            temp1 = 'Cadettes'
        if x[0]=='C' and x[1]=='G':
            temp1 = 'Cadets'
        if x[0]=='M' :
            temp1 = 'Minimes'
        if x[0]=='E' :
            temp1 = 'Ecole'
        if x[0]=='B' :
            temp1 = 'Benjamins'

        if x[1]=='G' :
            temp2 = 'Garcons'
        if x[1]=='F' :
            temp2 = 'Filles'

        return '{} {}'.format(temp1, temp2)
    def getPlayerCategory(self):
        year = self.birthday.year
        return getCategory(year, self.sexe)

    def __str__(self):
        return '{} {}'.format(self.lastname, self.firstname)


