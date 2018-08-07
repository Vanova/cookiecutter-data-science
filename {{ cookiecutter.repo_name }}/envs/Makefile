help:
	@cat Makefile

DOCKER_NAME={{cookiecutter.repo_name}}_env

# CUDA version settings
GPU?=0
CUDA_VERSION?=8.0
CUDNN_VERSION?=6

# local folders
SRC?=$(cd .. && pwd)
DATA?=~/wrkdir/datasets
# container folders
PROJ?=/wrkdir/project/$(DOCKER_NAME)

DOCKER_FILE=Dockerfile
DOCKER=sudo GPU=$(GPU) nvidia-docker
BACKEND=tensorflow

build:
	docker build --build-arg cuda_version=$(CUDA_VERSION) --build-arg cudnn_version=$(CUDNN_VERSION) \
		-t $(DOCKER_NAME) -f  $(DOCKER_FILE) .

bash: build	
	$(DOCKER) run -it -v $(SRC):$(PROJ) -v $(DATA):/wrkdir/datasets $(DOCKER_NAME) bash

ipython: build
	$(DOCKER) run -it -v $(SRC):$(PROJ) -v $(DATA):/wrkdir/datasets --env KERAS_BACKEND=$(BACKEND) $(DOCKER_NAME) ipython

notebook: build
	$(DOCKER) run -it -v $(SRC):$(PROJ) -v $(DATA):/wrkdir/datasets --net=host --env KERAS_BACKEND=$(BACKEND) $(DOCKER_NAME)

test: build
	$(DOCKER) run -it -v $(SRC):$(PROJ) -v $(DATA):/wrkdir/datasets --env KERAS_BACKEND=$(BACKEND) $(DOCKER_NAME) py.test $(PROJ)

# TODO fix according to project
#task1: build
#       $(DOCKER) run -it -v $(SRC):$(PROJ) $(DOCKER_NAME) /bin/bash -c "python applications/task1.py -s dcase2017,gmm -o; python applications/task1.py -show_eval"

