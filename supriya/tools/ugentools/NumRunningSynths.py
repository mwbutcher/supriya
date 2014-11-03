# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.InfoUGenBase import InfoUGenBase


class NumRunningSynths(InfoUGenBase):
    r'''Number of running synths info unit generator.

    ::

        >>> ugentools.NumRunningSynths.ir()
        NumRunningSynths.ir()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Info UGens'

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        ):
        InfoUGenBase.__init__(
            self,
            calculation_rate=calculation_rate,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def kr(cls, **kwargs):
        r'''Construct a control-calculation_rate ugen.

        ::

            >>> num_running_synths = ugentools.NumRunningSynths.kr()
            >>> num_running_synths
            NumRunningSynths.kr() 

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            **kwargs
            )
        return ugen