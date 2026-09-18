# Getting Started

## Installation

```
pip install capo-devops-agent
```

## Usage

```python
from capo_devops_agent import AsyncDevOpsAgentClient


async def main():
    async with AsyncDevOpsAgentClient() as dev_ops_agent:
        # Example: call the create_asset operation
        response = await dev_ops_agent.create_asset()
        print(response["asset"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_devops_agent import AsyncDevOpsAgentClient


async def main():
    async with AsyncDevOpsAgentClient() as dev_ops_agent:
        # Example: paginate over list_asset_files
        async for item in dev_ops_agent.iter_list_asset_files():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_devops_agent import AsyncDevOpsAgentClient
from capo_devops_agent.error import AccessDeniedException


async def main():
    async with AsyncDevOpsAgentClient() as dev_ops_agent:
        try:
            await dev_ops_agent.create_asset()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_devops_agent import AsyncDevOpsAgentClient


async def main():
    async with AsyncDevOpsAgentClient() as dev_ops_agent:
        # Default: 3 attempts for every operation
        response = await dev_ops_agent.create_asset()

        # Override per operation
        response = await dev_ops_agent.create_asset(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await dev_ops_agent.create_asset(config_overrides={"retry_max_attempts": 1})
```
