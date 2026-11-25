# MartLLM Cookbook

This cookbook demonstrates how to use MartLLM with the Agno framework. MartLLM is a marketplace
of third-party sellers behind one OpenAI-compatible API: each request is sent to a third-party
provider that serves the requested model. It is not run by, or affiliated with, the makers of
the models it lists.

> **Prerequisites**: Fork and clone this repository if needed

## Quick Start

### 1. Create and activate a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Export your `MARTLLM_API_KEY`

Get your API key from: https://martllm.com/signup

```shell
export MARTLLM_API_KEY=***
```

### 3. Install libraries

```shell
uv pip install -U openai agno
```

### 4. Run basic Agent

```shell
python cookbook/90_models/martllm/basic.py
```

### 5. Run Agent with Tools

```shell
python cookbook/90_models/martllm/tool_use.py
```

## Model Ids

Model ids have the form `<maker>/<model>`. The current list, with context lengths, prices and
whether a model supports tools, vision or reasoning, is at `GET /v1/models` (no key needed).
A few examples:

- `deepseek/deepseek-v4.1-flash` (default): supports tool calls
- `openai/gpt-4o-mini`
- `anthropic/claude-haiku-4.5`
- `google/gemini-2.5-flash`

The list changes, so read it from `/v1/models` rather than hardcoding it.

## Resources & Support

- [Website](https://martllm.com)
- [Quickstart](https://martllm.com/docs/quickstart)
- [How it works: where the capacity comes from](https://martllm.com/how-it-works)
- [Get API Key](https://martllm.com/signup)
- **Base URL**: `https://api.martllm.com/v1`
- **Models Endpoint**: `https://api.martllm.com/v1/models`
