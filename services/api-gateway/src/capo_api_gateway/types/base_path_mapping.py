"""Generated from Smithy shape ``com.amazonaws.apigateway#BasePathMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class BasePathMapping(TypedDict, closed=True):
    base_path: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The base path name that callers of the API must provide as part of the URL after the domain name.</p>"""
    rest_api_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The string identifier of the associated RestApi.</p>"""
    stage: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The name of the associated stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BasePathMapping) -> dict:
    out: dict = {}
    if "base_path" in value:
        out["basePath"] = value["base_path"]
    if "rest_api_id" in value:
        out["restApiId"] = value["rest_api_id"]
    if "stage" in value:
        out["stage"] = value["stage"]
    return out


def deserialize_json(data: dict) -> BasePathMapping:
    out: BasePathMapping = {}  # type: ignore[typeddict-item]
    if data.get("basePath") is not None:
        out["base_path"] = data["basePath"]
    if data.get("restApiId") is not None:
        out["rest_api_id"] = data["restApiId"]
    if data.get("stage") is not None:
        out["stage"] = data["stage"]
    return out
