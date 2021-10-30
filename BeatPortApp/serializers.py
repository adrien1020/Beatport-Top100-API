from .models import Main, DeepDubstepGrime, AfroHouse, BassClub, BassHouse, BreaksBreakBeatUKBass, DanceElectroPop, \
    DeepHouse, DJTools, DrumAndBass, Dubstep, ElectroClassicDetroitModern, Electronica, FunkyHouse, HardDanceHardcore, \
    HardTechno, House, IndieDance, JackinHouse, Mainstage, MelodicHouseTechno, MinimalDeepTech, NuDiscoDisco, OrganicHouseDownTempo, \
    ProgressiveHouse, PsyTrance, TechHouse, TechnoPeakTimeDriving
from rest_framework import serializers


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = '__all__'


class DeepDubstepGrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeepDubstepGrime
        fields = '__all__'


class AfroHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AfroHouse
        fields = '__all__'


class BassClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = BassClub
        fields = '__all__'


class BassHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BassHouse
        fields = '__all__'


class BreaksBreakBeatUKBassSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreaksBreakBeatUKBass
        fields = '__all__'


class DanceElectroPopSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanceElectroPop
        fields = '__all__'


class DeepHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeepHouse
        fields = '__all__'


class DJToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DJTools
        fields = '__all__'


class DrumAndBassSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrumAndBass
        fields = '__all__'


class DubstepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dubstep
        fields = '__all__'


class ElectroClassicDetroitModernSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectroClassicDetroitModern
        fields = '__all__'


class ElectronicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electronica
        fields = '__all__'


class FunkyHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunkyHouse
        fields = '__all__'


class HardDanceHardcoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardDanceHardcore
        fields = '__all__'


class HardTechnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardTechno
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class IndieDanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndieDance
        fields = '__all__'


class JackinHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = JackinHouse
        fields = '__all__'


class MainstageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mainstage
        fields = '__all__'

class MelodicHouseTechnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MelodicHouseTechno
        fields = '__all__'

class MinimalDeepTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinimalDeepTech
        fields = '__all__'

class NuDiscoDiscoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NuDiscoDisco
        fields = '__all__'

class OrganicHouseDownTempoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganicHouseDownTempo
        fields = '__all__'

class ProgressiveHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressiveHouse
        fields = '__all__'

class PsyTranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PsyTrance
        fields = '__all__'

class TechHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechHouse
        fields = '__all__'

class TechnoPeakTimeDrivingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnoPeakTimeDriving
        fields = '__all__'

