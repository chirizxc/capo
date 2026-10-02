"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.client_token
    import capo_securityhub.types.cspm_provider_configuration
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.tag_map


class CreateConnectorRequest(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the connector. Must be unique within the account.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The description of the connector.</p>"""
    provider: NotRequired[
        "capo_securityhub.types.cspm_provider_configuration.CspmProviderConfiguration"
    ]
    """<p>The configuration for the cloud provider to connect to. Currently supports Azure.</p>"""
    tags: NotRequired["capo_securityhub.types.tag_map.TagMap"]
    """<p>The tags to add to the connector resource.</p>"""
    client_token: NotRequired["capo_securityhub.types.client_token.ClientToken"]
    """<p>A unique identifier used to ensure idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "provider" in value:
        import capo_securityhub.types.cspm_provider_configuration

        out["Provider"] = (
            capo_securityhub.types.cspm_provider_configuration.serialize_json(
                value["provider"]
            )
        )
    if "tags" in value:
        import capo_securityhub.types.tag_map

        out["Tags"] = capo_securityhub.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateConnectorRequest:
    out: CreateConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Provider") is not None:
        import capo_securityhub.types.cspm_provider_configuration

        out["provider"] = (
            capo_securityhub.types.cspm_provider_configuration.deserialize_json(
                data["Provider"]
            )
        )
    if data.get("Tags") is not None:
        import capo_securityhub.types.tag_map

        out["tags"] = capo_securityhub.types.tag_map.deserialize_json(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
