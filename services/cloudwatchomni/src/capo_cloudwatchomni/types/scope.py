"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#Scope``."""

from typing import Literal, TypeAlias, cast

"""Whether an integration is account-scoped (customer-created) or organization-scoped (created by an org-enablement rule on behalf of the destination account). Mirrors the {@code Scope} discriminator used by CloudWatch Centralization / Observability Admin."""
Scope: TypeAlias = Literal[
    "ACCOUNT",
    "ORGANIZATION",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Scope) -> str:
    return value


def deserialize_cbor(data: str) -> Scope:
    return cast(Scope, data)
