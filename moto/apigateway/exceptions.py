from __future__ import unicode_literals
from moto.core.exceptions import RESTError



class StageNonFoundException(RESTError):
    code = 404

    def __init__(self, code="NonFoundException", message="Invalid stage identifier specified"):
        super(StageNonFoundException, self).__init__(
            code, message)



