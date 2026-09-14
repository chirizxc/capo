"""Generated from Smithy shape ``com.amazonaws.detective#TTPsObservedDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.api_failure_count
    import capo_detective.types.api_name
    import capo_detective.types.api_success_count
    import capo_detective.types.ip_address
    import capo_detective.types.procedure
    import capo_detective.types.tactic
    import capo_detective.types.technique


class TTPsObservedDetail(TypedDict, closed=True):
    tactic: NotRequired["capo_detective.types.tactic.Tactic"]
    """<p>The tactic used, identified by the investigation.</p>"""
    technique: NotRequired["capo_detective.types.technique.Technique"]
    """<p>The technique used, identified by the investigation. </p>"""
    procedure: NotRequired["capo_detective.types.procedure.Procedure"]
    """<p>The procedure used, identified by the investigation.</p>"""
    ip_address: NotRequired["capo_detective.types.ip_address.IpAddress"]
    """<p>The IP address where the tactics, techniques, and procedure (TTP) was observed.</p>"""
    api_name: NotRequired["capo_detective.types.api_name.APIName"]
    """<p>The name of the API where the tactics, techniques, and procedure (TTP) was observed.</p>"""
    api_success_count: "capo_detective.types.api_success_count.APISuccessCount"
    """<p>The total number of successful API requests.</p>"""
    api_failure_count: "capo_detective.types.api_failure_count.APIFailureCount"
    """<p>The total number of failed API requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TTPsObservedDetail) -> dict:
    out: dict = {}
    if "tactic" in value:
        out["Tactic"] = value["tactic"]
    if "technique" in value:
        out["Technique"] = value["technique"]
    if "procedure" in value:
        out["Procedure"] = value["procedure"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "api_name" in value:
        out["APIName"] = value["api_name"]
    out["APISuccessCount"] = value.get("api_success_count", 0)
    out["APIFailureCount"] = value.get("api_failure_count", 0)
    return out


def deserialize_json(data: dict) -> TTPsObservedDetail:
    out: TTPsObservedDetail = {}  # type: ignore[typeddict-item]
    if data.get("Tactic") is not None:
        out["tactic"] = data["Tactic"]
    if data.get("Technique") is not None:
        out["technique"] = data["Technique"]
    if data.get("Procedure") is not None:
        out["procedure"] = data["Procedure"]
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    if data.get("APIName") is not None:
        out["api_name"] = data["APIName"]
    if data.get("APISuccessCount") is not None:
        out["api_success_count"] = data["APISuccessCount"]
    else:
        out["api_success_count"] = 0
    if data.get("APIFailureCount") is not None:
        out["api_failure_count"] = data["APIFailureCount"]
    else:
        out["api_failure_count"] = 0
    return out
