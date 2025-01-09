![Icon](./_assets/00792-icon-service-Computer-Vision.svg)

# Azure AI Vision

![GitHub Release](https://img.shields.io/github/v/release/fujita-h/dify-plugin-azure-ai-vision)
![GitHub License](https://img.shields.io/github/license/fujita-h/dify-plugin-azure-ai-vision)


This extension provides a set of Azure AI Vision services.

## Tools

### Caption

he Caption feature generates a one-sentence description of all the image contents.

### Dense Caption

Dense Captions provides more detail by generating one-sentence descriptions of up to 10 different regions of the image in addition to describing the whole image. 

### Object Detection

Object detection returns the bounding box coordinates (in pixels) for each object found in the image. For example, if an image contains a dog, cat, and person, the object detection operation lists those objects with their coordinates in the image.

### People Detection

People detection offers the ability to detect people appearing in images. The bounding box coordinates of each detected person are returned, along with a confidence score.

### OCR

OCR is a machine-learning-based technique for extracting text from in-the-wild and non-document images like product labels, user-generated images, screenshots, street signs, and posters.

### Smart-Cropping

Smart-Cropping is a reduced-size representation of an image. Smart-Cropping are used to represent images and other data in a more economical, layout-friendly way. The Azure AI Vision 4.0 API uses smart cropping to create intuitive image thumbnails that include the most important regions of an image with priority given to any detected faces.

### Tags

The tags feature returns content tags for thousands of recognizable objects, living beings, scenery, and actions that appear in images.

## Important Notes

The functionality provided by this plugin is subject to the requirements and limitations of Azure AI Vision.
Please refer to the official documentation for more information.

### Input Requirements

Refer to the following page for the input requirements.

https://learn.microsoft.com/ja-jp/azure/ai-services/computer-vision/overview-image-analysis?tabs=4-0#input-requirements


### Language Support

You can specify the language for output generation by setting the `language` parameter.
If this parameter is not specified, the default value is "en".
See https://learn.microsoft.com/azure/ai-services/computer-vision/language-support for a list of supported languages.
