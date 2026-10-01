"""Generated from Smithy shape ``com.amazonaws.connect#DescribeExtractionDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.extraction_definition


class DescribeExtractionDefinitionResponse(TypedDict, closed=True):
    extraction_definition: (
        "capo_connect.types.extraction_definition.ExtractionDefinition"
    )
    """<p>The extraction definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeExtractionDefinitionResponse) -> dict:
    out: dict = {}
    import capo_connect.types.extraction_definition

    out["ExtractionDefinition"] = (
        capo_connect.types.extraction_definition.serialize_json(
            value["extraction_definition"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeExtractionDefinitionResponse:
    out: DescribeExtractionDefinitionResponse = {}  # type: ignore[typeddict-item]
    if data.get("ExtractionDefinition") is not None:
        import capo_connect.types.extraction_definition

        out["extraction_definition"] = (
            capo_connect.types.extraction_definition.deserialize_json(
                data["ExtractionDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeExtractionDefinitionResponse.extraction_definition required"
        )
    return out
