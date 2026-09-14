"""Generated from Smithy shape ``com.amazonaws.datazone#SparkEmrPropertiesPatch``."""

from typing_extensions import NotRequired, TypedDict


class SparkEmrPropertiesPatch(TypedDict, closed=True):
    compute_arn: NotRequired["str"]
    """<p>The compute ARN in the Spark EMR properties patch.</p>"""
    instance_profile_arn: NotRequired["str"]
    """<p>The instance profile ARN in the Spark EMR properties patch.</p>"""
    java_virtual_env: NotRequired["str"]
    """<p>The Java virtual evn in the Spark EMR properties patch.</p>"""
    log_uri: NotRequired["str"]
    """<p>The log URI in the Spark EMR properties patch.</p>"""
    python_virtual_env: NotRequired["str"]
    """<p>The Python virtual env in the Spark EMR properties patch.</p>"""
    runtime_role: NotRequired["str"]
    """<p>The runtime role in the Spark EMR properties patch.</p>"""
    trusted_certificates_s3_uri: NotRequired["str"]
    """<p>The trusted certificates S3 URI in the Spark EMR properties patch.</p>"""
    managed_endpoint_arn: NotRequired["str"]
    """<p>The managed endpoint ARN of the EMR on EKS cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SparkEmrPropertiesPatch) -> dict:
    out: dict = {}
    if "compute_arn" in value:
        out["computeArn"] = value["compute_arn"]
    if "instance_profile_arn" in value:
        out["instanceProfileArn"] = value["instance_profile_arn"]
    if "java_virtual_env" in value:
        out["javaVirtualEnv"] = value["java_virtual_env"]
    if "log_uri" in value:
        out["logUri"] = value["log_uri"]
    if "python_virtual_env" in value:
        out["pythonVirtualEnv"] = value["python_virtual_env"]
    if "runtime_role" in value:
        out["runtimeRole"] = value["runtime_role"]
    if "trusted_certificates_s3_uri" in value:
        out["trustedCertificatesS3Uri"] = value["trusted_certificates_s3_uri"]
    if "managed_endpoint_arn" in value:
        out["managedEndpointArn"] = value["managed_endpoint_arn"]
    return out


def deserialize_json(data: dict) -> SparkEmrPropertiesPatch:
    out: SparkEmrPropertiesPatch = {}  # type: ignore[typeddict-item]
    if data.get("computeArn") is not None:
        out["compute_arn"] = data["computeArn"]
    if data.get("instanceProfileArn") is not None:
        out["instance_profile_arn"] = data["instanceProfileArn"]
    if data.get("javaVirtualEnv") is not None:
        out["java_virtual_env"] = data["javaVirtualEnv"]
    if data.get("logUri") is not None:
        out["log_uri"] = data["logUri"]
    if data.get("pythonVirtualEnv") is not None:
        out["python_virtual_env"] = data["pythonVirtualEnv"]
    if data.get("runtimeRole") is not None:
        out["runtime_role"] = data["runtimeRole"]
    if data.get("trustedCertificatesS3Uri") is not None:
        out["trusted_certificates_s3_uri"] = data["trustedCertificatesS3Uri"]
    if data.get("managedEndpointArn") is not None:
        out["managed_endpoint_arn"] = data["managedEndpointArn"]
    return out
