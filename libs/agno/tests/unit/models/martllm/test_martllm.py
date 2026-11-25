import os
from unittest.mock import patch

import pytest

from agno.exceptions import ModelAuthenticationError
from agno.models.martllm import MartLLM
from agno.models.utils import get_model, get_model_from_dict


def test_martllm_initialization_with_api_key():
    model = MartLLM(id="deepseek/deepseek-v4.1-flash", api_key="test-api-key")
    assert model.id == "deepseek/deepseek-v4.1-flash"
    assert model.api_key == "test-api-key"
    assert model.base_url == "https://api.martllm.com/v1"


def test_martllm_initialization_without_api_key():
    with patch.dict(os.environ, {}, clear=True):
        model = MartLLM(id="deepseek/deepseek-v4.1-flash")
        client_params = None
        with pytest.raises(ModelAuthenticationError):
            client_params = model._get_client_params()
        assert client_params is None


def test_martllm_initialization_with_env_api_key():
    with patch.dict(os.environ, {"MARTLLM_API_KEY": "env-api-key"}):
        model = MartLLM(id="deepseek/deepseek-v4.1-flash")
        assert model.api_key == "env-api-key"


def test_martllm_client_params():
    model = MartLLM(id="deepseek/deepseek-v4.1-flash", api_key="test-api-key")
    client_params = model._get_client_params()
    assert client_params["api_key"] == "test-api-key"
    assert client_params["base_url"] == "https://api.martllm.com/v1"


def test_martllm_default_values():
    model = MartLLM(api_key="test-api-key")
    assert model.id == "deepseek/deepseek-v4.1-flash"
    assert model.name == "MartLLM"
    assert model.provider == "MartLLM"


def test_martllm_resolves_from_string_syntax():
    model = get_model("martllm:deepseek/deepseek-v4.1-flash")
    assert isinstance(model, MartLLM)
    assert model.id == "deepseek/deepseek-v4.1-flash"


def test_martllm_round_trips_through_dict():
    model = MartLLM(id="openai/gpt-4o-mini", api_key="test-api-key")
    rebuilt = get_model_from_dict(model.to_dict())
    assert isinstance(rebuilt, MartLLM)
    assert rebuilt.id == "openai/gpt-4o-mini"
