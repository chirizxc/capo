"""Generated from Smithy shape ``com.amazonaws.macie2#IamUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string


class IamUser(TypedDict, closed=True):
    account_id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The unique identifier for the Amazon Web Services account that's associated with the IAM user who performed the action.</p>"""
    arn: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the principal that performed the action. The last section of the ARN contains the name of the user who performed the action.</p>"""
    principal_id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The unique identifier for the IAM user who performed the action.</p>"""
    user_name: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The username of the IAM user who performed the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamUser) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    if "user_name" in value:
        out["userName"] = value["user_name"]
    return out


def deserialize_json(data: dict) -> IamUser:
    out: IamUser = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("principalId") is not None:
        out["principal_id"] = data["principalId"]
    if data.get("userName") is not None:
        out["user_name"] = data["userName"]
    return out
