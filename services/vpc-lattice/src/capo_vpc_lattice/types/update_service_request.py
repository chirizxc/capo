"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.auth_type
    import capo_vpc_lattice.types.certificate_arn
    import capo_vpc_lattice.types.idle_timeout_seconds
    import capo_vpc_lattice.types.service_identifier


class UpdateServiceRequest(TypedDict, closed=True):
    service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    certificate_arn: NotRequired[
        "capo_vpc_lattice.types.certificate_arn.CertificateArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the certificate.</p>"""
    auth_type: NotRequired["capo_vpc_lattice.types.auth_type.AuthType"]
    """<p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>"""
    idle_timeout_seconds: NotRequired[
        "capo_vpc_lattice.types.idle_timeout_seconds.IdleTimeoutSeconds"
    ]
    """<p>The amount of time, in seconds, that a connection can remain idle (no data sent) before VPC Lattice closes it. The valid range is 60 to 600 seconds. If you don't specify a value, the default is 60 seconds. This setting does not change the maximum connection duration of 10 minutes; connections are still closed when they reach that limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceRequest) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "auth_type" in value:
        out["authType"] = value["auth_type"]
    if "idle_timeout_seconds" in value:
        out["idleTimeoutSeconds"] = value["idle_timeout_seconds"]
    return out


def deserialize_json(data: dict) -> UpdateServiceRequest:
    out: UpdateServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("certificateArn") is not None:
        out["certificate_arn"] = data["certificateArn"]
    if data.get("authType") is not None:
        out["auth_type"] = data["authType"]
    if data.get("idleTimeoutSeconds") is not None:
        out["idle_timeout_seconds"] = data["idleTimeoutSeconds"]
    return out
