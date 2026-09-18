"""Generated from Smithy shape ``com.amazonaws.ecrpublic#CreateRepositoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.repository
    import capo_ecr_public.types.repository_catalog_data


class CreateRepositoryResponse(TypedDict, closed=True):
    repository: NotRequired["capo_ecr_public.types.repository.Repository"]
    """<p>The repository that was created.</p>"""
    catalog_data: NotRequired[
        "capo_ecr_public.types.repository_catalog_data.RepositoryCatalogData"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRepositoryResponse) -> dict:
    out: dict = {}
    if "repository" in value:
        import capo_ecr_public.types.repository

        out["repository"] = capo_ecr_public.types.repository.serialize_aws_json_1_1(
            value["repository"]
        )
    if "catalog_data" in value:
        import capo_ecr_public.types.repository_catalog_data

        out["catalogData"] = (
            capo_ecr_public.types.repository_catalog_data.serialize_aws_json_1_1(
                value["catalog_data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRepositoryResponse:
    out: CreateRepositoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("repository") is not None:
        import capo_ecr_public.types.repository

        out["repository"] = capo_ecr_public.types.repository.deserialize_aws_json_1_1(
            data["repository"]
        )
    if data.get("catalogData") is not None:
        import capo_ecr_public.types.repository_catalog_data

        out["catalog_data"] = (
            capo_ecr_public.types.repository_catalog_data.deserialize_aws_json_1_1(
                data["catalogData"]
            )
        )
    return out
