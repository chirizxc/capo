"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#NamespaceKeyValidation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.namespace_allowed_values_list
    import capo_bedrock_agentcore_control.types.namespace_regex_pattern


class NamespaceKeyValidation(TypedDict, closed=True):
    allowed_values: NotRequired[
        "capo_bedrock_agentcore_control.types.namespace_allowed_values_list.NamespaceAllowedValuesList"
    ]
    """<p>The allowed values for this namespace variable key.</p>"""
    regex_pattern: NotRequired[
        "capo_bedrock_agentcore_control.types.namespace_regex_pattern.NamespaceRegexPattern"
    ]
    """<p>A regex pattern that the namespace variable key-value must match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NamespaceKeyValidation) -> dict:
    out: dict = {}
    if "allowed_values" in value:
        import capo_bedrock_agentcore_control.types.namespace_allowed_values_list

        out["allowedValues"] = (
            capo_bedrock_agentcore_control.types.namespace_allowed_values_list.serialize_json(
                value["allowed_values"]
            )
        )
    if "regex_pattern" in value:
        out["regexPattern"] = value["regex_pattern"]
    return out


def deserialize_json(data: dict) -> NamespaceKeyValidation:
    out: NamespaceKeyValidation = {}  # type: ignore[typeddict-item]
    if data.get("allowedValues") is not None:
        import capo_bedrock_agentcore_control.types.namespace_allowed_values_list

        out["allowed_values"] = (
            capo_bedrock_agentcore_control.types.namespace_allowed_values_list.deserialize_json(
                data["allowedValues"]
            )
        )
    if data.get("regexPattern") is not None:
        out["regex_pattern"] = data["regexPattern"]
    return out
