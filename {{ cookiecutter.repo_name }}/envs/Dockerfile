# Environment: Conda, Python 2.7, Tensorflow, Keras
FROM continuumio/miniconda3:latest

# Install extra packages if required
RUN apt-get update && apt-get install -y \
    xxxxxx \
    && rm -rf /var/lib/apt/lists/*

# Add the user that will run the app (no need to run as root)
RUN groupadd -r myuser && useradd -r -g myuser myuser

WORKDIR /app

# Grab appropriate conda settings
{% if cookiecutter.python_interpreter == 'python' %}
COPY conda/ai.py2.yml /app/ai.yml
{% elif cookiecutter.python_interpreter == 'python3' %}
COPY conda/ai.py3.yml /app/ai.yml
{% endif %}

RUN conda config --add channels conda-forge \
    && conda env create -n myapp -f environment.yml \
    && rm -rf /opt/conda/pkgs/*

# Install myapp
COPY . /app/
RUN chown -R myuser:myuser /app/*

# activate the myapp environment
ENV PATH /opt/conda/envs/myapp/bin:$PATH
