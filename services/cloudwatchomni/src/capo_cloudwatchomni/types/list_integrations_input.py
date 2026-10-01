"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListIntegrationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.integration_status
    import capo_cloudwatchomni.types.integration_type


class ListIntegrationsInput(TypedDict, closed=True):
    integration_type: NotRequired[
        "capo_cloudwatchomni.types.integration_type.IntegrationType"
    ]
    """Returns only integrations of this provider type."""
    status: NotRequired[
        "capo_cloudwatchomni.types.integration_status.IntegrationStatus"
    ]
    """Returns only integrations in this status."""
    name: NotRequired["str"]
    """Returns only the integration with this exact name."""
    next_token: NotRequired["str"]
    """Pagination token from a previous response; omit for the first page."""
    max_results: NotRequired["int"]
    """Maximum number of integrations to return in one page."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListIntegrationsInput) -> dict:
    out: dict = {}
    if "integration_type" in value:
        import capo_cloudwatchomni.types.integration_type

        out["integrationType"] = (
            capo_cloudwatchomni.types.integration_type.serialize_cbor(
                value["integration_type"]
            )
        )
    if "status" in value:
        import capo_cloudwatchomni.types.integration_status

        out["status"] = capo_cloudwatchomni.types.integration_status.serialize_cbor(
            value["status"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListIntegrationsInput:
    out: ListIntegrationsInput = {}  # type: ignore[typeddict-item]
    if data.get("integrationType") is not None:
        import capo_cloudwatchomni.types.integration_type

        out["integration_type"] = (
            capo_cloudwatchomni.types.integration_type.deserialize_cbor(
                data["integrationType"]
            )
        )
    if data.get("status") is not None:
        import capo_cloudwatchomni.types.integration_status

        out["status"] = capo_cloudwatchomni.types.integration_status.deserialize_cbor(
            data["status"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
