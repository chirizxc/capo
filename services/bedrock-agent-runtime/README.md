# Getting Started

## Installation

```
pip install capo-bedrock-agent-runtime
```

## Usage

```python
from capo_bedrock_agent_runtime import AsyncBedrockAgentRuntimeClient


async def main():
    async with AsyncBedrockAgentRuntimeClient() as bedrock_agent_runtime:
        # Example: call the get_execution_flow_snapshot operation
        response = await bedrock_agent_runtime.get_execution_flow_snapshot()
        print(response["flow_identifier"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_bedrock_agent_runtime import AsyncBedrockAgentRuntimeClient


async def main():
    async with AsyncBedrockAgentRuntimeClient() as bedrock_agent_runtime:
        # Example: paginate over list_flow_execution_events
        async for item in bedrock_agent_runtime.iter_list_flow_execution_events():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_bedrock_agent_runtime import AsyncBedrockAgentRuntimeClient
from capo_bedrock_agent_runtime.error import AccessDeniedException


async def main():
    async with AsyncBedrockAgentRuntimeClient() as bedrock_agent_runtime:
        try:
            await bedrock_agent_runtime.get_execution_flow_snapshot()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_bedrock_agent_runtime import AsyncBedrockAgentRuntimeClient


async def main():
    async with AsyncBedrockAgentRuntimeClient() as bedrock_agent_runtime:
        # Default: 3 attempts for every operation
        response = await bedrock_agent_runtime.get_execution_flow_snapshot()

        # Override per operation
        response = await bedrock_agent_runtime.get_execution_flow_snapshot(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await bedrock_agent_runtime.get_execution_flow_snapshot(config_overrides={"retry_max_attempts": 1})
```
