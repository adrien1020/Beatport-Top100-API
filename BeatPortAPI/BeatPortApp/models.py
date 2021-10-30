from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token




class Main(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'MAIN'


class DeepDubstepGrime(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = '140 / DEEP DUBSTEP / GRIME'


class AfroHouse(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'AFRO HOUSE'


class BassClub(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'BASS / CLUB'


class BassHouse(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'BASS / HOUSE'


class BreaksBreakBeatUKBass(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'BREAKS / BREAKBEAT / UK BASS'


class DanceElectroPop(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'DANCE / ELECTRO POP'


class DeepHouse(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'DEEP HOUSE'


class DJTools(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'DJ TOOLS'


class DrumAndBass(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'DRUM & BASS'

class Dubstep(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'DUBSTEP'


class ElectroClassicDetroitModern(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'ELECTRO (CLASSIC / DETROIT / MODERN)'


class Electronica(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'ELECTRONICA'


class FunkyHouse(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'FUNKY HOUSE'


class HardDanceHardcore(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'HARD DANCE / HARDCORE'


class HardTechno(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'HARD TECHNO'

class House(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'HOUSE'


class IndieDance(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'INDIE DANCE'


class JackinHouse(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'JACKIN HOUSE'

class Mainstage(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'MAINSTAGE'


class MelodicHouseTechno(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'MELODIC HOUSE & TECHNO'

class MinimalDeepTech(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'MINIMAL / DEEP TECH'

class NuDiscoDisco(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'NU DISCO / DISCO'

class OrganicHouseDownTempo(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'ORGANIC HOUSE / DOWNTEMPO'

class ProgressiveHouse(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'PROGRESSIVE HOUSE'

class PsyTrance(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'PSY-TRANCE'

class TechHouse(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'TECH HOUSE'


class TechnoPeakTimeDriving(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    remixers = models.CharField(max_length=200, blank=True)
    video_id = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    release_date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'TECHNO (PEAK TIME / DRIVING)'