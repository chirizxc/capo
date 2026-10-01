"""Generated from Smithy shape ``com.amazonaws.connect#ExtractionDefinitionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.extraction_definition_id
    import capo_connect.types.extraction_definition_name
    import capo_connect.types.timestamp


class ExtractionDefinitionSummary(TypedDict, closed=True):
    name: "capo_connect.types.extraction_definition_name.ExtractionDefinitionName"
    """<p>The name of the extraction definition.</p>"""
    extraction_definition_id: (
        "capo_connect.types.extraction_definition_id.ExtractionDefinitionId"
    )
    """<p>The identifier of the extraction definition.</p>"""
    extraction_definition_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the extraction definition.</p>"""
    created_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp when the extraction definition was created.</p>"""
    last_updated_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp when the extraction definition was last updated.</p>"""
    last_updated_by: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the extraction definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionDefinitionSummary) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ExtractionDefinitionId"] = value["extraction_definition_id"]
    out["ExtractionDefinitionArn"] = value["extraction_definition_arn"]
    import capo_connect.types.timestamp

    out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    import capo_connect.types.timestamp

    out["LastUpdatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["last_updated_time"]
    )
    out["LastUpdatedBy"] = value["last_updated_by"]
    return out


def deserialize_json(data: dict) -> ExtractionDefinitionSummary:
    out: ExtractionDefinitionSummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ExtractionDefinitionSummary.name required")
    if data.get("ExtractionDefinitionId") is not None:
        out["extraction_definition_id"] = data["ExtractionDefinitionId"]
    else:
        raise DeserializationError(
            "ExtractionDefinitionSummary.extraction_definition_id required"
        )
    if data.get("ExtractionDefinitionArn") is not None:
        out["extraction_definition_arn"] = data["ExtractionDefinitionArn"]
    else:
        raise DeserializationError(
            "ExtractionDefinitionSummary.extraction_definition_arn required"
        )
    if data.get("CreatedTime") is not None:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("ExtractionDefinitionSummary.created_time required")
    if data.get("LastUpdatedTime") is not None:
        import capo_connect.types.timestamp

        out["last_updated_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    else:
        raise DeserializationError(
            "ExtractionDefinitionSummary.last_updated_time required"
        )
    if data.get("LastUpdatedBy") is not None:
        out["last_updated_by"] = data["LastUpdatedBy"]
    else:
        raise DeserializationError(
            "ExtractionDefinitionSummary.last_updated_by required"
        )
    return out
