from django.urls import path
from .api_view_main import main_list, main_detail
from .api_view_deep_dubstep_grime import deep_dubstep_grime_list, deep_dubstep_grime_detail
from .api_view_drum_and_bass import drum_and_bass_list, drum_and_bass_detail
from .api_view_dubstep import dubstep_list, dubstep_detail
from .api_view_electro_classic_detroit_modern import electro_classic_detroit_modern_list, electro_classic_detroit_modern_detail
from .api_view_electronica import electronica_list, electronica_detail
from .api_view_funky_house import funky_house_list, funky_house_detail
from .api_view_hard_dance_hardcore import hard_dance_hardcore_list, hard_dance_hardcore__detail
from .api_view_afro_house import afro_house_list, afro_house_detail
from .api_view_bass_club import bass_club_list, bass_club_detail
from .api_view_bass_house import bass_house_list, bass_house_detail
from .api_view_breaks_breakbeat_ukbass import breaks_breakbeat_ukbass_list, breaks_breakbeat_ukbass_detail
from .api_view_dance_electro_pop import dance_electro_pop_list, dance_electro_pop_detail
from .api_view_deep_house import deep_house_list, deep_house_detail
from .api_view_dj_tools import dj_tools_list, dj_tools_detail
from .api_view_hard_techno import hard_techno_list, hard_techno_detail
from .api_view_house import house_list, house_detail
from .api_view_indie_dance import indie_dance_list, indie_dance_detail
from .api_view_jackin_house import jackin_house_list, jackin_house_detail
from .api_view_mainstage import mainstage_list, mainstage_detail
from .api_view_melodic_house_techno import melodic_house_techno_list, melodic_house_techno_detail
from .api_view_minimal_deep_tech import  minimal_deep_tech_list, minimal_deep_tech_detail
from .api_view_nu_disco_disco import nu_disco_disco_list, nu_disco_disco_detail
from .api_view_organic_house_downtempo import organic_house_downtempo_list, organic_house_downtempo_detail
from .api_view_progressive_house import progressive_house_list, progressive_house_detail
from .api_view_psy_trance import psy_trance_list, psy_trance_detail
from .api_view_tech_house import tech_house_list, tech_house_detail
from .api_view_techno_peak_time_driving import techno_peak_time_driving_list, techno_peak_time_driving_detail


urlpatterns = [
    path('beatport-top100-main/', main_list),
    path('beatport-top100-main/<int:pk>/', main_detail),
    path('beatport-top100-140-deep-dubstep-grime/', deep_dubstep_grime_list),
    path('beatport-top100-140-deep-dubstep-grime/<int:pk>/', deep_dubstep_grime_detail),
    path('beatport-top100-afro-house/', afro_house_list),
    path('beatport-top100-afro-house/<int:pk>/', afro_house_detail),
    path('beatport-top100-bass-club/', bass_club_list),
    path('beatport-top100-bass-club/<int:pk>/', bass_club_detail),
    path('beatport-top100-bass-house/', bass_house_list),
    path('beatport-top100-bass-house/<int:pk>/', bass_house_detail),
    path('beatport-top100-breaks-breakbeat-uk-bass/', breaks_breakbeat_ukbass_list),
    path('beatport-top100-breaks-breakbeat-uk-bass/<int:pk>/', breaks_breakbeat_ukbass_detail),
    path('beatport-top100-dance-electro-pop/', dance_electro_pop_list),
    path('beatport-top100-dance-electro-pop/<int:pk>/', dance_electro_pop_detail),
    path('beatport-top100-deep-house/', deep_house_list),
    path('beatport-top100-deep-house/<int:pk>/', deep_house_detail),
    path('beatport-top100-dj-tools/', dj_tools_list),
    path('beatport-top100-dj-tools/<int:pk>/', dj_tools_detail),
    path('beatport-top100-drum-bass/', drum_and_bass_list),
    path('beatport-top100-drum-bass/<int:pk>/', drum_and_bass_detail),
    path('beatport-top100-dubstep/', dubstep_list),
    path('beatport-top100-dubstep/<int:pk>/', dubstep_detail),
    path('beatport-top100-electro-classic-detroit-modern/', electro_classic_detroit_modern_list),
    path('beatport-top100-electro-classic-detroit-modern/<int:pk>/', electro_classic_detroit_modern_detail),
    path('beatport-top100-electronica/', electronica_list),
    path('beatport-top100-electronica/<int:pk>/', electronica_detail),
    path('beatport-top100-funky-house/', funky_house_list),
    path('beatport-top100-funky-house/<int:pk>/', funky_house_detail),
    path('beatport-top100-hard-dance-hardcore/', hard_dance_hardcore_list),
    path('beatport-top100-hard-dance-hardcore/<int:pk>/', hard_dance_hardcore__detail),
    path('beatport-top100-hard-techno/', hard_techno_list),
    path('beatport-top100-hard-techno/<int:pk>/', hard_techno_detail),
    path('beatport-top100-house/', house_list),
    path('beatport-top100-house/<int:pk>/', house_detail),
    path('beatport-top100-indie-dance/', indie_dance_list),
    path('beatport-top100-indie-dance/<int:pk>/', indie_dance_detail),
    path('beatport-top100-jackin-house/', jackin_house_list),
    path('beatport-top100-jackin-house/<int:pk>/', jackin_house_detail),
    path('beatport-top100-mainstage/', mainstage_list),
    path('beatport-top100-mainstage/<int:pk>/', mainstage_detail),
    path('beatport-top100-melodic-house-techno/', melodic_house_techno_list),
    path('beatport-top100-melodic-house-techno/<int:pk>/', melodic_house_techno_detail),
    path('beatport-top100-minimal-deep-tech/', minimal_deep_tech_list),
    path('beatport-top100-minimal-deep-tech/<int:pk>/', minimal_deep_tech_detail),
    path('beatport-top100-nu-disco-disco/', nu_disco_disco_list),
    path('beatport-top100-nu-disco-disco/<int:pk>/', nu_disco_disco_detail),
    path('beatport-top100-organic-house-downtempo/', organic_house_downtempo_list),
    path('beatport-top100-organic-house-downtempo/<int:pk>/', organic_house_downtempo_detail),
    path('beatport-top100-progressive-house/', progressive_house_list),
    path('beatport-top100-progressive-house/<int:pk>/', progressive_house_detail),
    path('beatport-top100-psy-trance/', psy_trance_list),
    path('beatport-top100-psy-trance/<int:pk>/', psy_trance_detail),
    path('beatport-top100-tech-house/', tech_house_list),
    path('beatport-top100-tech-house/<int:pk>/', tech_house_detail),
    path('beatport-top100-techno-peak-time-driving/', techno_peak_time_driving_list),
    path('beatport-top100-techno-peak-time-driving/<int:pk>/', techno_peak_time_driving_detail),
    ]
