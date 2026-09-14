"""Generated from Smithy shape ``com.amazonaws.securitylake#CustomLogSourceAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.amazon_resource_name


class CustomLogSourceAttributes(TypedDict, closed=True):
    crawler_arn: NotRequired[
        "capo_securitylake.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the Glue crawler.</p>"""
    database_arn: NotRequired[
        "capo_securitylake.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the Glue database where results are written, such as: <code>arn:aws:daylight:us-east-1::database/sometable/*</code>.</p>"""
    table_arn: NotRequired[
        "capo_securitylake.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the Glue table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomLogSourceAttributes) -> dict:
    out: dict = {}
    if "crawler_arn" in value:
        out["crawlerArn"] = value["crawler_arn"]
    if "database_arn" in value:
        out["databaseArn"] = value["database_arn"]
    if "table_arn" in value:
        out["tableArn"] = value["table_arn"]
    return out


def deserialize_json(data: dict) -> CustomLogSourceAttributes:
    out: CustomLogSourceAttributes = {}  # type: ignore[typeddict-item]
    if data.get("crawlerArn") is not None:
        out["crawler_arn"] = data["crawlerArn"]
    if data.get("databaseArn") is not None:
        out["database_arn"] = data["databaseArn"]
    if data.get("tableArn") is not None:
        out["table_arn"] = data["tableArn"]
    return out
