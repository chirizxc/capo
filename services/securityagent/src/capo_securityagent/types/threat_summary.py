"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.stride_category_list
    import capo_securityagent.types.threat_actor
    import capo_securityagent.types.threat_severity
    import capo_securityagent.types.threat_status


class ThreatSummary(TypedDict, closed=True):
    threat_id: NotRequired["str"]
    """<p>The unique identifier of the threat.</p>"""
    threat_job_id: NotRequired["str"]
    """<p>The unique identifier of the threat model job that produced the threat.</p>"""
    title: NotRequired["str"]
    """<p>A short title summarizing the threat.</p>"""
    statement: NotRequired["str"]
    """<p>The natural-language threat statement.</p>"""
    severity: NotRequired["capo_securityagent.types.threat_severity.ThreatSeverity"]
    """<p>The severity level of the threat.</p>"""
    status: NotRequired["capo_securityagent.types.threat_status.ThreatStatus"]
    """<p>The current status of the threat.</p>"""
    stride: NotRequired[
        "capo_securityagent.types.stride_category_list.StrideCategoryList"
    ]
    """<p>The STRIDE categories applicable to this threat.</p>"""
    created_by: NotRequired["capo_securityagent.types.threat_actor.ThreatActor"]
    """<p>Who created this threat.</p>"""
    updated_by: NotRequired["capo_securityagent.types.threat_actor.ThreatActor"]
    """<p>Who last updated this threat.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the threat was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the threat was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThreatSummary) -> dict:
    out: dict = {}
    if "threat_id" in value:
        out["threatId"] = value["threat_id"]
    if "threat_job_id" in value:
        out["threatJobId"] = value["threat_job_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "statement" in value:
        out["statement"] = value["statement"]
    if "severity" in value:
        import capo_securityagent.types.threat_severity

        out["severity"] = capo_securityagent.types.threat_severity.serialize_json(
            value["severity"]
        )
    if "status" in value:
        import capo_securityagent.types.threat_status

        out["status"] = capo_securityagent.types.threat_status.serialize_json(
            value["status"]
        )
    if "stride" in value:
        import capo_securityagent.types.stride_category_list

        out["stride"] = capo_securityagent.types.stride_category_list.serialize_json(
            value["stride"]
        )
    if "created_by" in value:
        import capo_securityagent.types.threat_actor

        out["createdBy"] = capo_securityagent.types.threat_actor.serialize_json(
            value["created_by"]
        )
    if "updated_by" in value:
        import capo_securityagent.types.threat_actor

        out["updatedBy"] = capo_securityagent.types.threat_actor.serialize_json(
            value["updated_by"]
        )
    if "created_at" in value:
        import capo_securityagent._protocol.serialize

        out["createdAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent._protocol.serialize

        out["updatedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> ThreatSummary:
    out: ThreatSummary = {}  # type: ignore[typeddict-item]
    if data.get("threatId") is not None:
        out["threat_id"] = data["threatId"]
    if data.get("threatJobId") is not None:
        out["threat_job_id"] = data["threatJobId"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("statement") is not None:
        out["statement"] = data["statement"]
    if data.get("severity") is not None:
        import capo_securityagent.types.threat_severity

        out["severity"] = capo_securityagent.types.threat_severity.deserialize_json(
            data["severity"]
        )
    if data.get("status") is not None:
        import capo_securityagent.types.threat_status

        out["status"] = capo_securityagent.types.threat_status.deserialize_json(
            data["status"]
        )
    if data.get("stride") is not None:
        import capo_securityagent.types.stride_category_list

        out["stride"] = capo_securityagent.types.stride_category_list.deserialize_json(
            data["stride"]
        )
    if data.get("createdBy") is not None:
        import capo_securityagent.types.threat_actor

        out["created_by"] = capo_securityagent.types.threat_actor.deserialize_json(
            data["createdBy"]
        )
    if data.get("updatedBy") is not None:
        import capo_securityagent.types.threat_actor

        out["updated_by"] = capo_securityagent.types.threat_actor.deserialize_json(
            data["updatedBy"]
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
    return out
