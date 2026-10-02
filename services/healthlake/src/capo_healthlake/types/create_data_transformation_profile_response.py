"""Generated from Smithy shape ``com.amazonaws.healthlake#CreateDataTransformationProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.date_time
    import capo_healthlake.types.profile_id_string
    import capo_healthlake.types.profile_name_string
    import capo_healthlake.types.profile_version
    import capo_healthlake.types.source_format
    import capo_healthlake.types.target_format


class CreateDataTransformationProfileResponse(TypedDict, closed=True):
    profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString"
    """<p>The unique identifier of the created profile.</p>"""
    version: "capo_healthlake.types.profile_version.ProfileVersion"
    """<p>The version number of the newly created profile. The starting version is always 0, which indicates the profile is in DRAFT state.</p>"""
    source_format: "capo_healthlake.types.source_format.SourceFormat"
    """<p>The source data format of the profile.</p>"""
    target_format: "capo_healthlake.types.target_format.TargetFormat"
    """<p>The target output format. Always <code>FHIR_R4</code>.</p>"""
    profile_name: "capo_healthlake.types.profile_name_string.ProfileNameString"
    """<p>The name of the created profile.</p>"""
    last_updated_at: "capo_healthlake.types.date_time.DateTime"
    """<p>The timestamp when the profile was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDataTransformationProfileResponse) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    out["Version"] = value["version"]
    import capo_healthlake.types.source_format

    out["SourceFormat"] = capo_healthlake.types.source_format.serialize_aws_json_1_0(
        value["source_format"]
    )
    import capo_healthlake.types.target_format

    out["TargetFormat"] = capo_healthlake.types.target_format.serialize_aws_json_1_0(
        value["target_format"]
    )
    out["ProfileName"] = value["profile_name"]
    import capo_healthlake.types.date_time

    out["LastUpdatedAt"] = capo_healthlake.types.date_time.serialize_aws_json_1_0(
        value["last_updated_at"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDataTransformationProfileResponse:
    out: CreateDataTransformationProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError(
            "CreateDataTransformationProfileResponse.profile_id required"
        )
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        raise DeserializationError(
            "CreateDataTransformationProfileResponse.version required"
        )
    if data.get("SourceFormat") is not None:
        import capo_healthlake.types.source_format

        out["source_format"] = (
            capo_healthlake.types.source_format.deserialize_aws_json_1_0(
                data["SourceFormat"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataTransformationProfileResponse.source_format required"
        )
    if data.get("TargetFormat") is not None:
        import capo_healthlake.types.target_format

        out["target_format"] = (
            capo_healthlake.types.target_format.deserialize_aws_json_1_0(
                data["TargetFormat"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataTransformationProfileResponse.target_format required"
        )
    if data.get("ProfileName") is not None:
        out["profile_name"] = data["ProfileName"]
    else:
        raise DeserializationError(
            "CreateDataTransformationProfileResponse.profile_name required"
        )
    if data.get("LastUpdatedAt") is not None:
        import capo_healthlake.types.date_time

        out["last_updated_at"] = (
            capo_healthlake.types.date_time.deserialize_aws_json_1_0(
                data["LastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataTransformationProfileResponse.last_updated_at required"
        )
    return out
