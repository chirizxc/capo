"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DatasetIntegrationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.dataset_integration_summary

DatasetIntegrationSummaries: TypeAlias = list[
    "capo_observabilityadmin.types.dataset_integration_summary.DatasetIntegrationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetIntegrationSummaries) -> list:
    import capo_observabilityadmin.types.dataset_integration_summary

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.dataset_integration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DatasetIntegrationSummaries:
    import capo_observabilityadmin.types.dataset_integration_summary

    out: DatasetIntegrationSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_observabilityadmin.types.dataset_integration_summary.deserialize_json(
                item
            )
        )
    return out
