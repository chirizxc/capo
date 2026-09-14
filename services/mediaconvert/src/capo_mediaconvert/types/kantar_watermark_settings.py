"""Generated from Smithy shape ``com.amazonaws.mediaconvert#KantarWatermarkSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__double_min0
    import capo_mediaconvert.types.__integer_min0_max2147483647
    import capo_mediaconvert.types.__string_min1_max20
    import capo_mediaconvert.types.__string_min1_max50
    import capo_mediaconvert.types.__string_min1_max50_pattern_azaz09
    import capo_mediaconvert.types.__string_min1_max2048_pattern_arn_az_secretsmanager_wd12_secret_azaz09
    import capo_mediaconvert.types.__string_pattern_https_kantarmedia
    import capo_mediaconvert.types.__string_pattern_s3


class KantarWatermarkSettings(TypedDict, closed=True):
    channel_name: NotRequired[
        "capo_mediaconvert.types.__string_min1_max20.__stringMin1Max20"
    ]
    """Provide an audio channel name from your Kantar audio license."""
    content_reference: NotRequired[
        "capo_mediaconvert.types.__string_min1_max50_pattern_azaz09.__stringMin1Max50PatternAZAZ09"
    ]
    """Specify a unique identifier for Kantar to use for this piece of content."""
    credentials_secret_name: NotRequired[
        "capo_mediaconvert.types.__string_min1_max2048_pattern_arn_az_secretsmanager_wd12_secret_azaz09.__stringMin1Max2048PatternArnAZSecretsmanagerWD12SecretAZAZ09"
    ]
    """Provide the name of the AWS Secrets Manager secret where your Kantar credentials are stored. Note that your MediaConvert service role must provide access to this secret. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/granting-permissions-for-mediaconvert-to-access-secrets-manager-secret.html. For instructions on creating a secret, see https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html, in the AWS Secrets Manager User Guide."""
    file_offset: NotRequired["capo_mediaconvert.types.__double_min0.__doubleMin0"]
    """Optional. Specify an offset, in whole seconds, from the start of your output and the beginning of the watermarking. When you don't specify an offset, Kantar defaults to zero."""
    kantar_license_id: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Provide your Kantar license ID number. You should get this number from Kantar."""
    kantar_server_url: NotRequired[
        "capo_mediaconvert.types.__string_pattern_https_kantarmedia.__stringPatternHttpsKantarmedia"
    ]
    """Provide the HTTPS endpoint to the Kantar server. You should get this endpoint from Kantar."""
    log_destination: NotRequired[
        "capo_mediaconvert.types.__string_pattern_s3.__stringPatternS3"
    ]
    """Optional. Specify the Amazon S3 bucket where you want MediaConvert to store your Kantar watermark XML logs. When you don't specify a bucket, MediaConvert doesn't save these logs. Note that your MediaConvert service role must provide access to this location. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html"""
    metadata3: NotRequired[
        "capo_mediaconvert.types.__string_min1_max50.__stringMin1Max50"
    ]
    """You can optionally use this field to specify the first timestamp that Kantar embeds during watermarking. Kantar suggests that you be very cautious when using this Kantar feature, and that you use it only on channels that are managed specifically for use with this feature by your Audience Measurement Operator. For more information about this feature, contact Kantar technical support."""
    metadata4: NotRequired[
        "capo_mediaconvert.types.__string_min1_max50.__stringMin1Max50"
    ]
    """Additional metadata that MediaConvert sends to Kantar. Maximum length is 50 characters."""
    metadata5: NotRequired[
        "capo_mediaconvert.types.__string_min1_max50.__stringMin1Max50"
    ]
    """Additional metadata that MediaConvert sends to Kantar. Maximum length is 50 characters."""
    metadata6: NotRequired[
        "capo_mediaconvert.types.__string_min1_max50.__stringMin1Max50"
    ]
    """Additional metadata that MediaConvert sends to Kantar. Maximum length is 50 characters."""
    metadata7: NotRequired[
        "capo_mediaconvert.types.__string_min1_max50.__stringMin1Max50"
    ]
    """Additional metadata that MediaConvert sends to Kantar. Maximum length is 50 characters."""
    metadata8: NotRequired[
        "capo_mediaconvert.types.__string_min1_max50.__stringMin1Max50"
    ]
    """Additional metadata that MediaConvert sends to Kantar. Maximum length is 50 characters."""


# --- restJson1 ser/de ---
def serialize_json(value: KantarWatermarkSettings) -> dict:
    out: dict = {}
    if "channel_name" in value:
        out["channelName"] = value["channel_name"]
    if "content_reference" in value:
        out["contentReference"] = value["content_reference"]
    if "credentials_secret_name" in value:
        out["credentialsSecretName"] = value["credentials_secret_name"]
    if "file_offset" in value:
        out["fileOffset"] = (
            "NaN"
            if value["file_offset"] != value["file_offset"]
            else "Infinity"
            if value["file_offset"] == float("inf")
            else "-Infinity"
            if value["file_offset"] == float("-inf")
            else value["file_offset"]
        )
    if "kantar_license_id" in value:
        out["kantarLicenseId"] = value["kantar_license_id"]
    if "kantar_server_url" in value:
        out["kantarServerUrl"] = value["kantar_server_url"]
    if "log_destination" in value:
        out["logDestination"] = value["log_destination"]
    if "metadata3" in value:
        out["metadata3"] = value["metadata3"]
    if "metadata4" in value:
        out["metadata4"] = value["metadata4"]
    if "metadata5" in value:
        out["metadata5"] = value["metadata5"]
    if "metadata6" in value:
        out["metadata6"] = value["metadata6"]
    if "metadata7" in value:
        out["metadata7"] = value["metadata7"]
    if "metadata8" in value:
        out["metadata8"] = value["metadata8"]
    return out


def deserialize_json(data: dict) -> KantarWatermarkSettings:
    out: KantarWatermarkSettings = {}  # type: ignore[typeddict-item]
    if data.get("channelName") is not None:
        out["channel_name"] = data["channelName"]
    if data.get("contentReference") is not None:
        out["content_reference"] = data["contentReference"]
    if data.get("credentialsSecretName") is not None:
        out["credentials_secret_name"] = data["credentialsSecretName"]
    if data.get("fileOffset") is not None:
        out["file_offset"] = float(data["fileOffset"])
    if data.get("kantarLicenseId") is not None:
        out["kantar_license_id"] = data["kantarLicenseId"]
    if data.get("kantarServerUrl") is not None:
        out["kantar_server_url"] = data["kantarServerUrl"]
    if data.get("logDestination") is not None:
        out["log_destination"] = data["logDestination"]
    if data.get("metadata3") is not None:
        out["metadata3"] = data["metadata3"]
    if data.get("metadata4") is not None:
        out["metadata4"] = data["metadata4"]
    if data.get("metadata5") is not None:
        out["metadata5"] = data["metadata5"]
    if data.get("metadata6") is not None:
        out["metadata6"] = data["metadata6"]
    if data.get("metadata7") is not None:
        out["metadata7"] = data["metadata7"]
    if data.get("metadata8") is not None:
        out["metadata8"] = data["metadata8"]
    return out
