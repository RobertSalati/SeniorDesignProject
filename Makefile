main: main.py
	python3 main.py

clearphotos: 
	rm ./images/*.jpg

manual: manual.py
	python3 manual.py

motortest: motorTest.py
	python3 motorTest.py

cameratest: cameraTest.py
	python3 cameraTest.py
