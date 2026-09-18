"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#SubjectDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_rolesanywhere.types.credential_summaries
    import capo_rolesanywhere.types.instance_properties
    import capo_rolesanywhere.types.uuid


class SubjectDetail(TypedDict, closed=True):
    subject_arn: NotRequired["str"]
    """<p>The ARN of the resource.</p>"""
    subject_id: NotRequired["capo_rolesanywhere.types.uuid.Uuid"]
    """<p>The id of the resource</p>"""
    enabled: NotRequired["bool"]
    """<p>The enabled status of the subject.</p>"""
    x509_subject: NotRequired["str"]
    """<p>The x509 principal identifier of the authenticating certificate.</p>"""
    last_seen_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp of the last time this subject requested temporary session credentials.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the subject was created. </p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the subject was last updated.</p>"""
    credentials: NotRequired[
        "capo_rolesanywhere.types.credential_summaries.CredentialSummaries"
    ]
    """<p>The temporary session credentials vended at the last authenticating call with this subject.</p>"""
    instance_properties: NotRequired[
        "capo_rolesanywhere.types.instance_properties.InstanceProperties"
    ]
    """<p>The specified instance properties associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubjectDetail) -> dict:
    out: dict = {}
    if "subject_arn" in value:
        out["subjectArn"] = value["subject_arn"]
    if "subject_id" in value:
        out["subjectId"] = value["subject_id"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "x509_subject" in value:
        out["x509Subject"] = value["x509_subject"]
    if "last_seen_at" in value:
        import capo_rolesanywhere._protocol.serialize

        out["lastSeenAt"] = capo_rolesanywhere._protocol.serialize.fmt_date_time(
            value["last_seen_at"]
        )
    if "created_at" in value:
        import capo_rolesanywhere._protocol.serialize

        out["createdAt"] = capo_rolesanywhere._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_rolesanywhere._protocol.serialize

        out["updatedAt"] = capo_rolesanywhere._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    if "credentials" in value:
        import capo_rolesanywhere.types.credential_summaries

        out["credentials"] = (
            capo_rolesanywhere.types.credential_summaries.serialize_json(
                value["credentials"]
            )
        )
    if "instance_properties" in value:
        import capo_rolesanywhere.types.instance_properties

        out["instanceProperties"] = (
            capo_rolesanywhere.types.instance_properties.serialize_json(
                value["instance_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubjectDetail:
    out: SubjectDetail = {}  # type: ignore[typeddict-item]
    if data.get("subjectArn") is not None:
        out["subject_arn"] = data["subjectArn"]
    if data.get("subjectId") is not None:
        out["subject_id"] = data["subjectId"]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("x509Subject") is not None:
        out["x509_subject"] = data["x509Subject"]
    if data.get("lastSeenAt") is not None:
        import datetime

        out["last_seen_at"] = datetime.datetime.fromisoformat(
            data["lastSeenAt"].replace("Z", "+00:00")
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    if data.get("credentials") is not None:
        import capo_rolesanywhere.types.credential_summaries

        out["credentials"] = (
            capo_rolesanywhere.types.credential_summaries.deserialize_json(
                data["credentials"]
            )
        )
    if data.get("instanceProperties") is not None:
        import capo_rolesanywhere.types.instance_properties

        out["instance_properties"] = (
            capo_rolesanywhere.types.instance_properties.deserialize_json(
                data["instanceProperties"]
            )
        )
    return out
