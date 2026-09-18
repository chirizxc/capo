"""Generated from Smithy shape ``com.amazonaws.emr#DeleteSecurityConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.xml_string


class DeleteSecurityConfigurationInput(TypedDict, closed=True):
    name: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The name of the security configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSecurityConfigurationInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSecurityConfigurationInput:
    out: DeleteSecurityConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
