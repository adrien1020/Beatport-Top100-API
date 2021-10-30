from django.contrib import admin
from .models import Main, DeepDubstepGrime, AfroHouse, BassClub, BassHouse, BreaksBreakBeatUKBass, DanceElectroPop, \
    DeepHouse, DJTools, DrumAndBass, Dubstep, ElectroClassicDetroitModern, Electronica, FunkyHouse, HardDanceHardcore, \
    HardTechno, House, IndieDance, JackinHouse, Mainstage,MelodicHouseTechno, MinimalDeepTech, NuDiscoDisco, \
    OrganicHouseDownTempo, ProgressiveHouse, PsyTrance, TechHouse, TechnoPeakTimeDriving


class BeatPortTop100Admin(admin.ModelAdmin):
    list_display = ('artist', 'title', 'remixers')
    search_fields = ['artist', 'title', "remixers"]


admin.site.register(Main, BeatPortTop100Admin)
admin.site.register(DeepDubstepGrime, BeatPortTop100Admin)
admin.site.register(AfroHouse, BeatPortTop100Admin)
admin.site.register(BassClub, BeatPortTop100Admin)
admin.site.register(BassHouse, BeatPortTop100Admin)
admin.site.register(BreaksBreakBeatUKBass, BeatPortTop100Admin)
admin.site.register(DanceElectroPop, BeatPortTop100Admin)
admin.site.register(DeepHouse, BeatPortTop100Admin)
admin.site.register(DJTools, BeatPortTop100Admin)
admin.site.register(DrumAndBass, BeatPortTop100Admin)
admin.site.register(Dubstep, BeatPortTop100Admin)
admin.site.register(ElectroClassicDetroitModern, BeatPortTop100Admin)
admin.site.register(Electronica, BeatPortTop100Admin)
admin.site.register(FunkyHouse, BeatPortTop100Admin)
admin.site.register(HardDanceHardcore, BeatPortTop100Admin)
admin.site.register(HardTechno, BeatPortTop100Admin)
admin.site.register(House, BeatPortTop100Admin)
admin.site.register(IndieDance, BeatPortTop100Admin)
admin.site.register(JackinHouse, BeatPortTop100Admin)
admin.site.register(Mainstage, BeatPortTop100Admin)
admin.site.register(MelodicHouseTechno, BeatPortTop100Admin)
admin.site.register(MinimalDeepTech, BeatPortTop100Admin)
admin.site.register(NuDiscoDisco, BeatPortTop100Admin)
admin.site.register(OrganicHouseDownTempo, BeatPortTop100Admin)
admin.site.register(ProgressiveHouse, BeatPortTop100Admin)
admin.site.register(PsyTrance, BeatPortTop100Admin)
admin.site.register(TechHouse, BeatPortTop100Admin)
admin.site.register(TechnoPeakTimeDriving, BeatPortTop100Admin)