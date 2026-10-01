"""Generated from Smithy shape ``com.amazonaws.devopsagent#RemoteAgentAuthorizationMethod``."""

from typing import Literal, TypeAlias, cast

"""<p>Supported authorization methods for remote A2A agents.</p>"""
RemoteAgentAuthorizationMethod: TypeAlias = Literal[
    "oauth-client-credentials",
    "api-key",
    "bearer-token",
]


# --- restJson1 ser/de ---
def serialize_json(value: RemoteAgentAuthorizationMethod) -> str:
    return value


def deserialize_json(data: str) -> RemoteAgentAuthorizationMethod:
    return cast(RemoteAgentAuthorizationMethod, data)
