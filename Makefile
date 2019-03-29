

build-docker:
	docker build -t vdc-app .


push-docker:

chart-lint:
	helm lint ./chart
chart-install:
	helm install ./chart 


