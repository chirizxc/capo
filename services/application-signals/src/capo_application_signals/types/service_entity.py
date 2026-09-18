"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceEntity``."""

from typing_extensions import NotRequired, TypedDict


class ServiceEntity(TypedDict, closed=True):
    type: NotRequired["str"]
    """<p>The type of the service entity.</p>"""
    name: NotRequired["str"]
    """<p>The name of the service.</p>"""
    environment: NotRequired["str"]
    """<p>The environment where the service is deployed.</p>"""
    aws_account_id: NotRequired["str"]
    """<p>The Amazon Web Services account ID where the service is located. Provide this value only for cross-account access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEntity) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "name" in value:
        out["Name"] = value["name"]
    if "environment" in value:
        out["Environment"] = value["environment"]
    if "aws_account_id" in value:
        out["AwsAccountId"] = value["aws_account_id"]
    return out


def deserialize_json(data: dict) -> ServiceEntity:
    out: ServiceEntity = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Environment") is not None:
        out["environment"] = data["Environment"]
    if data.get("AwsAccountId") is not None:
        out["aws_account_id"] = data["AwsAccountId"]
    return out
