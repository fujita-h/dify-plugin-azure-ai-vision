import io
from collections.abc import Generator
from typing import Any

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class ReadTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # Ensure runtime and credentials
        if not self.runtime or not self.runtime.credentials:
            raise Exception("Tool runtime or credentials are missing")

        # Get endpoint and api key
        api_endpoint = str(self.runtime.credentials.get("azure_ai_vision_api_endpoint"))
        api_key = str(self.runtime.credentials.get("azure_ai_vision_api_key"))

        # Ensure API key and endpoint are provided
        if not api_key:
            raise Exception("Azure AI Vision API key is missing")
        if not api_endpoint:
            raise Exception("Azure AI Vision API endpoint is missing")

        # Create client
        client = ImageAnalysisClient(
            endpoint=api_endpoint,
            credential=AzureKeyCredential(api_key),
        )

        # Get file
        file = tool_parameters.get("file")
        if not file:
            raise ValueError("File is required")

        # Analyze image
        try:
            file_binary = io.BytesIO(file.blob)
            result = client._analyze_from_image_data(
                image_data=file_binary.getvalue(),
                visual_features=[VisualFeatures.DENSE_CAPTIONS],
            )
            yield self.create_json_message(result.as_dict())

        except Exception as e:
            raise Exception(str(e)) from e
