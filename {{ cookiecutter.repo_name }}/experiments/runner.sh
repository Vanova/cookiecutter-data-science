#!/bin/bash

export PYTHONPATH="`pwd`/:$PYTHONPATH"
{% if cookiecutter.python_interpreter == 'python' %}
# use python2
source activate ai # activate conda environment
{% elif cookiecutter.python_interpreter == 'python3' %}
# use python3
source activate ai3
{% endif %}

model=sed_ogits
log_dir=logs/$(date "+%d_%b_%Y")
log_file=$log_dir/${model}_$(date "+%H_%M_%S").log
mkdir -p $log_dir

echo "Log to: $log_file"
python -u experiment.py -m dev -p ./params/experiment.yaml --verbose > ${log_file}
