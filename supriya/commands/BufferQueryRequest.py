import supriya.osc
from supriya.commands.Request import Request
from supriya.commands.RequestId import RequestId


class BufferQueryRequest(Request):
    """
    A /b_query request.

    ::

        >>> import supriya.commands
        >>> request = supriya.commands.BufferQueryRequest(
        ...     buffer_ids=(1, 23, 41)
        ...     )
        >>> request
        BufferQueryRequest(
            buffer_ids=(1, 23, 41),
            )

    ::

        >>> message = request.to_osc()
        >>> message
        OscMessage(47, 1, 23, 41)

    ::

        >>> message.address == supriya.commands.RequestId.BUFFER_QUERY
        True

    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_buffer_ids',
        )

    request_id = RequestId.BUFFER_QUERY

    ### INITIALIZER ###

    def __init__(
        self,
        buffer_ids=None,
    ):
        Request.__init__(self)
        if buffer_ids:
            buffer_ids = tuple(int(buffer_id) for buffer_id in buffer_ids)
        self._buffer_ids = buffer_ids

    ### PUBLIC METHODS ###

    def to_osc(self, with_request_name=False):
        if with_request_name:
            request_id = self.request_name
        else:
            request_id = int(self.request_id)
        contents = [
            request_id,
            ]
        for buffer_id in self.buffer_ids:
            contents.append(buffer_id)
        message = supriya.osc.OscMessage(*contents)
        return message

    ### PUBLIC PROPERTIES ###

    @property
    def buffer_ids(self):
        return self._buffer_ids

    @property
    def response_patterns(self):
        if 1 == len(self.buffer_ids):
            return [['/b_info', self.buffer_ids[0]]]
        return []
