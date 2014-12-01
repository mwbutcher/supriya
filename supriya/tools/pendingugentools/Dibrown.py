# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.Dbrown import Dbrown


class Dibrown(Dbrown):
    r'''

    ::

        >>> dibrown = ugentools.Dibrown.ar(
        ...     length="float('inf')",
        ...     maximum=1,
        ...     minimum=0,
        ...     step=0.01,
        ...     )
        >>> dibrown
        Dibrown.ar()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'minimum',
        'maximum',
        'step',
        'length',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        length="float('inf')",
        maximum=1,
        minimum=0,
        step=0.01,
        ):
        Dbrown.__init__(
            self,
            calculation_rate=calculation_rate,
            length=length,
            maximum=maximum,
            minimum=minimum,
            step=step,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        length="float('inf')",
        maximum=1,
        minimum=0,
        step=0.01,
        ):
        r'''Constructs a Dibrown.

        ::

            >>> dibrown = ugentools.Dibrown.new(
            ...     length="float('inf')",
            ...     maximum=1,
            ...     minimum=0,
            ...     step=0.01,
            ...     )
            >>> dibrown
            Dibrown.new()

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = None
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            length=length,
            maximum=maximum,
            minimum=minimum,
            step=step,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def length(self):
        r'''Gets `length` input of Dibrown.

        ::

            >>> dibrown = ugentools.Dibrown.ar(
            ...     length="float('inf')",
            ...     maximum=1,
            ...     minimum=0,
            ...     step=0.01,
            ...     )
            >>> dibrown.length

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('length')
        return self._inputs[index]

    @property
    def maximum(self):
        r'''Gets `maximum` input of Dibrown.

        ::

            >>> dibrown = ugentools.Dibrown.ar(
            ...     length="float('inf')",
            ...     maximum=1,
            ...     minimum=0,
            ...     step=0.01,
            ...     )
            >>> dibrown.maximum
            1.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('maximum')
        return self._inputs[index]

    @property
    def minimum(self):
        r'''Gets `minimum` input of Dibrown.

        ::

            >>> dibrown = ugentools.Dibrown.ar(
            ...     length="float('inf')",
            ...     maximum=1,
            ...     minimum=0,
            ...     step=0.01,
            ...     )
            >>> dibrown.minimum
            0.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('minimum')
        return self._inputs[index]

    @property
    def step(self):
        r'''Gets `step` input of Dibrown.

        ::

            >>> dibrown = ugentools.Dibrown.ar(
            ...     length="float('inf')",
            ...     maximum=1,
            ...     minimum=0,
            ...     step=0.01,
            ...     )
            >>> dibrown.step
            0.01

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('step')
        return self._inputs[index]