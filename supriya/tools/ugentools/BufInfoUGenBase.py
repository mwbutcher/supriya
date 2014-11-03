# -*- encoding: utf-8 -*-
import abc
from supriya.tools.ugentools.InfoUGenBase import InfoUGenBase


class BufInfoUGenBase(InfoUGenBase):
    r'''Abstract base class for buffer information ugens.

    Buffer information ugens expose both scalar-calculation_rate and control-calculation_rate
    constructors, as buffer topology may change after a synth is instantiated.
    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Info UGens'

    __slots__ = ()

    _ordered_input_names = (
        'buffer_id',
        )

    ### INITIALIZER ###

    @abc.abstractmethod
    def __init__(
        self,
        buffer_id=None,
        calculation_rate=None,
        ):
        InfoUGenBase.__init__(
            self,
            buffer_id=buffer_id,
            calculation_rate=calculation_rate,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ir(cls, buffer_id=None):
        r'''Constructs a scalar-calculation_rate buffer information ugen.

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.SCALAR
        ugen = cls._new_expanded(
            buffer_id=buffer_id,
            calculation_rate=calculation_rate,
            )
        return ugen

    @classmethod
    def kr(cls, buffer_id=None):
        r'''Constructs a control-calculation_rate buffer information ugen.

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            buffer_id=buffer_id,
            calculation_rate=calculation_rate,
            )
        return ugen