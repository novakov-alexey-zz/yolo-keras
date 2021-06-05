# Yolov3 in Keras

Based on [this](https://machinelearningmastery.com/how-to-perform-object-detection-with-yolov3-in-keras/)  article.

## Run

1. Download weights from here: [https://pjreddie.com/media/files/yolov3.weights](https://pjreddie.com/media/files/yolov3.weights) and put them into `yolo-keras/models` directory

2. Run this script to create Keras model:
```bash
python create_model.py
```

3. Run `predict.py` script to predict labels via video stream capture.