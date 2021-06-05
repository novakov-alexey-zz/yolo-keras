import json
import numpy as np
import onnx
import onnxruntime
from predict import load_image_pixels

model_path = 'models/yolov3.onnx'
model = onnx.load(model_path)
output =[node.name for node in model.graph.output]

input_all = [node.name for node in model.graph.input]
input_initializer =  [node.name for node in model.graph.initializer]
net_feed_input = list(set(input_all)  - set(input_initializer))

print('Inputs: ', net_feed_input)
print('Outputs: ', output)

try:
    onnx.checker.check_model(model)
except onnx.checker.ValidationError as e:
    print('The model is invalid: %s' % e)
else:
    print('The model is valid!')

input_w, input_h = 416, 416
img, w, h = load_image_pixels("zebra.jpg", (input_w, input_h))

session = onnxruntime.InferenceSession(model_path, None)
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name
data = json.dumps({'data': img.tolist()})
data = np.array(json.loads(data)['data']).astype('float32')

result = session.run([output_name], {input_name: data})
print(result[0].shape)
print(result[0][0][0][0])