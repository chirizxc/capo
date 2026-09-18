"""Generated from Smithy shape ``com.amazonaws.glue#SessionCommand``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string
    import capo_glue.types.python_version_string


class SessionCommand(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>Specifies the name of the SessionCommand. Can be 'glueetl' or 'gluestreaming'.</p>"""
    python_version: NotRequired[
        "capo_glue.types.python_version_string.PythonVersionString"
    ]
    """<p>Specifies the Python version. The Python version indicates the version supported for jobs of type Spark.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionCommand) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "python_version" in value:
        out["PythonVersion"] = value["python_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionCommand:
    out: SessionCommand = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("PythonVersion") is not None:
        out["python_version"] = data["PythonVersion"]
    return out
