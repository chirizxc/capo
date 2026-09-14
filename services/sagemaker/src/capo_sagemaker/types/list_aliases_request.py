"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAliasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.image_name
    import capo_sagemaker.types.image_version_number
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sage_maker_image_version_alias


class ListAliasesRequest(TypedDict, closed=True):
    image_name: NotRequired["capo_sagemaker.types.image_name.ImageName"]
    """<p>The name of the image.</p>"""
    alias: NotRequired[
        "capo_sagemaker.types.sage_maker_image_version_alias.SageMakerImageVersionAlias"
    ]
    """<p>The alias of the image version.</p>"""
    version: NotRequired["capo_sagemaker.types.image_version_number.ImageVersionNumber"]
    """<p>The version of the image. If image version is not specified, the aliases of all versions of the image are listed.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of aliases to return.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the previous call to <code>ListAliases</code> didn't return the full set of aliases, the call returns a token for retrieving the next set of aliases.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAliasesRequest) -> dict:
    out: dict = {}
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    if "alias" in value:
        out["Alias"] = value["alias"]
    if "version" in value:
        out["Version"] = value["version"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAliasesRequest:
    out: ListAliasesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ImageName") is not None:
        out["image_name"] = data["ImageName"]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
