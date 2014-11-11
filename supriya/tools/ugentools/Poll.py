# -*- encoding: utf-8 -*-
import collections
from supriya.tools.synthdeftools.UGen import UGen


class Poll(UGen):
    r'''UGen poller.

    ::

        >>> sine = ugentools.SinOsc.ar()
        >>> trigger = ugentools.Impulse.kr(1)
        >>> poll = ugentools.Poll.ar(
        ...     source=sine,
        ...     trigger=trigger,
        ...     trigger_id=1234,
        ...     )
        >>> poll
        Poll.ar()

    ..  container:: example

        ::

            >>> builder = SynthDefBuilder()
            >>> sine = ugentools.SinOsc.ar()
            >>> trigger = ugentools.Impulse.kr(1)
            >>> poll = ugentools.Poll.ar(
            ...     source=sine,
            ...     trigger=trigger,
            ...     trigger_id=1234,
            ...     )
            >>> builder.add_ugen([sine, trigger, poll])
            >>> synthdef = builder.build()

        ::

            >>> server = Server().boot()
            >>> synth = Synth(synthdef).allocate()
            >>> resonse_callback = responsetools.ResponseCallback(
            ...     prototype=responsetools.TriggerResponse,
            ...     procedure=lambda x: print(x),
            ...     )
            >>> server.register_response_callback(response_callback)

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'trigger',
        'source',
        'trigger_id',
        )

    _unexpanded_argument_names = None

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        label=None,
        source=None,
        trigger=None,
        trigger_id=-1,
        ):
        from supriya.tools import synthdeftools
        if label is None:
            if isinstance(source, synthdeftools.UGen):
                label = type(source).__name__
            elif isinstance(source, synthdeftools.OutputProxy):
                label = type(source.source).__name__
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            source=source,
            trigger=trigger,
            trigger_id=trigger_id,
            )
        label = str(label)
        self._configure_input('label', len(label))
        for character in label:
            self._configure_input('label', ord(character))

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        label=None,
        source=None,
        trigger=None,
        trigger_id=-1,
        ):
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            label=label,
            source=source,
            trigger=trigger,
            trigger_id=trigger_id,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        label=None,
        source=None,
        trigger=None,
        trigger_id=-1,
        ):
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            label=label,
            source=source,
            trigger=trigger,
            trigger_id=trigger_id,
            )
        return ugen

    @classmethod
    def new(
        cls,
        label=None,
        source=None,
        trigger=None,
        trigger_id=-1,
        ):
        from supriya.tools import synthdeftools
        if isinstance(source, collections.Sequence):
            source = (source,)
        calculation_rates = []
        for single_source in source:
            rate = synthdeftools.CalculationRate.from_expr(single_source)
            calculation_rates.append(rate)
        ugen = cls._new_expanded(
            calculation_rate=calculation_rates,
            label=label,
            source=source,
            trigger=trigger,
            trigger_id=trigger_id,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def label(self):
        index = self._ordered_input_names.index('trigger_id') + 2
        characters = self._inputs[index:]
        characters = [chr(int(_)) for _ in characters]
        label = ''.join(characters)
        return label