"""Generated from Smithy shape ``com.amazonaws.medialive#InputDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_input_request_destination_route
    import capo_medialive.types.__string


class InputDestinationRequest(TypedDict, closed=True):
    stream_name: NotRequired["capo_medialive.types.__string.__string"]
    """A unique name for the location the RTMP stream is being pushed to."""
    network: NotRequired["capo_medialive.types.__string.__string"]
    """If the push input has an input location of ON-PREM, ID the ID of the attached network."""
    network_routes: NotRequired[
        "capo_medialive.types.__list_of_input_request_destination_route.__listOfInputRequestDestinationRoute"
    ]
    """If the push input has an input location of ON-PREM it's a requirement to specify what the route of the input is going to be on the customer local network."""
    static_ip_address: NotRequired["capo_medialive.types.__string.__string"]
    """If the push input has an input location of ON-PREM it's optional to specify what the ip address of the input is going to be on the customer local network."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDestinationRequest) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["streamName"] = value["stream_name"]
    if "network" in value:
        out["network"] = value["network"]
    if "network_routes" in value:
        import capo_medialive.types.__list_of_input_request_destination_route

        out["networkRoutes"] = (
            capo_medialive.types.__list_of_input_request_destination_route.serialize_json(
                value["network_routes"]
            )
        )
    if "static_ip_address" in value:
        out["staticIpAddress"] = value["static_ip_address"]
    return out


def deserialize_json(data: dict) -> InputDestinationRequest:
    out: InputDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("streamName") is not None:
        out["stream_name"] = data["streamName"]
    if data.get("network") is not None:
        out["network"] = data["network"]
    if data.get("networkRoutes") is not None:
        import capo_medialive.types.__list_of_input_request_destination_route

        out["network_routes"] = (
            capo_medialive.types.__list_of_input_request_destination_route.deserialize_json(
                data["networkRoutes"]
            )
        )
    if data.get("staticIpAddress") is not None:
        out["static_ip_address"] = data["staticIpAddress"]
    return out
