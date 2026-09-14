"""Generated from Smithy shape ``com.amazonaws.devicefarm#Problem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.device
    import capo_device_farm.types.execution_result
    import capo_device_farm.types.message
    import capo_device_farm.types.problem_detail


class Problem(TypedDict, closed=True):
    run: NotRequired["capo_device_farm.types.problem_detail.ProblemDetail"]
    """<p>Information about the associated run.</p>"""
    job: NotRequired["capo_device_farm.types.problem_detail.ProblemDetail"]
    """<p>Information about the associated job.</p>"""
    suite: NotRequired["capo_device_farm.types.problem_detail.ProblemDetail"]
    """<p>Information about the associated suite.</p>"""
    test: NotRequired["capo_device_farm.types.problem_detail.ProblemDetail"]
    """<p>Information about the associated test.</p>"""
    device: NotRequired["capo_device_farm.types.device.Device"]
    """<p>Information about the associated device.</p>"""
    result: NotRequired["capo_device_farm.types.execution_result.ExecutionResult"]
    """<p>The problem's result.</p> <p>Allowed values include:</p> <ul> <li> <p>PENDING</p> </li> <li> <p>PASSED</p> </li> <li> <p>WARNED</p> </li> <li> <p>FAILED</p> </li> <li> <p>SKIPPED</p> </li> <li> <p>ERRORED</p> </li> <li> <p>STOPPED</p> </li> </ul>"""
    message: NotRequired["capo_device_farm.types.message.Message"]
    """<p>A message about the problem's result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Problem) -> dict:
    out: dict = {}
    if "run" in value:
        import capo_device_farm.types.problem_detail

        out["run"] = capo_device_farm.types.problem_detail.serialize_aws_json_1_1(
            value["run"]
        )
    if "job" in value:
        import capo_device_farm.types.problem_detail

        out["job"] = capo_device_farm.types.problem_detail.serialize_aws_json_1_1(
            value["job"]
        )
    if "suite" in value:
        import capo_device_farm.types.problem_detail

        out["suite"] = capo_device_farm.types.problem_detail.serialize_aws_json_1_1(
            value["suite"]
        )
    if "test" in value:
        import capo_device_farm.types.problem_detail

        out["test"] = capo_device_farm.types.problem_detail.serialize_aws_json_1_1(
            value["test"]
        )
    if "device" in value:
        import capo_device_farm.types.device

        out["device"] = capo_device_farm.types.device.serialize_aws_json_1_1(
            value["device"]
        )
    if "result" in value:
        import capo_device_farm.types.execution_result

        out["result"] = capo_device_farm.types.execution_result.serialize_aws_json_1_1(
            value["result"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Problem:
    out: Problem = {}  # type: ignore[typeddict-item]
    if data.get("run") is not None:
        import capo_device_farm.types.problem_detail

        out["run"] = capo_device_farm.types.problem_detail.deserialize_aws_json_1_1(
            data["run"]
        )
    if data.get("job") is not None:
        import capo_device_farm.types.problem_detail

        out["job"] = capo_device_farm.types.problem_detail.deserialize_aws_json_1_1(
            data["job"]
        )
    if data.get("suite") is not None:
        import capo_device_farm.types.problem_detail

        out["suite"] = capo_device_farm.types.problem_detail.deserialize_aws_json_1_1(
            data["suite"]
        )
    if data.get("test") is not None:
        import capo_device_farm.types.problem_detail

        out["test"] = capo_device_farm.types.problem_detail.deserialize_aws_json_1_1(
            data["test"]
        )
    if data.get("device") is not None:
        import capo_device_farm.types.device

        out["device"] = capo_device_farm.types.device.deserialize_aws_json_1_1(
            data["device"]
        )
    if data.get("result") is not None:
        import capo_device_farm.types.execution_result

        out["result"] = (
            capo_device_farm.types.execution_result.deserialize_aws_json_1_1(
                data["result"]
            )
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
