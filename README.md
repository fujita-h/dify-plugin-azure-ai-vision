![Icon](./_assets/00792-icon-service-Computer-Vision.svg)

# Azure AI Vision

[![GitHub Repo](https://img.shields.io/badge/GitHub_Repo-fujita--h/dify--plugin--azure--ai--vision-blue?logo=github)](https://github.com/fujita-h/dify-plugin-azure-ai-vision)
![GitHub Release](https://img.shields.io/github/v/release/fujita-h/dify-plugin-azure-ai-vision)
![GitHub License](https://img.shields.io/github/license/fujita-h/dify-plugin-azure-ai-vision)

This plugin provides tools for image analysis with OCR and AI using Azure AI Vision.

> [!IMPORTANT]  
> This plugin requires an Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Learn more about the free trial [here](https://azure.microsoft.com/free/).

## Tools provided by this plugin

Discover computer vision insights from image analysis with OCR and AI.

### Caption

he Caption feature generates a one-sentence description of all the image contents.

https://learn.microsoft.com/azure/ai-services/computer-vision/concept-describe-images-40

### Dense Caption

Dense Captions provides more detail by generating one-sentence descriptions of up to 10 different regions of the image in addition to describing the whole image. 

https://learn.microsoft.com/azure/ai-services/computer-vision/concept-describe-images-40

### Object Detection

Object detection returns the bounding box coordinates (in pixels) for each object found in the image. For example, if an image contains a dog, cat, and person, the object detection operation lists those objects with their coordinates in the image.

https://learn.microsoft.com/azure/ai-services/computer-vision/concept-object-detection-40

### People Detection

People detection offers the ability to detect people appearing in images. The bounding box coordinates of each detected person are returned, along with a confidence score.

https://learn.microsoft.com/azure/ai-services/computer-vision/concept-people-detection

### OCR

OCR is a machine-learning-based technique for extracting text from in-the-wild and non-document images like product labels, user-generated images, screenshots, street signs, and posters.

https://learn.microsoft.com/azure/ai-services/computer-vision/concept-ocr

### Smart-Cropping

Smart-Cropping is a reduced-size representation of an image. Smart-Cropping are used to represent images and other data in a more economical, layout-friendly way. The Azure AI Vision 4.0 API uses smart cropping to create intuitive image thumbnails that include the most important regions of an image with priority given to any detected faces.

https://learn.microsoft.com/azure/ai-services/computer-vision/concept-generate-thumbnails-40

### Tags

The tags feature returns content tags for thousands of recognizable objects, living beings, scenery, and actions that appear in images.

https://learn.microsoft.com/azure/ai-services/computer-vision/concept-tag-images-40


## Notes

This plugin uses the Image Analysis API v4.0 of [Azure AI Vision](https://azure.microsoft.com/products/ai-services/ai-vision/). Please refer to the official documentation for more information.

The functionality provided by this plugin is subject to the requirements and limitations of Azure AI Vision.
Please refer to the official documentation for more information.

https://learn.microsoft.com/azure/ai-services/computer-vision/overview

### Input Requirements

Refer to the following page for the input requirements.

https://learn.microsoft.com/azure/ai-services/computer-vision/overview-image-analysis?tabs=4-0#input-requirements

### Region Availability

Image Analysis API v4.0 is limited to the following regions.

https://learn.microsoft.com/azure/ai-services/computer-vision/overview-image-analysis?tabs=4-0#region-availability

### Language Support

You can specify the language for output generation by setting the `language` parameter.
If this parameter is not specified, the default value is "en".
See https://learn.microsoft.com/azure/ai-services/computer-vision/language-support for a list of supported languages.

## Contributing

This plugin is open-source and contributions are welcome. Please visit the GitHub repository to contribute.
