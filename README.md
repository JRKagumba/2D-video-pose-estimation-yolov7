# YOLOv7 2D Video Pose Estimation

## Overview

This project project is an attempt at a refined version of the [NFL Combine - 2D Video Running Analysis](https://github.com/JRKagumba/2D-video-based-running-analysis). There were issues with defining the specific subject to perform inference on within each frame of video. As well as issues with performing inference with OpenPose. This project aims to resolve both of these issues by using YOLOv7 Pose Estimation algorithm as well as video datasets with only 1 person running in each frame. 

## Goals

1. Develop a working model
2. Deploy a web application to allow for live interaction
3. Configure a mobile application to allow for real-time gait event detection

## Datasets

The project uses publicly available running footage found from YouTube. At the time of writing this, the datasets consist of 29 treadmill running clips and 17 on ground running clips mainly filmed from a saggital view.  **Finding good, publicly available, running videos shot at a saggital view is proving to be quite challenging**

## About YOLOv7 Pose

"You Only Look Once" Pose Estimation

Keypoint Map: 
- (5,7,9) ==> Right Arm 
- (6,8,10) ==> Left Arm
- (11,13,15) ==> Right Leg
- (12,14,16) ==> Left Leg

![keypoint_yolo](https://user-images.githubusercontent.com/63820705/192370409-6604d59a-646b-493a-ba43-e6525633c249.jpg)


Pose estimation implimentation is based on [YOLO-Pose](https://arxiv.org/abs/2204.06806). 

### Dataset preparison

[[Keypoints Labels of MS COCO 2017]](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/coco2017labels-keypoints.zip)


### Citation

```
@article{wang2022yolov7,
  title={{YOLOv7}: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors},
  author={Wang, Chien-Yao and Bochkovskiy, Alexey and Liao, Hong-Yuan Mark},
  journal={arXiv preprint arXiv:2207.02696},
  year={2022}
}
```

### Acknowledgements

<details><summary> <b>Expand</b> </summary>

* [https://github.com/AlexeyAB/darknet](https://github.com/AlexeyAB/darknet)
* [https://github.com/WongKinYiu/yolor](https://github.com/WongKinYiu/yolor)
* [https://github.com/WongKinYiu/PyTorch_YOLOv4](https://github.com/WongKinYiu/PyTorch_YOLOv4)
* [https://github.com/WongKinYiu/ScaledYOLOv4](https://github.com/WongKinYiu/ScaledYOLOv4)
* [https://github.com/Megvii-BaseDetection/YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)
* [https://github.com/ultralytics/yolov3](https://github.com/ultralytics/yolov3)
* [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
* [https://github.com/DingXiaoH/RepVGG](https://github.com/DingXiaoH/RepVGG)
* [https://github.com/JUGGHM/OREPA_CVPR2022](https://github.com/JUGGHM/OREPA_CVPR2022)
* [https://github.com/TexasInstruments/edgeai-yolov5/tree/yolo-pose](https://github.com/TexasInstruments/edgeai-yolov5/tree/yolo-pose)

</details>
