# dqm-playground-cli

[![Build Status](https://app.travis-ci.com/XavierAtCERN/dqm-playground-cli.svg?branch=main)](https://app.travis-ci.com/XavierAtCERN/dqm-playground-cli)

The goal of this package is to provide a user interface between the [DQM Playground](https://github.com/CMSTrackerDPG/MLplayground) DB aiming at gathering information from various sources and the data science framework chosen to create models for anomaly detection.

To build the cli:
```
git clone https://github.com/XavierAtCERN/dqm-playground-cli

cd dqm-playground-cli
pip3 install --upgrade -r requirements.txt
pip3 install --editable .
```

A naive skeleton of the cli (built using [Click](https://click.palletsprojects.com/en/8.0.x/)) is the following:
```
dqm_playground_cli --help
Usage: dqm_playground_cli [OPTIONS]

  Simple program that provides list of runs / list of variables

Options:
  --run_list BOOLEAN       Provides list of runs.
  --variable_list BOOLEAN  Provides list of variables.
  --run_number INTEGER     Run number for variable exploration.
  --subsystem TEXT         Subsystem for variable exploration.
  --workspace TEXT         Workspace for variable exploration.
  --help                   Show this message and exit.
```

Accessing all available runs:
```
dqm_playground_cli --run_list=True
```

Accessing all variables from a given run (315257):
```
dqm_playground_cli --variable_list=True --run_number=315257
```
