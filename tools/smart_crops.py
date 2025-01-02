import io
from collections.abc import Generator
from typing import Any, List

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import CropRegion, ImageBoundingBox, SmartCropsResult, VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.file.file import File
from PIL import Image


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
        file: File | None = tool_parameters.get("file", None)
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

            # Generate croppped images (preview)
            # If failed to generate cropped images, it will NOT raise an exception
            try:
                # Prepare output format
                output_format_extension: str = file.extension or ".jpg"
                match output_format_extension:
                    case ".jpg":
                        output_format = "JPEG"
                    case ".jpeg":
                        output_format = "JPEG"
                    case ".png":
                        output_format = "PNG"
                    case ".gif":
                        output_format = "GIF"
                    case ".bmp":
                        output_format = "BMP"
                    case ".webp":
                        output_format = "WEBP"
                    case ".ico":
                        output_format = "ICO"
                    case ".tiff":
                        output_format = "TIFF"
                    case _:
                        output_format = "JPEG"

                # Get smart crops result
                smart_crops_result: SmartCropsResult | None = result.get("smartCropsResult", None)
                if smart_crops_result:
                    crop_regions: List[CropRegion] = smart_crops_result.get("values", [])
                    for crop_region in crop_regions:
                        image_bounding_box: ImageBoundingBox | None = crop_region.get("boundingBox", None)
                        if not image_bounding_box:
                            continue

                        # Get bounding box
                        h: int | None = image_bounding_box.get("h", None)
                        w: int | None = image_bounding_box.get("w", None)
                        x: int | None = image_bounding_box.get("x", None)
                        y: int | None = image_bounding_box.get("y", None)
                        if h is None or w is None or x is None or y is None:
                            continue

                        # Crop image
                        image = Image.open(file_binary)
                        cropped_image = image.crop((x, y, x + w, y + h))

                        # Special treatment for JPEG
                        if output_format == "JPEG":
                            cropped_image = cropped_image.convert("RGB")

                        # Save image to buffer
                        buffer = io.BytesIO()
                        cropped_image.save(buffer, format="JPEG")

                        yield self.create_blob_message(
                            blob=buffer.getvalue(),
                            meta={"mime_type": file.mime_type},
                        )

            except Exception as e:
                print(str(e))

        except Exception as e:
            raise Exception(str(e)) from e
