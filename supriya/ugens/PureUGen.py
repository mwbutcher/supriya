from supriya.ugens.UGen import UGen


class PureUGen(UGen):
    """
    Abstract base class for ugens with no side-effects.

    These ugens may be optimized out of ugen graphs during SynthDef
    compilation.
    """

    ### CLASS VARIABLES ###

    _is_pure = True

    ### PRIVATE METHODS ###

    def _optimize_graph(self, sort_bundles):
        self._perform_dead_code_elimination(sort_bundles)
