"""Generated from Smithy shape ``com.amazonaws.sesv2#TenantNameFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.tenant_name

TenantNameFilterList: TypeAlias = list["capo_sesv2.types.tenant_name.TenantName"]


# --- restJson1 ser/de ---
def serialize_json(value: TenantNameFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> TenantNameFilterList:
    return [item for item in data if item is not None]
