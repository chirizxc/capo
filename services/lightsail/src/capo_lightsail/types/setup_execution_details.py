"""Generated from Smithy shape ``com.amazonaws.lightsail#SetupExecutionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.setup_status
    import capo_lightsail.types.string


class SetupExecutionDetails(TypedDict, closed=True):
    command: NotRequired["capo_lightsail.types.string.string"]
    """<p>The command that was executed.</p>"""
    date_time: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp for when the request was run.</p>"""
    name: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The name of the target resource.</p>"""
    status: NotRequired["capo_lightsail.types.setup_status.SetupStatus"]
    """<p>The status of the <code>SetupInstanceHttps</code> request.</p>"""
    standard_error: NotRequired["capo_lightsail.types.string.string"]
    """<p>The text written by the command to stderr.</p>"""
    standard_output: NotRequired["capo_lightsail.types.string.string"]
    """<p>The text written by the command to stdout.</p>"""
    version: NotRequired["capo_lightsail.types.string.string"]
    """<p>The current version of the script..</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetupExecutionDetails) -> dict:
    out: dict = {}
    if "command" in value:
        out["command"] = value["command"]
    if "date_time" in value:
        import capo_lightsail.types.iso_date

        out["dateTime"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["date_time"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import capo_lightsail.types.setup_status

        out["status"] = capo_lightsail.types.setup_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "standard_error" in value:
        out["standardError"] = value["standard_error"]
    if "standard_output" in value:
        out["standardOutput"] = value["standard_output"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SetupExecutionDetails:
    out: SetupExecutionDetails = {}  # type: ignore[typeddict-item]
    if data.get("command") is not None:
        out["command"] = data["command"]
    if data.get("dateTime") is not None:
        import capo_lightsail.types.iso_date

        out["date_time"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["dateTime"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        import capo_lightsail.types.setup_status

        out["status"] = capo_lightsail.types.setup_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("standardError") is not None:
        out["standard_error"] = data["standardError"]
    if data.get("standardOutput") is not None:
        out["standard_output"] = data["standardOutput"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
