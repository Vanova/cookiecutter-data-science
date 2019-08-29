"""
    {{cookiecutter.project_name}}
    =====================================
    {{cookiecutter.description}}

    --------------------------------------------------------------------
        Affiliation: {{cookiecutter.affiliation}}
        Author:  {{cookiecutter.author_name}}

    Usage:
        experiment.py [-p FILE] [-m (dev|sub)] [--overwrite] [--quiet | --verbose]
        experiment.py -m dev -p file.yaml --verbose
        experiment.py -m sub -p file.yaml
        experiment.py (-s | --show_params)
        experiment.py (-h | --help)
        experiment.py (-v | --version)

    Options:
        -h --help               Show this screen.
        -v --version            Show version.
        -s --show_params        Show available configuration files  [default: False].
        -m --mode               System mode: development (dev) / submission or evaluation (sub) [default: dev].
        -p FILE, --params FILE  Model configuration file            [default: params/experiment.yaml].
        --overwrite             Force to overwrite model data       [default: False].
        --quite                 Output less log information         [default: False].
        --verbose               Output detailed log information     [default: False].
"""
from __future__ import print_function, absolute_import
import os
import sys
from docopt import docopt
sys.path.append(os.path.split(os.path.dirname(os.path.realpath(__file__)))[0])
__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)


def main(args):
    """
    Pipelines logic is here
    """
    pass


if __name__ == '__main__':
    arguments = docopt(__doc__, version=__version__)
    main(arguments)
