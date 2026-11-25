from dataclasses import dataclass, field
from os import getenv
from typing import Any, Dict, Optional

from agno.exceptions import ModelAuthenticationError
from agno.models.openai.like import OpenAILike


@dataclass
class MartLLM(OpenAILike):
    """
    A class for interacting with MartLLM, a marketplace of third-party sellers behind one
    OpenAI-compatible API.

    Attributes:
        id (str): The id of the MartLLM model to use. Default is "deepseek/deepseek-v4.1-flash".
        name (str): The name of this chat model instance. Default is "MartLLM".
        provider (str): The provider of the model. Default is "MartLLM".
        api_key (str): The api key to authorize request to MartLLM.
        base_url (str): The base url to which the requests are sent. Defaults to "https://api.martllm.com/v1".
    """

    id: str = "deepseek/deepseek-v4.1-flash"
    name: str = "MartLLM"
    provider: str = "MartLLM"
    api_key: Optional[str] = field(default_factory=lambda: getenv("MARTLLM_API_KEY"))
    base_url: str = "https://api.martllm.com/v1"

    def _get_client_params(self) -> Dict[str, Any]:
        """
        Returns client parameters for API requests, checking for MARTLLM_API_KEY.

        Returns:
            Dict[str, Any]: A dictionary of client parameters for API requests.
        """
        if not self.api_key:
            self.api_key = getenv("MARTLLM_API_KEY")
            if not self.api_key:
                raise ModelAuthenticationError(
                    message="MARTLLM_API_KEY not set. Please set the MARTLLM_API_KEY environment variable.",
                    model_name=self.name,
                )
        return super()._get_client_params()
