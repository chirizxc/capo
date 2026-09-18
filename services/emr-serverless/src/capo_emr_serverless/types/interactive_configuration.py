"""Generated from Smithy shape ``com.amazonaws.emrserverless#InteractiveConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class InteractiveConfiguration(TypedDict, closed=True):
    studio_enabled: NotRequired["bool"]
    """<p>Enables you to connect an application to Amazon EMR Studio to run interactive workloads in a notebook.</p>"""
    livy_endpoint_enabled: NotRequired["bool"]
    """<p>Enables an Apache Livy endpoint that you can connect to and run interactive jobs.</p>"""
    session_enabled: NotRequired["bool"]
    """<p>Enables interactive sessions on the application. When set to <code>true</code>, you can start interactive sessions using the <code>StartSession</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InteractiveConfiguration) -> dict:
    out: dict = {}
    if "studio_enabled" in value:
        out["studioEnabled"] = value["studio_enabled"]
    if "livy_endpoint_enabled" in value:
        out["livyEndpointEnabled"] = value["livy_endpoint_enabled"]
    if "session_enabled" in value:
        out["sessionEnabled"] = value["session_enabled"]
    return out


def deserialize_json(data: dict) -> InteractiveConfiguration:
    out: InteractiveConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("studioEnabled") is not None:
        out["studio_enabled"] = data["studioEnabled"]
    if data.get("livyEndpointEnabled") is not None:
        out["livy_endpoint_enabled"] = data["livyEndpointEnabled"]
    if data.get("sessionEnabled") is not None:
        out["session_enabled"] = data["sessionEnabled"]
    return out
