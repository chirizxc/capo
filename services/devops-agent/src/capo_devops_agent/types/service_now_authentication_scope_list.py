"""Generated from Smithy shape ``com.amazonaws.devopsagent#ServiceNowAuthenticationScopeList``."""

from typing import TypeAlias

ServiceNowAuthenticationScopeList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNowAuthenticationScopeList) -> list:
    return list(value)


def deserialize_json(data: list) -> ServiceNowAuthenticationScopeList:
    return [item for item in data if item is not None]
