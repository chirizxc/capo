"""Generated from Smithy shape ``com.amazonaws.acm#CertificateOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.certificate_export
    import capo_acm.types.certificate_transparency_logging_preference
    import capo_acm.types.validation_method


class CertificateOptions(TypedDict, closed=True):
    certificate_transparency_logging_preference: NotRequired[
        "capo_acm.types.certificate_transparency_logging_preference.CertificateTransparencyLoggingPreference"
    ]
    """<p>This parameter has been deprecated. Certificate transparency logging opt-out is no longer available. All public certificates are recorded in a certificate transparency log.</p>"""
    export: NotRequired["capo_acm.types.certificate_export.CertificateExport"]
    """<p>You can opt in to allow the export of your certificates by specifying <code>ENABLED</code>. You cannot update the value of <code>Export</code> after the the certificate is created.</p>"""
    validation_method: NotRequired["capo_acm.types.validation_method.ValidationMethod"]
    """<p>The domain validation method for the certificate. To migrate from email to DNS validation, specify <code>DNS</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateOptions) -> dict:
    out: dict = {}
    if "certificate_transparency_logging_preference" in value:
        import capo_acm.types.certificate_transparency_logging_preference

        out["CertificateTransparencyLoggingPreference"] = (
            capo_acm.types.certificate_transparency_logging_preference.serialize_aws_json_1_1(
                value["certificate_transparency_logging_preference"]
            )
        )
    if "export" in value:
        import capo_acm.types.certificate_export

        out["Export"] = capo_acm.types.certificate_export.serialize_aws_json_1_1(
            value["export"]
        )
    if "validation_method" in value:
        import capo_acm.types.validation_method

        out["ValidationMethod"] = (
            capo_acm.types.validation_method.serialize_aws_json_1_1(
                value["validation_method"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateOptions:
    out: CertificateOptions = {}  # type: ignore[typeddict-item]
    if data.get("CertificateTransparencyLoggingPreference") is not None:
        import capo_acm.types.certificate_transparency_logging_preference

        out["certificate_transparency_logging_preference"] = (
            capo_acm.types.certificate_transparency_logging_preference.deserialize_aws_json_1_1(
                data["CertificateTransparencyLoggingPreference"]
            )
        )
    if data.get("Export") is not None:
        import capo_acm.types.certificate_export

        out["export"] = capo_acm.types.certificate_export.deserialize_aws_json_1_1(
            data["Export"]
        )
    if data.get("ValidationMethod") is not None:
        import capo_acm.types.validation_method

        out["validation_method"] = (
            capo_acm.types.validation_method.deserialize_aws_json_1_1(
                data["ValidationMethod"]
            )
        )
    return out
