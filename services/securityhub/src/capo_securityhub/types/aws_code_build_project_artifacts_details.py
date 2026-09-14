"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectArtifactsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsCodeBuildProjectArtifactsDetails(TypedDict, closed=True):
    artifact_identifier: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>An identifier for the artifact definition.</p>"""
    encryption_disabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether to disable encryption on the artifact. Only valid when <code>Type</code> is <code>S3</code>.</p>"""
    location: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Only used when <code>Type</code> is <code>S3</code>. The name of the S3 bucket where the artifact is located.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Only used when Type is S3. The name of the artifact. Used with <code>NamepaceType</code> and <code>Path</code> to determine the pattern for storing the artifact.</p>"""
    namespace_type: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Only used when <code>Type</code> is <code>S3</code>. The value to use for the namespace. Used with <code>Name</code> and <code>Path</code> to determine the pattern for storing the artifact.</p>"""
    override_artifact_name: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the name specified in the buildspec file overrides the artifact name.</p>"""
    packaging: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Only used when <code>Type</code> is <code>S3</code>. The type of output artifact to create.</p>"""
    path: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Only used when <code>Type</code> is <code>S3</code>. The path to the artifact. Used with <code>Name</code> and <code>NamespaceType</code> to determine the pattern for storing the artifact.</p>"""
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of build artifact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCodeBuildProjectArtifactsDetails) -> dict:
    out: dict = {}
    if "artifact_identifier" in value:
        out["ArtifactIdentifier"] = value["artifact_identifier"]
    if "encryption_disabled" in value:
        out["EncryptionDisabled"] = value["encryption_disabled"]
    if "location" in value:
        out["Location"] = value["location"]
    if "name" in value:
        out["Name"] = value["name"]
    if "namespace_type" in value:
        out["NamespaceType"] = value["namespace_type"]
    if "override_artifact_name" in value:
        out["OverrideArtifactName"] = value["override_artifact_name"]
    if "packaging" in value:
        out["Packaging"] = value["packaging"]
    if "path" in value:
        out["Path"] = value["path"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsCodeBuildProjectArtifactsDetails:
    out: AwsCodeBuildProjectArtifactsDetails = {}  # type: ignore[typeddict-item]
    if data.get("ArtifactIdentifier") is not None:
        out["artifact_identifier"] = data["ArtifactIdentifier"]
    if data.get("EncryptionDisabled") is not None:
        out["encryption_disabled"] = data["EncryptionDisabled"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("NamespaceType") is not None:
        out["namespace_type"] = data["NamespaceType"]
    if data.get("OverrideArtifactName") is not None:
        out["override_artifact_name"] = data["OverrideArtifactName"]
    if data.get("Packaging") is not None:
        out["packaging"] = data["Packaging"]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    return out
