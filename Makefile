main: main.py release.py
	python3 ~/SeniorDesignProject/main.py
	python3 ~/SeniorDesignProject/release.py

clearphotos: 
	rm ~/SeniorDesignProject/images/*.jpg

release: release.py
	python3 ~/SeniorDesignProject/release.py

manual: manual.py
	python3 ~/SeniorDesignProject/manual.py

motortest: motorTest.py
	python3 ~/SeniorDesignProject/motorTest.py

cameratest: cameraTest.py
	python3 ~/SeniorDesignProject/cameraTest.py