# Getting Started

## Installation

```
pip install capo-ssm-guiconnect
```

## Usage

```python
from capo_ssm_guiconnect import AsyncSSMGuiConnectClient


async def main():
    async with AsyncSSMGuiConnectClient() as ssm_gui_connect:
        # Example: call the get_connection_recording_preferences operation
        response = await ssm_gui_connect.get_connection_recording_preferences()
        print(response["client_token"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_ssm_guiconnect import AsyncSSMGuiConnectClient
from capo_ssm_guiconnect.error import AccessDeniedException


async def main():
    async with AsyncSSMGuiConnectClient() as ssm_gui_connect:
        try:
            await ssm_gui_connect.get_connection_recording_preferences()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ssm_guiconnect import AsyncSSMGuiConnectClient


async def main():
    async with AsyncSSMGuiConnectClient() as ssm_gui_connect:
        # Default: 3 attempts for every operation
        response = await ssm_gui_connect.get_connection_recording_preferences()

        # Override per operation
        response = await ssm_gui_connect.get_connection_recording_preferences(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await ssm_gui_connect.get_connection_recording_preferences(config_overrides={"retry_max_attempts": 1})
```
