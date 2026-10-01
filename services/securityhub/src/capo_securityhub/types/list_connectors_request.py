"""Generated from Smithy shape ``com.amazonaws.securityhub#ListConnectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.cspm_connector_provider_name
    import capo_securityhub.types.cspm_connector_status
    import capo_securityhub.types.cspm_enablement_status
    import capo_securityhub.types.max_results
    import capo_securityhub.types.next_token


class ListConnectorsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to request the next page of results.</p>"""
    max_results: NotRequired["capo_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    provider_name: NotRequired[
        "capo_securityhub.types.cspm_connector_provider_name.CspmConnectorProviderName"
    ]
    """<p>The name of the cloud provider to filter connectors by.</p>"""
    connector_status: NotRequired[
        "capo_securityhub.types.cspm_connector_status.CspmConnectorStatus"
    ]
    """<p>The connectivity status to filter connectors by.</p>"""
    enablement_status: NotRequired[
        "capo_securityhub.types.cspm_enablement_status.CspmEnablementStatus"
    ]
    """<p>The enablement status to filter connectors by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConnectorsRequest:
    out: ListConnectorsRequest = {}  # type: ignore[typeddict-item]
    return out
