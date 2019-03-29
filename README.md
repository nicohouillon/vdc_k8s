# vdc_k8s
## technical assignment

This test should demonstrate the creation of a simple service and the automation necessary to
package and deploy it to a Kubernetes cluster. Submit a tarball or hosted code repo that we can
access to check out your work!

## Task

Build a simple REST-based python application (a 'hello world' app is fine)
Build a Dockerfile that builds a working image
Create a Helm chart for the application that:
* Defines a deployment 2 or more pods
* Defines a health check on the deployment that makes sure /health is responding
with a 200
* Defines a kubernetes service using ClusterIP
* Defines a kubernetes ingress to allow traffic on to the pods

*(You may manually set up ingress on your laptop, but you must provide instructions th at
get it working on a clean k8s cluster).*

Create a script (either a standalone script or using Make, Rake, etc..) that automates building
and deploying the application to a k8s cluster.

The script should include the following options for performing the specific subtasks of an end-
to-end deployment:

* Build
* Local unit or integration tests
* Package
* Deploy
* Smoke test


### commands: 
* docker:  
build the image : `docker build -t vdc-app:v1 .`  
verify the image is there : `docker images`  
run the container locally : ` docker run -p 8081:8081 vdc-app:v1`  
 


