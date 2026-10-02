"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PipelineSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.pipeline_summary

PipelineSummaries: TypeAlias = list[
    "capo_iotsitewise.types.pipeline_summary.PipelineSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineSummaries) -> list:
    import capo_iotsitewise.types.pipeline_summary

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.pipeline_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PipelineSummaries:
    import capo_iotsitewise.types.pipeline_summary

    out: PipelineSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iotsitewise.types.pipeline_summary.deserialize_json(item))
    return out
