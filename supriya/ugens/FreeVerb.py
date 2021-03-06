import collections
from supriya import CalculationRate
from supriya.ugens.UGen import UGen


class FreeVerb(UGen):
    """
    A FreeVerb reverb unit generator.

    ::

        >>> source = supriya.ugens.In.ar(bus=0)
        >>> supriya.ugens.FreeVerb.ar(
        ...     source=source,
        ...     )
        FreeVerb.ar()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Reverb UGens'

    _ordered_input_names = collections.OrderedDict([
        ('source', None),
        ('mix', 0.33),
        ('room_size', 0.5),
        ('damping', 0.5),
    ])

    _valid_calculation_rates = (
        CalculationRate.AUDIO,
    )
