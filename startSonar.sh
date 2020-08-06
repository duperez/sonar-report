container_name="sonarqube"

if [ "$( docker container inspect -f '{{.State.Running}}' dockers_sonarqube_1 )" == "false" ]; then
    docker run -d -p 9000:9000 sonarqube
else
    echo "DOCKER RUNNING"
fi