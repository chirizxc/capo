# Getting Started

## Installation

```
pip install capo-bedrock-agent
```

## Usage

```python
from capo_bedrock_agent import AsyncBedrockAgentClient


async def main():
    async with AsyncBedrockAgentClient() as bedrock_agent:
        # Example: call the create_vpc_configuration operation
        response = await bedrock_agent.create_vpc_configuration()
        print(response["vpc_configuration_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_bedrock_agent import AsyncBedrockAgentClient


async def main():
    async with AsyncBedrockAgentClient() as bedrock_agent:
        # Example: paginate over list_vpc_configurations
        async for item in bedrock_agent.iter_list_vpc_configurations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_bedrock_agent import AsyncBedrockAgentClient
from capo_bedrock_agent.error import AccessDeniedException


async def main():
    async with AsyncBedrockAgentClient() as bedrock_agent:
        try:
            await bedrock_agent.create_vpc_configuration()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_bedrock_agent import AsyncBedrockAgentClient


async def main():
    async with AsyncBedrockAgentClient() as bedrock_agent:
        # Default: 3 attempts for every operation
        response = await bedrock_agent.create_vpc_configuration()

        # Override per operation
        response = await bedrock_agent.create_vpc_configuration(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await bedrock_agent.create_vpc_configuration(config_overrides={"retry_max_attempts": 1})
```
