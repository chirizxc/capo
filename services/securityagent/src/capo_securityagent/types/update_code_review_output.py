"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateCodeReviewOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.assets
    import capo_securityagent.types.cloud_watch_log
    import capo_securityagent.types.code_remediation_strategy
    import capo_securityagent.types.service_role


class UpdateCodeReviewOutput(TypedDict, closed=True):
    code_review_id: "str"
    """<p>The unique identifier of the code review.</p>"""
    title: NotRequired["str"]
    """<p>The title of the code review.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the code review was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the code review was last updated, in UTC format.</p>"""
    assets: NotRequired["capo_securityagent.types.assets.Assets"]
    """<p>The assets included in the code review.</p>"""
    service_role: NotRequired["capo_securityagent.types.service_role.ServiceRole"]
    """<p>The IAM service role used for the code review.</p>"""
    log_config: NotRequired["capo_securityagent.types.cloud_watch_log.CloudWatchLog"]
    """<p>The CloudWatch Logs configuration for the code review.</p>"""
    agent_space_id: NotRequired["str"]
    """<p>The unique identifier of the agent space that contains the code review.</p>"""
    code_remediation_strategy: NotRequired[
        "capo_securityagent.types.code_remediation_strategy.CodeRemediationStrategy"
    ]
    """<p>The code remediation strategy for the code review.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCodeReviewOutput) -> dict:
    out: dict = {}
    out["codeReviewId"] = value["code_review_id"]
    if "title" in value:
        out["title"] = value["title"]
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
    if "assets" in value:
        import capo_securityagent.types.assets

        out["assets"] = capo_securityagent.types.assets.serialize_json(value["assets"])
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "log_config" in value:
        import capo_securityagent.types.cloud_watch_log

        out["logConfig"] = capo_securityagent.types.cloud_watch_log.serialize_json(
            value["log_config"]
        )
    if "agent_space_id" in value:
        out["agentSpaceId"] = value["agent_space_id"]
    if "code_remediation_strategy" in value:
        import capo_securityagent.types.code_remediation_strategy

        out["codeRemediationStrategy"] = (
            capo_securityagent.types.code_remediation_strategy.serialize_json(
                value["code_remediation_strategy"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCodeReviewOutput:
    out: UpdateCodeReviewOutput = {}  # type: ignore[typeddict-item]
    if data.get("codeReviewId") is not None:
        out["code_review_id"] = data["codeReviewId"]
    else:
        raise DeserializationError("UpdateCodeReviewOutput.code_review_id required")
    if data.get("title") is not None:
        out["title"] = data["title"]
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
    if data.get("assets") is not None:
        import capo_securityagent.types.assets

        out["assets"] = capo_securityagent.types.assets.deserialize_json(data["assets"])
    if data.get("serviceRole") is not None:
        out["service_role"] = data["serviceRole"]
    if data.get("logConfig") is not None:
        import capo_securityagent.types.cloud_watch_log

        out["log_config"] = capo_securityagent.types.cloud_watch_log.deserialize_json(
            data["logConfig"]
        )
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    if data.get("codeRemediationStrategy") is not None:
        import capo_securityagent.types.code_remediation_strategy

        out["code_remediation_strategy"] = (
            capo_securityagent.types.code_remediation_strategy.deserialize_json(
                data["codeRemediationStrategy"]
            )
        )
    return out
