"""Generated from Smithy shape ``com.amazonaws.athena#CalculationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.calculation_result_type
    import capo_athena.types.s3_uri


class CalculationResult(TypedDict, closed=True):
    std_out_s3_uri: NotRequired["capo_athena.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 location of the <code>stdout</code> file for the calculation.</p>"""
    std_error_s3_uri: NotRequired["capo_athena.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 location of the <code>stderr</code> error messages file for the calculation.</p>"""
    result_s3_uri: NotRequired["capo_athena.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 location of the folder for the calculation results.</p>"""
    result_type: NotRequired[
        "capo_athena.types.calculation_result_type.CalculationResultType"
    ]
    """<p>The data format of the calculation result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CalculationResult) -> dict:
    out: dict = {}
    if "std_out_s3_uri" in value:
        out["StdOutS3Uri"] = value["std_out_s3_uri"]
    if "std_error_s3_uri" in value:
        out["StdErrorS3Uri"] = value["std_error_s3_uri"]
    if "result_s3_uri" in value:
        out["ResultS3Uri"] = value["result_s3_uri"]
    if "result_type" in value:
        out["ResultType"] = value["result_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CalculationResult:
    out: CalculationResult = {}  # type: ignore[typeddict-item]
    if data.get("StdOutS3Uri") is not None:
        out["std_out_s3_uri"] = data["StdOutS3Uri"]
    if data.get("StdErrorS3Uri") is not None:
        out["std_error_s3_uri"] = data["StdErrorS3Uri"]
    if data.get("ResultS3Uri") is not None:
        out["result_s3_uri"] = data["ResultS3Uri"]
    if data.get("ResultType") is not None:
        out["result_type"] = data["ResultType"]
    return out
