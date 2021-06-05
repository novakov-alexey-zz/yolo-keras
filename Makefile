install:
	python3 -m venv yolokeras	
	source yolokeras/bin/activate
	python3 -m pip install -r requirements.txt

save-2-onnx:	
	python3 -m tf2onnx.convert --saved-model models/yolov3 --output models/yolov3.onnx --tag serve --verbose	 	