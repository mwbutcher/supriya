from supriya.tools import patterntools
from patterntools_testbase import TestCase


class TestCase(TestCase):

    pattern_01 = patterntools.Ppar([
        patterntools.Pbind(
            amplitude=1.0,
            duration=1.0,
            frequency=patterntools.Pseq([1001, 1002, 1003], 1),
            ),
        ])

    pattern_02 = patterntools.Ppar([
        patterntools.Pbind(
            amplitude=1.0,
            duration=1.0,
            frequency=patterntools.Pseq([1001, 1002], 1),
            ),
        patterntools.Pmono(
            amplitude=1.0,
            duration=0.75,
            frequency=patterntools.Pseq([2001, 2002, 2003], 1),
            ),
        ])

    pattern_03 = patterntools.Ppar([
        patterntools.Pbind(
            amplitude=1.0,
            duration=1.0,
            frequency=patterntools.Pseq([1001, 1002, 1003], 1),
            ),
        patterntools.Pbind(
            amplitude=1.0,
            duration=0.75,
            frequency=patterntools.Pseq([], 1),
            ),
        ])

    pattern_04 = patterntools.Ppar([
        patterntools.Pbus(
            patterntools.Pbind(
                amplitude=1.0,
                duration=0.75,
                frequency=patterntools.Pseq([1001, 1002, 1003], 1),
                ),
            ),
        ])

    pattern_05 = patterntools.Ppar([
        patterntools.Pbus(
            patterntools.Pbind(
                amplitude=1.0,
                duration=1.0,
                frequency=patterntools.Pseq([1001, 1002], 1),
                ),
            ),
        patterntools.Pbus(
            patterntools.Pmono(
                amplitude=1.0,
                duration=0.75,
                frequency=patterntools.Pseq([2001, 2002, 2003], 1),
                ),
            ),
        ])

    pattern_06 = patterntools.Ppar([
        patterntools.Pgpar([
            [
                patterntools.Pbind(
                    delta=10,
                    duration=10,
                    frequency=patterntools.Pseq([1001, 1002, 1003]),
                    ),
                patterntools.Pbind(
                    delta=12,
                    duration=10,
                    frequency=patterntools.Pseq([2001, 2002, 2003]),
                    ),
                ],
            ]),
        patterntools.Pgpar([
            [
                patterntools.Pbind(
                    delta=10,
                    duration=10,
                    frequency=patterntools.Pseq([3001, 3002]),
                    ),
                patterntools.Pbind(
                    delta=12,
                    duration=10,
                    frequency=patterntools.Pseq([4001, 4002]),
                    ),
                ],
            ]),
        ])

    def test___iter___01(self):
        events = list(self.pattern_01)
        self.compare_objects_as_strings(
            events,
            '''
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=1.0,
                duration=1.0,
                frequency=1001,
                is_stop=True,
                uuid=UUID('A'),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=1.0,
                duration=1.0,
                frequency=1002,
                is_stop=True,
                uuid=UUID('B'),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                duration=1.0,
                frequency=1003,
                is_stop=True,
                uuid=UUID('C'),
                )
            ''',
            replace_uuids=True,
            )

    def test___iter___02(self):
        events = list(self.pattern_02)
        self.compare_objects_as_strings(
            events,
            '''
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=0.0,
                duration=1.0,
                frequency=1001,
                is_stop=True,
                uuid=UUID('A'),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=0.75,
                duration=0.75,
                frequency=2001,
                uuid=UUID('B'),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=0.25,
                duration=0.75,
                frequency=2002,
                uuid=UUID('B'),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=0.5,
                duration=1.0,
                frequency=1002,
                is_stop=True,
                uuid=UUID('C'),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                duration=0.75,
                frequency=2003,
                is_stop=True,
                uuid=UUID('B'),
                )
            ''',
            replace_uuids=True,
            )

    def test___iter___03(self):
        events = list(self.pattern_03)
        self.compare_objects_as_strings(
            events,
            '''
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=1.0,
                duration=1.0,
                frequency=1001,
                is_stop=True,
                uuid=UUID('A'),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=1.0,
                duration=1.0,
                frequency=1002,
                is_stop=True,
                uuid=UUID('B'),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                duration=1.0,
                frequency=1003,
                is_stop=True,
                uuid=UUID('C'),
                )
            ''',
            replace_uuids=True,
            )

    def test___iter___04(self):
        events = list(self.pattern_04)
        self.compare_objects_as_strings(
            events,
            '''
            supriya.tools.patterntools.CompositeEvent(
                delta=0.0,
                events=(
                    supriya.tools.patterntools.BusEvent(
                        calculation_rate=CalculationRate.AUDIO,
                        channel_count=2,
                        delta=0.0,
                        uuid=UUID('A'),
                        ),
                    supriya.tools.patterntools.GroupEvent(
                        delta=0.0,
                        uuid=UUID('B'),
                        ),
                    supriya.tools.patterntools.SynthEvent(
                        add_action=AddAction.ADD_AFTER,
                        amplitude=1.0,
                        delta=0.0,
                        fade_time=0.25,
                        in_=UUID('A'),
                        synthdef=<supriya.tools.synthdeftools.SynthDef('system_link_audio_2')>,
                        target_node=UUID('B'),
                        uuid=UUID('C'),
                        ),
                    ),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=0.75,
                duration=0.75,
                frequency=1001,
                is_stop=True,
                out=UUID('A'),
                target_node=UUID('B'),
                uuid=UUID('D'),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=0.75,
                duration=0.75,
                frequency=1002,
                is_stop=True,
                out=UUID('A'),
                target_node=UUID('B'),
                uuid=UUID('E'),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=0.75,
                duration=0.75,
                frequency=1003,
                is_stop=True,
                out=UUID('A'),
                target_node=UUID('B'),
                uuid=UUID('F'),
                )
            supriya.tools.patterntools.CompositeEvent(
                delta=0.0,
                events=(
                    supriya.tools.patterntools.SynthEvent(
                        delta=0.0,
                        is_stop=True,
                        uuid=UUID('C'),
                        ),
                    supriya.tools.patterntools.NullEvent(
                        delta=0.25,
                        ),
                    supriya.tools.patterntools.GroupEvent(
                        delta=0.0,
                        is_stop=True,
                        uuid=UUID('B'),
                        ),
                    supriya.tools.patterntools.BusEvent(
                        delta=0.0,
                        is_stop=True,
                        uuid=UUID('A'),
                        ),
                    ),
                is_stop=True,
                )
            ''',
            replace_uuids=True,
            )

    def test___iter___05(self):
        events = list(self.pattern_05)
        self.compare_objects_as_strings(
            events,
            '''
            supriya.tools.patterntools.CompositeEvent(
                delta=0.0,
                events=(
                    supriya.tools.patterntools.BusEvent(
                        calculation_rate=CalculationRate.AUDIO,
                        channel_count=2,
                        delta=0.0,
                        uuid=UUID('A'),
                        ),
                    supriya.tools.patterntools.GroupEvent(
                        delta=0.0,
                        uuid=UUID('B'),
                        ),
                    supriya.tools.patterntools.SynthEvent(
                        add_action=AddAction.ADD_AFTER,
                        amplitude=1.0,
                        delta=0.0,
                        fade_time=0.25,
                        in_=UUID('A'),
                        synthdef=<supriya.tools.synthdeftools.SynthDef('system_link_audio_2')>,
                        target_node=UUID('B'),
                        uuid=UUID('C'),
                        ),
                    ),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=0.0,
                duration=1.0,
                frequency=1001,
                is_stop=True,
                out=UUID('A'),
                target_node=UUID('B'),
                uuid=UUID('D'),
                )
            supriya.tools.patterntools.CompositeEvent(
                delta=0.0,
                events=(
                    supriya.tools.patterntools.BusEvent(
                        calculation_rate=CalculationRate.AUDIO,
                        channel_count=2,
                        delta=0.0,
                        uuid=UUID('E'),
                        ),
                    supriya.tools.patterntools.GroupEvent(
                        delta=0.0,
                        uuid=UUID('F'),
                        ),
                    supriya.tools.patterntools.SynthEvent(
                        add_action=AddAction.ADD_AFTER,
                        amplitude=1.0,
                        delta=0.0,
                        fade_time=0.25,
                        in_=UUID('E'),
                        synthdef=<supriya.tools.synthdeftools.SynthDef('system_link_audio_2')>,
                        target_node=UUID('F'),
                        uuid=UUID('G'),
                        ),
                    ),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=0.75,
                duration=0.75,
                frequency=2001,
                out=UUID('E'),
                target_node=UUID('F'),
                uuid=UUID('H'),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=0.25,
                duration=0.75,
                frequency=2002,
                out=UUID('E'),
                target_node=UUID('F'),
                uuid=UUID('H'),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=0.5,
                duration=1.0,
                frequency=1002,
                is_stop=True,
                out=UUID('A'),
                target_node=UUID('B'),
                uuid=UUID('I'),
                )
            supriya.tools.patterntools.NoteEvent(
                amplitude=1.0,
                delta=0.5,
                duration=0.75,
                frequency=2003,
                is_stop=True,
                out=UUID('E'),
                target_node=UUID('F'),
                uuid=UUID('H'),
                )
            supriya.tools.patterntools.CompositeEvent(
                delta=0.25,
                events=(
                    supriya.tools.patterntools.SynthEvent(
                        delta=0.0,
                        is_stop=True,
                        uuid=UUID('C'),
                        ),
                    supriya.tools.patterntools.NullEvent(
                        delta=0.25,
                        ),
                    supriya.tools.patterntools.GroupEvent(
                        delta=0.0,
                        is_stop=True,
                        uuid=UUID('B'),
                        ),
                    supriya.tools.patterntools.BusEvent(
                        delta=0.0,
                        is_stop=True,
                        uuid=UUID('A'),
                        ),
                    ),
                is_stop=True,
                )
            supriya.tools.patterntools.CompositeEvent(
                delta=0.0,
                events=(
                    supriya.tools.patterntools.SynthEvent(
                        delta=0.0,
                        is_stop=True,
                        uuid=UUID('G'),
                        ),
                    supriya.tools.patterntools.NullEvent(
                        delta=0.25,
                        ),
                    supriya.tools.patterntools.GroupEvent(
                        delta=0.0,
                        is_stop=True,
                        uuid=UUID('F'),
                        ),
                    supriya.tools.patterntools.BusEvent(
                        delta=0.0,
                        is_stop=True,
                        uuid=UUID('E'),
                        ),
                    ),
                is_stop=True,
                )
            ''',
            replace_uuids=True,
            )

    def test___iter___06(self):
        events = list(self.pattern_06)
        self.compare_objects_as_strings(
            events,
            '''
            supriya.tools.patterntools.CompositeEvent(
                delta=0.0,
                events=(
                    supriya.tools.patterntools.GroupEvent(
                        add_action=AddAction.ADD_TO_TAIL,
                        delta=0.0,
                        uuid=UUID('A'),
                        ),
                    ),
                )
            supriya.tools.patterntools.NoteEvent(
                delta=0.0,
                duration=10,
                frequency=1001,
                is_stop=True,
                target_node=UUID('A'),
                uuid=UUID('B'),
                )
            supriya.tools.patterntools.NoteEvent(
                delta=0.0,
                duration=10,
                frequency=2001,
                is_stop=True,
                target_node=UUID('A'),
                uuid=UUID('C'),
                )
            supriya.tools.patterntools.CompositeEvent(
                delta=0.0,
                events=(
                    supriya.tools.patterntools.GroupEvent(
                        add_action=AddAction.ADD_TO_TAIL,
                        delta=0.0,
                        uuid=UUID('D'),
                        ),
                    ),
                )
            supriya.tools.patterntools.NoteEvent(
                delta=0.0,
                duration=10,
                frequency=3001,
                is_stop=True,
                target_node=UUID('D'),
                uuid=UUID('E'),
                )
            supriya.tools.patterntools.NoteEvent(
                delta=10.0,
                duration=10,
                frequency=4001,
                is_stop=True,
                target_node=UUID('D'),
                uuid=UUID('F'),
                )
            supriya.tools.patterntools.NoteEvent(
                delta=0.0,
                duration=10,
                frequency=1002,
                is_stop=True,
                target_node=UUID('A'),
                uuid=UUID('G'),
                )
            supriya.tools.patterntools.NoteEvent(
                delta=2.0,
                duration=10,
                frequency=3002,
                is_stop=True,
                target_node=UUID('D'),
                uuid=UUID('H'),
                )
            supriya.tools.patterntools.NoteEvent(
                delta=0.0,
                duration=10,
                frequency=2002,
                is_stop=True,
                target_node=UUID('A'),
                uuid=UUID('I'),
                )
            supriya.tools.patterntools.NoteEvent(
                delta=8.0,
                duration=10,
                frequency=4002,
                is_stop=True,
                target_node=UUID('D'),
                uuid=UUID('J'),
                )
            supriya.tools.patterntools.NoteEvent(
                delta=4.0,
                duration=10,
                frequency=1003,
                is_stop=True,
                target_node=UUID('A'),
                uuid=UUID('K'),
                )
            supriya.tools.patterntools.NoteEvent(
                delta=0.0,
                duration=10,
                frequency=2003,
                is_stop=True,
                target_node=UUID('A'),
                uuid=UUID('L'),
                )
            supriya.tools.patterntools.CompositeEvent(
                delta=12.0,
                events=(
                    supriya.tools.patterntools.NullEvent(
                        delta=0.25,
                        ),
                    supriya.tools.patterntools.GroupEvent(
                        delta=0.0,
                        is_stop=True,
                        uuid=UUID('D'),
                        ),
                    ),
                is_stop=True,
                )
            supriya.tools.patterntools.CompositeEvent(
                delta=0.0,
                events=(
                    supriya.tools.patterntools.NullEvent(
                        delta=0.25,
                        ),
                    supriya.tools.patterntools.GroupEvent(
                        delta=0.0,
                        is_stop=True,
                        uuid=UUID('A'),
                        ),
                    ),
                is_stop=True,
                )
            ''',
            replace_uuids=True,
            )
