"""Generated from Smithy shape ``com.amazonaws.iot#CreateDomainConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.domain_configuration_arn
    import capo_iot.types.domain_configuration_name


class CreateDomainConfigurationResponse(TypedDict, closed=True):
    domain_configuration_name: NotRequired[
        "capo_iot.types.domain_configuration_name.DomainConfigurationName"
    ]
    """<p>The name of the domain configuration.</p>"""
    domain_configuration_arn: NotRequired[
        "capo_iot.types.domain_configuration_arn.DomainConfigurationArn"
    ]
    """<p>The ARN of the domain configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainConfigurationResponse) -> dict:
    out: dict = {}
    if "domain_configuration_name" in value:
        out["domainConfigurationName"] = value["domain_configuration_name"]
    if "domain_configuration_arn" in value:
        out["domainConfigurationArn"] = value["domain_configuration_arn"]
    return out


def deserialize_json(data: dict) -> CreateDomainConfigurationResponse:
    out: CreateDomainConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("domainConfigurationName") is not None:
        out["domain_configuration_name"] = data["domainConfigurationName"]
    if data.get("domainConfigurationArn") is not None:
        out["domain_configuration_arn"] = data["domainConfigurationArn"]
    return out
