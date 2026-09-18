"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ConfiguredModelAlgorithmSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.configured_model_algorithm_arn
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description


class ConfiguredModelAlgorithmSummary(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the configured model algorithm was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the configured model algorithm was updated.</p>"""
    configured_model_algorithm_arn: "capo_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the configured model algorithm.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured model algorithm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredModelAlgorithmSummary) -> dict:
    out: dict = {}
    import capo_cleanroomsml._protocol.serialize

    out["createTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["create_time"]
    )
    import capo_cleanroomsml._protocol.serialize

    out["updateTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["update_time"]
    )
    out["configuredModelAlgorithmArn"] = value["configured_model_algorithm_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ConfiguredModelAlgorithmSummary:
    out: ConfiguredModelAlgorithmSummary = {}  # type: ignore[typeddict-item]
    if data.get("createTime") is not None:
        import datetime

        out["create_time"] = datetime.datetime.fromisoformat(
            data["createTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError(
            "ConfiguredModelAlgorithmSummary.create_time required"
        )
    if data.get("updateTime") is not None:
        import datetime

        out["update_time"] = datetime.datetime.fromisoformat(
            data["updateTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError(
            "ConfiguredModelAlgorithmSummary.update_time required"
        )
    if data.get("configuredModelAlgorithmArn") is not None:
        out["configured_model_algorithm_arn"] = data["configuredModelAlgorithmArn"]
    else:
        raise DeserializationError(
            "ConfiguredModelAlgorithmSummary.configured_model_algorithm_arn required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConfiguredModelAlgorithmSummary.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
