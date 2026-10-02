"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#UserContext``."""

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError


class UserContext(TypedDict, closed=True):
    user_id: "str"
    """<p>The identifier of the user making the retrieval request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserContext) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> UserContext:
    out: UserContext = {}  # type: ignore[typeddict-item]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("UserContext.user_id required")
    return out
