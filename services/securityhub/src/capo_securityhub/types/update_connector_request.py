"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.cspm_provider_update_configuration
    import capo_securityhub.types.non_empty_string


class UpdateConnectorRequest(TypedDict, closed=True):
    connector_id: "capo_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The unique identifier of the connector to update.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The updated description of the connector.</p>"""
    provider: NotRequired[
        "capo_securityhub.types.cspm_provider_update_configuration.CspmProviderUpdateConfiguration"
    ]
    """<p>The updated cloud provider configuration for the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "provider" in value:
        import capo_securityhub.types.cspm_provider_update_configuration

        out["Provider"] = (
            capo_securityhub.types.cspm_provider_update_configuration.serialize_json(
                value["provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConnectorRequest:
    out: UpdateConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Provider") is not None:
        import capo_securityhub.types.cspm_provider_update_configuration

        out["provider"] = (
            capo_securityhub.types.cspm_provider_update_configuration.deserialize_json(
                data["Provider"]
            )
        )
    return out
