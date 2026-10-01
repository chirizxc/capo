from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    ElementalInferenceError as ElementalInferenceError,
)
from ._base import (
    SerializationError as SerializationError,
)
from ._base import (
    ServiceError as ServiceError,
)
from ._base import (
    UnknownServiceError as UnknownServiceError,
)
from ._base import (
    WaiterFailedError as WaiterFailedError,
)
from ._base import (
    WaiterTimeoutError as WaiterTimeoutError,
)
from .access_denied_exception import AccessDeniedException as AccessDeniedException
from .conflict_exception import ConflictException as ConflictException
from .gateway_timed_out_exception import (
    GatewayTimedOutException as GatewayTimedOutException,
)
from .internal_server_error_exception import (
    InternalServerErrorException as InternalServerErrorException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .service_unavailable_exception import (
    ServiceUnavailableException as ServiceUnavailableException,
)
from .too_many_request_exception import (
    TooManyRequestException as TooManyRequestException,
)
from .validation_exception import ValidationException as ValidationException
