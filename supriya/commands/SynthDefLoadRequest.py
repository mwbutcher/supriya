import os
import supriya.osc
from supriya.commands.Request import Request


class SynthDefLoadRequest(Request):
    """
    A /d_load request.
    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_completion_message',
        '_synthdef_path',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        completion_message=None,
        synthdef_path=None,
        ):
        Request.__init__(self)
        self._completion_message = completion_message
        self._synthdef_path = os.path.abspath(synthdef_path)

    ### PUBLIC METHODS ###

    def to_osc_message(self, with_textual_osc_command=False):
        if with_textual_osc_command:
            request_id = self.request_command
        else:
            request_id = int(self.request_id)
        contents = [
            request_id,
            self.synthdef_path,
            ]
        if self.completion_message:
            completion_message = self.completion_message.to_datagram()
            completion_message = bytearray(completion_message)
            contents.append(completion_message)
        message = supriya.osc.OscMessage(*contents)
        return message

    ### PUBLIC PROPERTIES ###

    @property
    def completion_message(self):
        return self._completion_message

    @property
    def response_specification(self):
        import supriya.commands
        return {
            supriya.commands.DoneResponse: {
                'action': ('/d_load',),
                },
            }

    @property
    def request_id(self):
        import supriya.commands
        return supriya.commands.RequestId.SYNTHDEF_LOAD

    @property
    def synthdef_path(self):
        return self._synthdef_path