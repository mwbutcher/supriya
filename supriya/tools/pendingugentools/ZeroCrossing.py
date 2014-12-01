# -*- encoding: utf-8 -*-
from supriya.tools.synthdeftools.UGen import UGen


class ZeroCrossing(UGen):
    r'''

    ::

        >>> zero_crossing = ugentools.ZeroCrossing.ar(
        ...     source=source,
        ...     )
        >>> zero_crossing
        ZeroCrossing.ar()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'source',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        source=None,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        source=source,
        ):
        r'''Constructs an audio-rate ZeroCrossing.

        ::

            >>> zero_crossing = ugentools.ZeroCrossing.ar(
            ...     source=source,
            ...     )
            >>> zero_crossing
            ZeroCrossing.ar()

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        source=source,
        ):
        r'''Constructs a control-rate ZeroCrossing.

        ::

            >>> zero_crossing = ugentools.ZeroCrossing.kr(
            ...     source=source,
            ...     )
            >>> zero_crossing
            ZeroCrossing.kr()

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def source(self):
        r'''Gets `source` input of ZeroCrossing.

        ::

            >>> zero_crossing = ugentools.ZeroCrossing.ar(
            ...     source=source,
            ...     )
            >>> zero_crossing.source

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('source')
        return self._inputs[index]