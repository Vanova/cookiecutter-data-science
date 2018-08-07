# Environment: Conda, Python, Tensorflow, Keras
MAINTAINER Ivan Kukanov <ivan@kukanov.com>

ARG cuda_version=8.0
ARG cudnn_version=6
FROM nvidia/cuda:${cuda_version}-cudnn${cudnn_version}-devel-ubuntu14.04

# Install extra packages if required
RUN apt-get update -qq && apt-get install --no-install-recommends -y \
    # Essentials
    build-essential \
    g++ \
    git \
    locales \
    rm -rf /var/lib/apt/lists/*

# Add the user that will run the app (no need to run as root)
RUN groupadd -r vano && useradd -r -g vano vano

# Working directory for data and projects
WORKDIR /wrkdir/project
RUN mkdir -p /wrkdir/project
RUN mkdir -p /wrkdir/datasets
RUN mkdir -p /wrkdir/env

# Setup locales
RUN dpkg-reconfigure locales && \
    locale-gen C.UTF-8 && \
    /usr/sbin/update-locale LANG=C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get install -y curl
RUN apt-get install -qq libsndfile1 sndfile-tools
#RUN apt-get install -qq libglib2.0-0
#RUN apt-get -y install libgl1-mesa-glx
RUN apt-get clean

###
# Take appropriate CONDA settings
###
{% if cookiecutter.python_interpreter == 'python' %}
# use python2
COPY conda/ai.py2.yml /wrkdir/env/ai.yml
{% elif cookiecutter.python_interpreter == 'python3' %}
# use python3
COPY conda/ai.py3.yml /wrkdir/env/ai.yml
{% endif %}

# Install conda
RUN conda update -n base conda
RUN conda env create -f /wrkdir/env/ai.yml \
    && rm -rf /opt/conda/pkgs/*

# Install project into container
COPY . /wrkdir/project/
RUN chown -R vano:vano /wrkdir/project/*

# Activate the myapp environment
ENV PATH='/opt/conda/envs/ai/bin:$PATH'
ENV PYTHONPATH='/wrkdir/project:$PYTHONPATH'
