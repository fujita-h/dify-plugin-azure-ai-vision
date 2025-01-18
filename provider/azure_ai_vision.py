from typing import Any

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class AzureAiVisionProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            api_endpoint = credentials.get("api_endpoint")
            api_key = credentials.get("api_key")

            # Ensure API key and endpoint are provided
            if not api_key:
                raise Exception("Azure AI Vision API key is missing")
            if not api_endpoint:
                raise Exception("Azure AI Vision API endpoint is missing")

            client = ImageAnalysisClient(
                endpoint=api_endpoint,
                credential=AzureKeyCredential(api_key),
            )
            try:
                result = client._analyze_from_image_data(b"", visual_features=[VisualFeatures.READ])
                print(result)
            except ClientAuthenticationError as e:
                raise Exception("Azure AI Vision API key is invalid") from e
            except HttpResponseError:
                pass

        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e)) from e
