# Set the base image to Ubuntu
FROM ubuntu

# Same thing than the 'server' Dockerfile.
# We import 'mongo.py' in '/mongodb/' folder.
ADD mongo.py /mongodb/
ADD modules.txt /mongodb/


# Update the repository sources list and install gnupg2
RUN apt-get update && apt-get install -y gnupg2

# Add the package verification key
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10

# Add MongoDB to the repository sources list
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > tee /etc/apt/sources.list.d/mongodb.list

# Update the repository sources list
RUN apt-get update

# Install MongoDB package (.deb)
RUN apt-get install -y mongodb

# Create the default data directory
RUN mkdir -p /data/db

# install Python 3
RUN apt-get install -y python3 python3-pip
RUN pip3 install -r ./mongodb/modules.txt

# Expose the default port
EXPOSE 27017

# Default port to execute the entrypoint (MongoDB)
CMD ["--port 27017", "mongod"]

WORKDIR /mongodb/