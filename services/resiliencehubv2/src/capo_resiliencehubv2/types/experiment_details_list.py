"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ExperimentDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.experiment_details

ExperimentDetailsList: TypeAlias = list[
    "capo_resiliencehubv2.types.experiment_details.ExperimentDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentDetailsList) -> list:
    import capo_resiliencehubv2.types.experiment_details

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.experiment_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExperimentDetailsList:
    import capo_resiliencehubv2.types.experiment_details

    out: ExperimentDetailsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_resiliencehubv2.types.experiment_details.deserialize_json(item))
    return out
