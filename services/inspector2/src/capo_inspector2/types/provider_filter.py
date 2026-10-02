"""Generated from Smithy shape ``com.amazonaws.inspector2#ProviderFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.connector_cloud_provider
    import capo_inspector2.types.provider_comparison


class ProviderFilter(TypedDict, closed=True):
    comparison: "capo_inspector2.types.provider_comparison.ProviderComparison"
    """<p>The comparison operator for the provider filter.</p>"""
    value: "capo_inspector2.types.connector_cloud_provider.ConnectorCloudProvider"
    """<p>The cloud provider value to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProviderFilter) -> dict:
    out: dict = {}
    import capo_inspector2.types.provider_comparison

    out["comparison"] = capo_inspector2.types.provider_comparison.serialize_json(
        value["comparison"]
    )
    import capo_inspector2.types.connector_cloud_provider

    out["value"] = capo_inspector2.types.connector_cloud_provider.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> ProviderFilter:
    out: ProviderFilter = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        import capo_inspector2.types.provider_comparison

        out["comparison"] = capo_inspector2.types.provider_comparison.deserialize_json(
            data["comparison"]
        )
    else:
        raise DeserializationError("ProviderFilter.comparison required")
    if data.get("value") is not None:
        import capo_inspector2.types.connector_cloud_provider

        out["value"] = capo_inspector2.types.connector_cloud_provider.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("ProviderFilter.value required")
    return out
