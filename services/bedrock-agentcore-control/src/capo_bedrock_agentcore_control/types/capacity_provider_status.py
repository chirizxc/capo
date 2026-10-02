"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CapacityProviderStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a capacity provider. Possible values:</p> <ul> <li> <p> <code>CREATING</code> – The service is creating the capacity provider and validating its configuration.</p> </li> <li> <p> <code>CREATE_FAILED</code> – The service could not create the capacity provider. For details, see <code>statusCode</code> and <code>statusReason</code>.</p> </li> <li> <p> <code>UPDATING</code> – The service is updating the capacity provider.</p> </li> <li> <p> <code>UPDATE_FAILED</code> – The service could not update the capacity provider. For details, see <code>statusCode</code> and <code>statusReason</code>.</p> </li> <li> <p> <code>READY</code> – The capacity provider is available for use.</p> </li> <li> <p> <code>DELETING</code> – The service is deleting the capacity provider.</p> </li> <li> <p> <code>DELETE_FAILED</code> – The service could not delete the capacity provider. You can retry the deletion.</p> </li> </ul>"""
CapacityProviderStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "READY",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderStatus) -> str:
    return value


def deserialize_json(data: str) -> CapacityProviderStatus:
    return cast(CapacityProviderStatus, data)
