"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#LogType``."""

from typing import Literal, TypeAlias, cast

"""<p>The following log types are supported for log delivery configuration:</p> <ul> <li> <p>APPLICATION_LOGS – Application-level logs.</p> </li> <li> <p>USAGE_LOGS – Resource usage logs.</p> </li> <li> <p>SECURITY_FINDING_LOGS – Security finding logs.</p> </li> <li> <p>ACCESS_LOGS – Access logs (such as Elastic Load Balancing access logs).</p> </li> <li> <p>CONNECTION_LOGS – Connection logs.</p> </li> <li> <p>S3_SERVER_ACCESS_LOGS – Amazon S3 server access logs.</p> </li> </ul>"""
LogType: TypeAlias = Literal[
    "APPLICATION_LOGS",
    "USAGE_LOGS",
    "SECURITY_FINDING_LOGS",
    "ACCESS_LOGS",
    "CONNECTION_LOGS",
    "S3_SERVER_ACCESS_LOGS",
    "ALB_ACCESS_LOGS",
    "ALB_CONNECTION_LOGS",
    "ALB_HEALTH_CHECK_LOGS",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogType) -> str:
    return value


def deserialize_json(data: str) -> LogType:
    return cast(LogType, data)
