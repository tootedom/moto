from __future__ import unicode_literals
from moto.core.exceptions import RESTError


class ClientError(RESTError):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('template', 'single_error')
        super(ClientError, self).__init__(*args, **kwargs)


# class StageNonFoundError(ClientError):
#     code = 404
#
#     def __init__(self, stage_name):
#         super(StageNonFoundError, self).__init__(
#             "NonFoundException",
#             "Invalid stage identifier specified",
#             stage=stage_name,
#         )

class StageNonFoundError(RESTError):
    code = 404

    def __init__(self, code="NonFoundException", message="Invalid stage identifier specified"):
        super(StageNonFoundError, self).__init__(
            code, message)



