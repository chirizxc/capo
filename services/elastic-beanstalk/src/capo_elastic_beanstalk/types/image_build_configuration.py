"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ImageBuildConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.architecture_type
    import capo_elastic_beanstalk.types.boxed_int
    import capo_elastic_beanstalk.types.compute_type
    import capo_elastic_beanstalk.types.image_build_type
    import capo_elastic_beanstalk.types.non_empty_string
    import capo_elastic_beanstalk.types.string


class ImageBuildConfiguration(TypedDict, closed=True):
    type: NotRequired["capo_elastic_beanstalk.types.image_build_type.ImageBuildType"]
    """<p>How Elastic Beanstalk builds the container image. Elastic Beanstalk rejects a <code>Build</code> that doesn't specify it.</p> <p>Valid values:</p> <ul> <li> <p> <code>docker</code> – Elastic Beanstalk builds the image from a Dockerfile in your source bundle. Specify the Dockerfile with <code>DockerfileLocation</code>.</p> </li> <li> <p> <code>buildpack</code> – Elastic Beanstalk builds the image with a Cloud Native Buildpacks builder. Specify the builder with <code>Buildpack</code>.</p> </li> </ul>"""
    dockerfile_location: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The path to the Dockerfile within the source bundle, relative to the root of the source bundle. For example, <code>backend/Dockerfile</code>.</p> <p>Elastic Beanstalk uses this member only when <code>Type</code> is <code>docker</code>. If you don't specify it, Elastic Beanstalk uses the Dockerfile at the root of the source bundle.</p>"""
    buildpack: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The Cloud Native Buildpacks builder image that Elastic Beanstalk uses to build the container image. For example, <code>paketobuildpacks/builder-jammy-base</code>.</p> <p>This member is required when <code>Type</code> is <code>buildpack</code>. Elastic Beanstalk doesn't provide a default builder.</p>"""
    architecture: NotRequired[
        "capo_elastic_beanstalk.types.architecture_type.ArchitectureType"
    ]
    """<p>The processor architecture that Elastic Beanstalk builds the container image for. The architecture must match the architecture of the instances in the environment that you deploy the application version to.</p> <p>Valid values:</p> <ul> <li> <p> <code>amd64</code> – x86-64 instances. This is the default.</p> </li> <li> <p> <code>arm64</code> – Amazon Web Services Graviton instances.</p> </li> </ul>"""
    code_build_service_role: NotRequired[
        "capo_elastic_beanstalk.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that CodeBuild assumes to run the build in your Amazon Web Services account. Elastic Beanstalk rejects a <code>Build</code> that doesn't specify this role.</p>"""
    compute_type: NotRequired["capo_elastic_beanstalk.types.compute_type.ComputeType"]
    """<p>The size of the compute resources that run the build. If you don't specify it, Elastic Beanstalk uses <code>BUILD_GENERAL1_MEDIUM</code>.</p> <p>Valid values:</p> <ul> <li> <p> <code>BUILD_GENERAL1_SMALL</code> – Use up to 3 GB memory and 2 vCPUs for builds.</p> </li> <li> <p> <code>BUILD_GENERAL1_MEDIUM</code> – Use up to 7 GB memory and 4 vCPUs for builds.</p> </li> <li> <p> <code>BUILD_GENERAL1_LARGE</code> – Use up to 15 GB memory and 8 vCPUs for builds.</p> </li> </ul>"""
    timeout_in_minutes: NotRequired["capo_elastic_beanstalk.types.boxed_int.BoxedInt"]
    """<p>How long, in minutes from 5 to 480 (8 hours), Elastic Beanstalk waits before stopping a build that hasn't completed. The default is 60 minutes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ImageBuildConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type" in value:
        import capo_elastic_beanstalk.types.image_build_type

        capo_elastic_beanstalk.types.image_build_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "dockerfile_location" in value:
        pairs.append(
            (f"{key_prefix}DockerfileLocation", str(value["dockerfile_location"]))
        )
    if "buildpack" in value:
        pairs.append((f"{key_prefix}Buildpack", str(value["buildpack"])))
    if "architecture" in value:
        import capo_elastic_beanstalk.types.architecture_type

        capo_elastic_beanstalk.types.architecture_type.serialize_query(
            value["architecture"], pairs, f"{key_prefix}Architecture"
        )
    if "code_build_service_role" in value:
        pairs.append(
            (f"{key_prefix}CodeBuildServiceRole", str(value["code_build_service_role"]))
        )
    if "compute_type" in value:
        import capo_elastic_beanstalk.types.compute_type

        capo_elastic_beanstalk.types.compute_type.serialize_query(
            value["compute_type"], pairs, f"{key_prefix}ComputeType"
        )
    if "timeout_in_minutes" in value:
        pairs.append(
            (f"{key_prefix}TimeoutInMinutes", str(value["timeout_in_minutes"]))
        )


def deserialize_query(el: Element) -> ImageBuildConfiguration:
    out: ImageBuildConfiguration = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_elastic_beanstalk.types.image_build_type

        out["type"] = capo_elastic_beanstalk.types.image_build_type.deserialize_query(
            child_type
        )
    child_dockerfile_location = el.find("DockerfileLocation")
    if child_dockerfile_location is not None:
        out["dockerfile_location"] = str(child_dockerfile_location.text or "")
    child_buildpack = el.find("Buildpack")
    if child_buildpack is not None:
        out["buildpack"] = str(child_buildpack.text or "")
    child_architecture = el.find("Architecture")
    if child_architecture is not None:
        import capo_elastic_beanstalk.types.architecture_type

        out["architecture"] = (
            capo_elastic_beanstalk.types.architecture_type.deserialize_query(
                child_architecture
            )
        )
    child_code_build_service_role = el.find("CodeBuildServiceRole")
    if child_code_build_service_role is not None:
        out["code_build_service_role"] = str(child_code_build_service_role.text or "")
    child_compute_type = el.find("ComputeType")
    if child_compute_type is not None:
        import capo_elastic_beanstalk.types.compute_type

        out["compute_type"] = (
            capo_elastic_beanstalk.types.compute_type.deserialize_query(
                child_compute_type
            )
        )
    child_timeout_in_minutes = el.find("TimeoutInMinutes")
    if child_timeout_in_minutes is not None:
        out["timeout_in_minutes"] = int(child_timeout_in_minutes.text or "")
    return out
