"""Generated from Smithy shape ``com.amazonaws.securityhub#AzureScopeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.scope_type
    import capo_securityhub.types.scope_value_list


class AzureScopeConfiguration(TypedDict, closed=True):
    scope_type: NotRequired["capo_securityhub.types.scope_type.ScopeType"]
    """<p>The type of scope. Valid values are <code>tenant</code> and <code>subscription</code>.</p>"""
    scope_values: NotRequired["capo_securityhub.types.scope_value_list.ScopeValueList"]
    """<p>The list of scope values, such as subscription IDs, when the scope type is <code>subscription</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureScopeConfiguration) -> dict:
    out: dict = {}
    if "scope_type" in value:
        import capo_securityhub.types.scope_type

        out["ScopeType"] = capo_securityhub.types.scope_type.serialize_json(
            value["scope_type"]
        )
    if "scope_values" in value:
        import capo_securityhub.types.scope_value_list

        out["ScopeValues"] = capo_securityhub.types.scope_value_list.serialize_json(
            value["scope_values"]
        )
    return out


def deserialize_json(data: dict) -> AzureScopeConfiguration:
    out: AzureScopeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ScopeType") is not None:
        import capo_securityhub.types.scope_type

        out["scope_type"] = capo_securityhub.types.scope_type.deserialize_json(
            data["ScopeType"]
        )
    if data.get("ScopeValues") is not None:
        import capo_securityhub.types.scope_value_list

        out["scope_values"] = capo_securityhub.types.scope_value_list.deserialize_json(
            data["ScopeValues"]
        )
    return out
