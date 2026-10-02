"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.application_id
    import capo_iotsitewise.types.application_name
    import capo_iotsitewise.types.application_status
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.dns_subdomain


class CreateApplicationResponse(TypedDict, closed=True):
    arn: "capo_iotsitewise.types.arn.ARN"
    """<p>ARN of the application</p>"""
    id: "capo_iotsitewise.types.application_id.ApplicationId"
    """<p>Unique identifier of the application</p>"""
    dns_subdomain: "capo_iotsitewise.types.dns_subdomain.DnsSubdomain"
    """<p>DNS subdomain for the application</p>"""
    name: "capo_iotsitewise.types.application_name.ApplicationName"
    """<p>Name of the application</p>"""
    status: "capo_iotsitewise.types.application_status.ApplicationStatus"
    """<p>Current status of the application</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["dnsSubdomain"] = value["dns_subdomain"]
    out["name"] = value["name"]
    import capo_iotsitewise.types.application_status

    out["status"] = capo_iotsitewise.types.application_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateApplicationResponse.arn required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateApplicationResponse.id required")
    if data.get("dnsSubdomain") is not None:
        out["dns_subdomain"] = data["dnsSubdomain"]
    else:
        raise DeserializationError("CreateApplicationResponse.dns_subdomain required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateApplicationResponse.name required")
    if data.get("status") is not None:
        import capo_iotsitewise.types.application_status

        out["status"] = capo_iotsitewise.types.application_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateApplicationResponse.status required")
    return out
