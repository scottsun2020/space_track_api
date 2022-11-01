# space_track_api
using a API script in Python to read the satalite data through space-track.org
using Docker to create a container environment for API script

Docker Commands:

docker build -t python-api.

docker run -it python-api

To locate output in default docker system:
\\wsl$\docker-desktop-data\data\...


Saving output data from Docker file system to local file system:
option1: Bind Mount:
docker run -v ${PWD}:/app python-api

option2: Volume:
a. create a volume first:
docker volume create --driver local -o o=bind -o type=none -o device="C:\Users\your_file_location\storage" your_volume

b. run docker command:
docker run -v your_volume:/app python-api
