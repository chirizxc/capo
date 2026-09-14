"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetIdentityCenterAuthTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class GetIdentityCenterAuthTokenResponse(TypedDict, closed=True):
    token: NotRequired["str"]
    """<p>The Identity Center authentication token that can be used to access data in the specified workgroups.</p> <p>This token contains the Identity Center identity information and is encrypted for secure transmission.</p>"""
    expiration_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the Identity Center authentication token expires.</p> <p>After this time, a new token must be requested for continued access.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIdentityCenterAuthTokenResponse) -> dict:
    out: dict = {}
    if "token" in value:
        out["token"] = value["token"]
    if "expiration_time" in value:
        import capo_redshift_serverless._protocol.serialize

        out["expirationTime"] = (
            capo_redshift_serverless._protocol.serialize.fmt_date_time(
                value["expiration_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIdentityCenterAuthTokenResponse:
    out: GetIdentityCenterAuthTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("token") is not None:
        out["token"] = data["token"]
    if data.get("expirationTime") is not None:
        import datetime

        out["expiration_time"] = datetime.datetime.fromisoformat(
            data["expirationTime"].replace("Z", "+00:00")
        )
    return out
