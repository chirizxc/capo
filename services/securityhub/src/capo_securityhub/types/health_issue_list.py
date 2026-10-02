"""Generated from Smithy shape ``com.amazonaws.securityhub#HealthIssueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.health_issue

HealthIssueList: TypeAlias = list["capo_securityhub.types.health_issue.HealthIssue"]


# --- restJson1 ser/de ---
def serialize_json(value: HealthIssueList) -> list:
    import capo_securityhub.types.health_issue

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.health_issue.serialize_json(item))
    return out


def deserialize_json(data: list) -> HealthIssueList:
    import capo_securityhub.types.health_issue

    out: HealthIssueList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityhub.types.health_issue.deserialize_json(item))
    return out
