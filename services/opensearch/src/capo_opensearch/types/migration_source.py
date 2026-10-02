"""Generated from Smithy shape ``com.amazonaws.opensearch#MigrationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.arn


class MigrationSource(TypedDict, closed=True):
    datasource_arn: "capo_opensearch.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the data source to migrate saved objects from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationSource) -> dict:
    out: dict = {}
    out["datasourceArn"] = value["datasource_arn"]
    return out


def deserialize_json(data: dict) -> MigrationSource:
    out: MigrationSource = {}  # type: ignore[typeddict-item]
    if data.get("datasourceArn") is not None:
        out["datasource_arn"] = data["datasourceArn"]
    else:
        raise DeserializationError("MigrationSource.datasource_arn required")
    return out
