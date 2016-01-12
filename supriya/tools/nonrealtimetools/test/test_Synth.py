# -*- encoding: utf-8 -*-
import os
import unittest
from abjad.tools import durationtools
from supriya.tools import requesttools
from supriya.tools import servertools
from supriya.tools import nonrealtimetools
from supriya.tools import osctools
from supriya.tools import synthdeftools
from supriya.tools import ugentools


class TestCase(unittest.TestCase):

    def setUp(self):
        self.output_filepath = os.path.abspath(os.path.join(
            os.path.dirname(__file__),
            'output.aiff',
            ))
        if os.path.exists(self.output_filepath):
            os.remove(self.output_filepath)

    def tearDown(self):
        if os.path.exists(self.output_filepath):
            os.remove(self.output_filepath)

    def build_synthdef(self):
        builder = synthdeftools.SynthDefBuilder(
            frequency=440,
            amplitude=1.,
            in_bus=0,
            out_bus=2,
            )
        with builder:
            input_ = ugentools.In.ar(bus=builder['in_bus'])
            source = ugentools.SinOsc.ar(frequency=builder['frequency'])
            source *= builder['amplitude']
            source *= input_
            ugentools.Out.ar(
                bus=builder['out_bus'],
                source=source,
                )
        return builder.build()

    def test_01(self):
        session = nonrealtimetools.Session()
        synth_one = session.add_synth(
            0, 4,
            synthdef=self.build_synthdef(),
            )
        synth_two = session.add_synth(
            2, 6,
            synthdef=self.build_synthdef(),
            frequency=330,
            )

        with session.at(2):
            synth_one['frequency'] = 550
        with session.at(3):
            synth_one['frequency'] = 660
            synth_two['frequency'] = 770
        with session.at(4):
            synth_two['frequency'] = 880

        with session.at(0):
            assert synth_one['frequency'] == 440
        with session.at(1):
            assert synth_one['frequency'] == 440
        with session.at(2):
            assert synth_one['frequency'] == 550
            assert synth_two['frequency'] == 330
        with session.at(3):
            assert synth_one['frequency'] == 660
            assert synth_two['frequency'] == 770
        with session.at(4):
            assert synth_two['frequency'] == 880
        with session.at(5):
            assert synth_two['frequency'] == 880

        id_mapping = {synth_one: 1001, synth_two: 1002}

        assert synth_one._collect_requests(id_mapping) == {
            durationtools.Offset(0, 1): [requesttools.SynthNewRequest(
                add_action=servertools.AddAction.ADD_TO_HEAD,
                node_id=1001,
                synthdef='0b294b53cc4d32c522f3e537ffb23f91',
                target_node_id=0
                )],
            durationtools.Offset(2, 1): [requesttools.NodeSetRequest(
                node_id=1001,
                frequency=550
                )],
            durationtools.Offset(3, 1): [requesttools.NodeSetRequest(
                node_id=1001,
                frequency=660
                )],
            durationtools.Offset(4, 1): [requesttools.NodeFreeRequest(
                node_ids=(1001,)
                )],
            }

        assert synth_two._collect_requests(id_mapping) == {
            durationtools.Offset(2, 1): [requesttools.SynthNewRequest(
                add_action=servertools.AddAction.ADD_TO_HEAD,
                node_id=1002,
                synthdef='0b294b53cc4d32c522f3e537ffb23f91',
                target_node_id=0,
                frequency=330
                )],
            durationtools.Offset(3, 1): [requesttools.NodeSetRequest(
                node_id=1002,
                frequency=770
                )],
            durationtools.Offset(4, 1): [requesttools.NodeSetRequest(
                node_id=1002,
                frequency=880
                )],
            durationtools.Offset(6, 1): [requesttools.NodeFreeRequest(
                node_ids=(1002,)
                )],
            }

    def test_02(self):
        session = nonrealtimetools.Session()
        bus_one = session.add_bus()
        bus_two = session.add_bus()
        session.add_synth(
            0, 4,
            synthdef=self.build_synthdef(),
            frequency=bus_one,
            amplitude=bus_two,
            )
        assert session.to_osc_bundles() == [
            osctools.OscBundle(
                timestamp=0.0,
                contents=(
                    osctools.OscMessage('/d_recv', bytearray(b'SCgf\x00\x00\x00\x02\x00\x01 0b294b53cc4d32c522f3e537ffb23f91\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x04?\x80\x00\x00C\xdc\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x04\tamplitude\x00\x00\x00\x00\tfrequency\x00\x00\x00\x01\x06in_bus\x00\x00\x00\x02\x07out_bus\x00\x00\x00\x03\x00\x00\x00\x06\x07Control\x01\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x01\x01\x01\x01\x02In\x02\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x02\x06SinOsc\x02\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff\xff\xff\xff\x00\x00\x00\x00\x02\x0cBinaryOpUGen\x02\x00\x00\x00\x02\x00\x00\x00\x01\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x0cBinaryOpUGen\x02\x00\x00\x00\x02\x00\x00\x00\x01\x00\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x02\x03Out\x02\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00')),
                    osctools.OscMessage('/s_new', '0b294b53cc4d32c522f3e537ffb23f91', 1000, 0, 0, 'amplitude', 'c1', 'frequency', 'c0'),
                    )
                ),
            osctools.OscBundle(
                timestamp=4.0,
                contents=(
                    osctools.OscMessage('/n_free', 1000),
                    )
                ),
            ]