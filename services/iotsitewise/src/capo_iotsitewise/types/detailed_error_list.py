"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DetailedErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.detailed_pipeline_error

DetailedErrorList: TypeAlias = list[
    "capo_iotsitewise.types.detailed_pipeline_error.DetailedPipelineError"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetailedErrorList) -> list:
    import capo_iotsitewise.types.detailed_pipeline_error

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.detailed_pipeline_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> DetailedErrorList:
    import capo_iotsitewise.types.detailed_pipeline_error

    out: DetailedErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iotsitewise.types.detailed_pipeline_error.deserialize_json(item)
        )
    return out
