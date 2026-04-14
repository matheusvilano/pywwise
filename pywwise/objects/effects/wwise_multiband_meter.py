# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EMeterMode, EMeterScope, EDecibelsPerOctave, EMixdownConfig
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.game_parameter import GameParameter


class WwiseMultibandMeter(WwiseObject):
    """
    https://www.audiokinetic.com/en/public-library/2025.1.6_9117/?source=SDK&id=wwiseobject_effect_wwise_multiband_meter.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_MULTIBAND_METER`.
    """
    apply_downstream_volume = WwiseProperty[bool]("ApplyDownstreamVolume", bool)
    attack_time_band0 = WwiseProperty[float]("AttackTime_Band0", float)
    attack_time_band1 = WwiseProperty[float]("AttackTime_Band1", float)
    attack_time_band2 = WwiseProperty[float]("AttackTime_Band2", float)
    attack_time_band3 = WwiseProperty[float]("AttackTime_Band3", float)
    attack_time_band4 = WwiseProperty[float]("AttackTime_Band4", float)
    enabled_band1 = WwiseProperty[bool]("Enabled_Band1", bool)
    enabled_band2 = WwiseProperty[bool]("Enabled_Band2", bool)
    enabled_band3 = WwiseProperty[bool]("Enabled_Band3", bool)
    enabled_band4 = WwiseProperty[bool]("Enabled_Band4", bool)
    game_parameter_band0 = WwiseProperty[GameParameter]("GameParameter_Band0", GameParameter)
    game_parameter_band1 = WwiseProperty[GameParameter]("GameParameter_Band1", GameParameter)
    game_parameter_band2 = WwiseProperty[GameParameter]("GameParameter_Band2", GameParameter)
    game_parameter_band3 = WwiseProperty[GameParameter]("GameParameter_Band3", GameParameter)
    game_parameter_band4 = WwiseProperty[GameParameter]("GameParameter_Band4", GameParameter)
    high_frequency_band1 = WwiseProperty[float]("HighFrequency_Band1", float)
    high_frequency_band2 = WwiseProperty[float]("HighFrequency_Band2", float)
    high_frequency_band3 = WwiseProperty[float]("HighFrequency_Band3", float)
    high_frequency_band4 = WwiseProperty[float]("HighFrequency_Band4", float)
    high_rolloff_band1 = WwiseProperty[EDecibelsPerOctave]("HighRolloff_Band1", EDecibelsPerOctave)
    high_rolloff_band2 = WwiseProperty[EDecibelsPerOctave]("HighRolloff_Band2", EDecibelsPerOctave)
    high_rolloff_band3 = WwiseProperty[EDecibelsPerOctave]("HighRolloff_Band3", EDecibelsPerOctave)
    high_rolloff_band4 = WwiseProperty[EDecibelsPerOctave]("HighRolloff_Band4", EDecibelsPerOctave)
    hold_band0 = WwiseProperty[float]("Hold_Band0", float)
    hold_band1 = WwiseProperty[float]("Hold_Band1", float)
    hold_band2 = WwiseProperty[float]("Hold_Band2", float)
    hold_band3 = WwiseProperty[float]("Hold_Band3", float)
    hold_band4 = WwiseProperty[float]("Hold_Band4", float)
    infinite_hold = WwiseProperty[bool]("InfiniteHold", bool)
    low_frequency_band0 = WwiseProperty[float]("LowFrequency_Band0", float)
    low_frequency_band1 = WwiseProperty[float]("LowFrequency_Band1", float)
    low_frequency_band2 = WwiseProperty[float]("LowFrequency_Band2", float)
    low_frequency_band3 = WwiseProperty[float]("LowFrequency_Band3", float)
    low_frequency_band4 = WwiseProperty[float]("LowFrequency_Band4", float)
    low_rolloff_band1 = WwiseProperty[EDecibelsPerOctave]("LowRolloff_Band1", EDecibelsPerOctave)
    low_rolloff_band2 = WwiseProperty[EDecibelsPerOctave]("LowRolloff_Band2", EDecibelsPerOctave)
    low_rolloff_band3 = WwiseProperty[EDecibelsPerOctave]("LowRolloff_Band3", EDecibelsPerOctave)
    low_rolloff_band4 = WwiseProperty[EDecibelsPerOctave]("LowRolloff_Band4", EDecibelsPerOctave)
    max_band0 = WwiseProperty[float]("Max_Band0", float)
    max_band1 = WwiseProperty[float]("Max_Band1", float)
    max_band2 = WwiseProperty[float]("Max_Band2", float)
    max_band3 = WwiseProperty[float]("Max_Band3", float)
    max_band4 = WwiseProperty[float]("Max_Band4", float)
    meter_mode = WwiseProperty[EMeterMode]("MeterMode", EMeterMode)
    meter_scope = WwiseProperty[EMeterScope]("MeterScope", EMeterScope)
    min_band0 = WwiseProperty[float]("Min_Band0", float)
    min_band1 = WwiseProperty[float]("Min_Band1", float)
    min_band2 = WwiseProperty[float]("Min_Band2", float)
    min_band3 = WwiseProperty[float]("Min_Band3", float)
    min_band4 = WwiseProperty[float]("Min_Band4", float)
    mixdown_cfg = WwiseProperty[EMixdownConfig]("MeterScope", EMixdownConfig)
    release_time_band0 = WwiseProperty[float]("ReleaseTime_Band0", float)
    release_time_band1 = WwiseProperty[float]("ReleaseTime_Band1", float)
    release_time_band2 = WwiseProperty[float]("ReleaseTime_Band2", float)
    release_time_band3 = WwiseProperty[float]("ReleaseTime_Band3", float)
    release_time_band4 = WwiseProperty[float]("ReleaseTime_Band4", float)
    solo_monitor = WwiseProperty[int]("SoloMonitor", int)
