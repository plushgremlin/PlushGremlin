
import logging_basics
import subprocess
import logging

# Initialize logger
log = logging.getLogger(__name__)

"""
Key Tools: 
- Docker: Containerization tool that allows you to package your application and its dependencies into a container
- Minikube (Kubernetes): imitates Kube in local environment 
"""
log.info("Container focus will be on minikube & docker tools")
subprocess.run("which docker", shell=True)
subprocess.run("which minikube", shell=True)

