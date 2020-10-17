# Same thing than the 'server' Dockerfile.
FROM python:latest

# Same thing than the 'server' Dockerfile.
# We import 'client.py' in '/client/' folder.
ADD slave.py /slave/

RUN pip uninstall bson
RUN pip uninstall pymongo
RUN pip install pymongo

# I would like to introduce something new, the 'WORKDIR' command.
# This command changes the base directory of your image.
# Here we define '/client/' as base directory.
WORKDIR /slave/