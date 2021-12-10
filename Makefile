main: main.py release.py
	python3 main.py
	python3 release.py

clearphotos: 
	rm ./images/*.jpg

release: release.py
	python3 release.py

manual: manual.py
	python3 manual.py

motortest: motorTest.py
	python3 motorTest.py

cameratest: cameraTest.py
	python3 cameraTest.py

