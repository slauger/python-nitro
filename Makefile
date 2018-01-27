all:
	./clear.py
	./config.py put configs/100-bestpractices.json
	./config.py put configs/100-feature_l3mode.json
	./config.py post configs/100-features_default.json
	./config.py post configs/100-ntp.json
	./config.py put configs/100-ssl.json
	./config.py post configs/900-xenmobile.json
	./config.py put configs/901-xenmobile.json
