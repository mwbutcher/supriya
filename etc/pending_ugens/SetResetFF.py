import collections
from supriya.enums import CalculationRate
from supriya.ugens.PulseCount import PulseCount


class SetResetFF(PulseCount):
    """

    ::

        >>> set_reset_ff = supriya.ugens.SetResetFF.ar(
        ...     reset=0,
        ...     trigger=0,
        ...     )
        >>> set_reset_ff
        SetResetFF.ar()

    """

    ### CLASS VARIABLES ###

    _ordered_input_names = collections.OrderedDict(
        'trigger',
        'reset',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        reset=0,
        trigger=0,
        ):
        PulseCount.__init__(
            self,
            calculation_rate=calculation_rate,
            reset=reset,
            trigger=trigger,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        reset=0,
        trigger=0,
        ):
        """
        Constructs an audio-rate SetResetFF.

        ::

            >>> set_reset_ff = supriya.ugens.SetResetFF.ar(
            ...     reset=0,
            ...     trigger=0,
            ...     )
            >>> set_reset_ff
            SetResetFF.ar()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            reset=reset,
            trigger=trigger,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        reset=0,
        trigger=0,
        ):
        """
        Constructs a control-rate SetResetFF.

        ::

            >>> set_reset_ff = supriya.ugens.SetResetFF.kr(
            ...     reset=0,
            ...     trigger=0,
            ...     )
            >>> set_reset_ff
            SetResetFF.kr()

        Returns ugen graph.
        """
        import supriya.synthdefs
        calculation_rate = supriya.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            reset=reset,
            trigger=trigger,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def reset(self):
        """
        Gets `reset` input of SetResetFF.

        ::

            >>> set_reset_ff = supriya.ugens.SetResetFF.ar(
            ...     reset=0,
            ...     trigger=0,
            ...     )
            >>> set_reset_ff.reset
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('reset')
        return self._inputs[index]

    @property
    def trigger(self):
        """
        Gets `trigger` input of SetResetFF.

        ::

            >>> set_reset_ff = supriya.ugens.SetResetFF.ar(
            ...     reset=0,
            ...     trigger=0,
            ...     )
            >>> set_reset_ff.trigger
            0.0

        Returns ugen input.
        """
        index = self._ordered_input_names.index('trigger')
        return self._inputs[index]
