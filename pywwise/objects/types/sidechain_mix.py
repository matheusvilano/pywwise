# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import (EColour, ESidechainMixConfig)
from pywwise.objects.abc import WwiseObject


class SidechainMix(WwiseObject):
    """
    https://www.audiokinetic.com/en/public-library/2025.1.6_9117/?source=SDK&id=wwiseobject_sidechainmix.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SIDECHAIN_MIX`.
    """
    colour = WwiseProperty[EColour]("Color", EColour)
    inclusion = WwiseProperty[bool]("Inclusion", bool)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    sidechain_mix_channel_config = WwiseProperty[ESidechainMixConfig]("SidechainMixChannelConfig", ESidechainMixConfig)
