"""Generated from Smithy shape ``com.amazonaws.proton#ListDeploymentsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.max_page_results
    import capo_proton.types.next_token
    import capo_proton.types.resource_name


class ListDeploymentsInput(TypedDict, closed=True):
    next_token: NotRequired["capo_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next deployment in the array of deployment, after the list of deployment that was previously requested.</p>"""
    environment_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of an environment for result list filtering. Proton returns deployments associated with the environment.</p>"""
    service_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of a service for result list filtering. Proton returns deployments associated with service instances of the service.</p>"""
    service_instance_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of a service instance for result list filtering. Proton returns the deployments associated with the service instance.</p>"""
    component_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of a component for result list filtering. Proton returns deployments associated with that component.</p>"""
    max_results: NotRequired["capo_proton.types.max_page_results.MaxPageResults"]
    """<p>The maximum number of deployments to list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDeploymentsInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "environment_name" in value:
        out["environmentName"] = value["environment_name"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDeploymentsInput:
    out: ListDeploymentsInput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("serviceInstanceName") is not None:
        out["service_instance_name"] = data["serviceInstanceName"]
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
