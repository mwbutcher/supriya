# -*- encoding: utf-8 -*-
from supriya.tools.synthdeftools.UGen import UGen


class FreeSelf(UGen):

    ### CLASS VARIABLES ###

    __slots__ = ()

    _ordered_input_names = (
        'source',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        rate=None,
        source=None,
        ):
        UGen.__init__(
            self,
            rate=rate,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def kr(
        cls,
        source=None,
        ):
        from supriya.tools import synthdeftools
        rate = synthdeftools.Rate.CONTROL
        cls._new_expanded(
            rate=rate,
            source=source,
            )
        return source