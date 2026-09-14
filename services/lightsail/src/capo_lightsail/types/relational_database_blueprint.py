"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseBlueprint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.relational_database_engine
    import capo_lightsail.types.string


class RelationalDatabaseBlueprint(TypedDict, closed=True):
    blueprint_id: NotRequired["capo_lightsail.types.string.string"]
    """<p>The ID for the database blueprint.</p>"""
    engine: NotRequired[
        "capo_lightsail.types.relational_database_engine.RelationalDatabaseEngine"
    ]
    """<p>The database software of the database blueprint (for example, <code>MySQL</code>).</p>"""
    engine_version: NotRequired["capo_lightsail.types.string.string"]
    """<p>The database engine version for the database blueprint (for example, <code>5.7.23</code>).</p>"""
    engine_description: NotRequired["capo_lightsail.types.string.string"]
    """<p>The description of the database engine for the database blueprint.</p>"""
    engine_version_description: NotRequired["capo_lightsail.types.string.string"]
    """<p>The description of the database engine version for the database blueprint.</p>"""
    is_engine_default: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the engine version is the default for the database blueprint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseBlueprint) -> dict:
    out: dict = {}
    if "blueprint_id" in value:
        out["blueprintId"] = value["blueprint_id"]
    if "engine" in value:
        import capo_lightsail.types.relational_database_engine

        out["engine"] = (
            capo_lightsail.types.relational_database_engine.serialize_aws_json_1_1(
                value["engine"]
            )
        )
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "engine_description" in value:
        out["engineDescription"] = value["engine_description"]
    if "engine_version_description" in value:
        out["engineVersionDescription"] = value["engine_version_description"]
    if "is_engine_default" in value:
        out["isEngineDefault"] = value["is_engine_default"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RelationalDatabaseBlueprint:
    out: RelationalDatabaseBlueprint = {}  # type: ignore[typeddict-item]
    if data.get("blueprintId") is not None:
        out["blueprint_id"] = data["blueprintId"]
    if data.get("engine") is not None:
        import capo_lightsail.types.relational_database_engine

        out["engine"] = (
            capo_lightsail.types.relational_database_engine.deserialize_aws_json_1_1(
                data["engine"]
            )
        )
    if data.get("engineVersion") is not None:
        out["engine_version"] = data["engineVersion"]
    if data.get("engineDescription") is not None:
        out["engine_description"] = data["engineDescription"]
    if data.get("engineVersionDescription") is not None:
        out["engine_version_description"] = data["engineVersionDescription"]
    if data.get("isEngineDefault") is not None:
        out["is_engine_default"] = data["isEngineDefault"]
    return out
