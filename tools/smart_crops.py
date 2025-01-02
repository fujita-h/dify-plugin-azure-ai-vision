import io
from collections.abc import Generator
from typing import Any, List

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

        # Get aspect ratios
        smartcrops_aspect_ratios_param: str | None = tool_parameters.get("smartcrops_aspect_ratios") or None
        smartcrops_aspect_ratios: List[float] | None = None
        try:
            if smartcrops_aspect_ratios_param is not None and smartcrops_aspect_ratios_param.strip():
                smartcrops_aspect_ratios = [
                    float(ratio.strip()) for ratio in smartcrops_aspect_ratios_param.strip().split(",")
                ]
        except Exception as e:
            raise ValueError("Invalid smartcrops_aspect_ratios") from e

        # Analyze image
        try:
            file_binary = io.BytesIO(file.blob)
            result = client._analyze_from_image_data(
                image_data=file_binary.getvalue(),
                visual_features=[VisualFeatures.SMART_CROPS],
                smart_crops_aspect_ratios=smartcrops_aspect_ratios,
            )
            yield self.create_json_message(result.as_dict())

        except Exception as e:
            raise Exception(str(e)) from e
