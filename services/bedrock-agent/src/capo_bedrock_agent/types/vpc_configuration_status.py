"""Generated from Smithy shape ``com.amazonaws.bedrockagent#VpcConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The lifecycle status of a VPC configuration. Valid values:</p> <ul> <li> <p> <code>CREATING</code> – The configuration is being created.</p> </li> <li> <p> <code>CREATED</code> – The configuration is ready to use.</p> </li> <li> <p> <code>DELETING</code> – The configuration is being deleted.</p> </li> <li> <p> <code>CREATE_FAILED</code> – Creation failed. See <code>statusMessage</code> for the cause.</p> </li> <li> <p> <code>DELETE_FAILED</code> – Deletion failed. See <code>statusMessage</code> for the cause.</p> </li> </ul>"""
VpcConfigurationStatus: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "DELETING",
    "CREATE_FAILED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> VpcConfigurationStatus:
    return cast(VpcConfigurationStatus, data)
