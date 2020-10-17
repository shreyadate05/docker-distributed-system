Run the following command to start the system:
docker-compose up --build --scale slave=<number_of_slaves>

To check slave logs, run the command:
docker-compose logs slave

To check master logs, run the command:
docker-compose logs master

To check status of the containers, run the command:
docker-compose ps
