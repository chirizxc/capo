"""Generated from Smithy shape ``com.amazonaws.securityagent#ProviderInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityagent.types.bitbucket_integration_input
    import capo_securityagent.types.confluence_integration_input
    import capo_securityagent.types.git_hub_integration_input
    import capo_securityagent.types.git_lab_integration_input


class _ProviderInput_github(TypedDict, closed=True):
    github: "capo_securityagent.types.git_hub_integration_input.GitHubIntegrationInput"


class _ProviderInput_gitlab(TypedDict, closed=True):
    gitlab: "capo_securityagent.types.git_lab_integration_input.GitLabIntegrationInput"


class _ProviderInput_bitbucket(TypedDict, closed=True):
    bitbucket: (
        "capo_securityagent.types.bitbucket_integration_input.BitbucketIntegrationInput"
    )


class _ProviderInput_confluence(TypedDict, closed=True):
    confluence: "capo_securityagent.types.confluence_integration_input.ConfluenceIntegrationInput"


ProviderInput: TypeAlias = (
    _ProviderInput_github
    | _ProviderInput_gitlab
    | _ProviderInput_bitbucket
    | _ProviderInput_confluence
)


# --- restJson1 ser/de ---
def serialize_json(value: ProviderInput) -> dict:
    if "github" in value:
        import capo_securityagent.types.git_hub_integration_input

        return {
            "github": capo_securityagent.types.git_hub_integration_input.serialize_json(
                value["github"]
            )
        }
    elif "gitlab" in value:
        import capo_securityagent.types.git_lab_integration_input

        return {
            "gitlab": capo_securityagent.types.git_lab_integration_input.serialize_json(
                value["gitlab"]
            )
        }
    elif "bitbucket" in value:
        import capo_securityagent.types.bitbucket_integration_input

        return {
            "bitbucket": capo_securityagent.types.bitbucket_integration_input.serialize_json(
                value["bitbucket"]
            )
        }
    elif "confluence" in value:
        import capo_securityagent.types.confluence_integration_input

        return {
            "confluence": capo_securityagent.types.confluence_integration_input.serialize_json(
                value["confluence"]
            )
        }
    else:
        raise SerializationError("ProviderInput: no variant present")


def deserialize_json(data: dict) -> ProviderInput:
    if data.get("github") is not None:
        import capo_securityagent.types.git_hub_integration_input

        return {
            "github": capo_securityagent.types.git_hub_integration_input.deserialize_json(
                data["github"]
            )
        }
    elif data.get("gitlab") is not None:
        import capo_securityagent.types.git_lab_integration_input

        return {
            "gitlab": capo_securityagent.types.git_lab_integration_input.deserialize_json(
                data["gitlab"]
            )
        }
    elif data.get("bitbucket") is not None:
        import capo_securityagent.types.bitbucket_integration_input

        return {
            "bitbucket": capo_securityagent.types.bitbucket_integration_input.deserialize_json(
                data["bitbucket"]
            )
        }
    elif data.get("confluence") is not None:
        import capo_securityagent.types.confluence_integration_input

        return {
            "confluence": capo_securityagent.types.confluence_integration_input.deserialize_json(
                data["confluence"]
            )
        }
    else:
        raise DeserializationError("ProviderInput: no recognized variant key")
