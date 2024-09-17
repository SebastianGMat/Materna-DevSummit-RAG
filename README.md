# Quick Setup

## 0. Requirements

- Docker
- Python: Make sure to install a compatible Python version to run this project from 
https://www.python.org/downloads/ - the project was developed using Python 3.12

## 1. Set up necessary docker containers

In the base directory of the project run the following command to set up the 
docker containers needed for this project:

```sh
docker compose up
```

This command creates the following containers

- etcd: A key value store needed for running milvus
- minio: A data store needed for running milvus
- milvus: The vector database used for this project
- attu: A GUI tool to explore milvus data


## 2. Set up Python

1. Create a new virtual environment to run the project in with the following 
command:
```sh
python -m venv .venv
```

2. Install required dependencies:
```sh
python -m pip install -r requirements.txt
```


## 3. Set up project configuration

- [TODO] Dotenv


## 4. Initial database setup

1. Download the base data from https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots - you might have to create a free account - extract it and place it in `./data/movies.csv`

2. Create the vector database by running the following command. This might take a while.
```sh
python ./src/create_database.py
```





