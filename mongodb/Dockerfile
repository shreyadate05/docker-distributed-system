# Same thing than the 'server' Dockerfile.
FROM mongo:latest

# Same thing than the 'server' Dockerfile.
# We import 'mongo.py' in '/mongodb/' folder.
ADD mongo.py /mongodb/
ADD modules.txt /mongodb/

# install Python 3
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get -y install python3.7-dev
RUN pip3 install -r ./mongodb/modules.txt

EXPOSE 27017

# I would like to introduce something new, the 'WORKDIR' command.
# This command changes the base directory of your image.
# Here we define '/mongodb/' as base directory.
WORKDIR /mongodb/