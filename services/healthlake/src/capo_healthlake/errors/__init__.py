from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    HealthLakeError as HealthLakeError,
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
from .agent_message_out_of_context_exception import (
    AgentMessageOutOfContextException as AgentMessageOutOfContextException,
)
from .conflict_exception import ConflictException as ConflictException
from .conversation_not_found_exception import (
    ConversationNotFoundException as ConversationNotFoundException,
)
from .failed_dependency_exception import (
    FailedDependencyException as FailedDependencyException,
)
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .not_implemented_operation_exception import (
    NotImplementedOperationException as NotImplementedOperationException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .unauthorized_exception import UnauthorizedException as UnauthorizedException
from .unsupported_mime_type_exception import (
    UnsupportedMIMETypeException as UnsupportedMIMETypeException,
)
from .validation_exception import ValidationException as ValidationException
