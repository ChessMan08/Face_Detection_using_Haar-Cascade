# Face Detection with Bounding Boxes using Haar Cascades

## Project Overview

This project focuses on detecting faces in images using Haar cascades, a popular method for real-time object detection. The model identifies faces in images and draws bounding boxes around them. Haar cascades are efficient and have been widely used in various computer vision applications, especially for face detection.

## Table of Contents

- [Introduction](#introduction)
- [Haar Cascades](#haar-cascades)
- [Implementation](#implementation)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Introduction

Face detection is a key step in many computer vision applications, including face recognition, facial expression analysis, and video surveillance. This project utilizes the Haar cascade classifier to detect faces in static images. The classifier is pre-trained and works by scanning the image at different scales to detect faces of varying sizes.

## Haar Cascades

Haar cascades are a machine learning-based approach where a cascade function is trained from a large number of positive (face) and negative (non-face) images. This method is particularly efficient for real-time face detection and is implemented in the OpenCV library.

## Implementation

The implementation steps include:
- **Loading the Haar Cascade Classifier**: The pre-trained Haar cascade for face detection is loaded from OpenCV's library. For this project, we use the `haarcascade_frontalface_default.xml` file, which can be found in the [OpenCV GitHub repository](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml).
- **Image Processing**: Convert the image to grayscale, as Haar cascades work more effectively on single-channel images.
- **Face Detection**: The classifier scans the image at different scales to detect faces and draw bounding boxes around them.
- **Display Results**: The detected faces are highlighted with rectangular boxes in the output image.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/ChessMan08/face-detection-haar-cascades.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare Your Images**: Place the images you want to process in the `images/` directory.
2. **Run the Detection Script**: Use the following command to detect faces in an image.
    ```bash
    python face_detection.py --image images/your-image.jpg
    ```
    
## Results

The face detection model using Haar cascades performs efficiently on images with clear frontal faces. The bounding boxes accurately highlight detected faces, making this approach suitable for real-time applications.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

