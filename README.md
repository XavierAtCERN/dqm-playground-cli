# dqm-playground-cli

[![Build Status](https://app.travis-ci.com/XavierAtCERN/dqm-playground-cli.svg?branch=main)](https://app.travis-ci.com/XavierAtCERN/dqm-playground-cli)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The goal of this package is to provide a user interface between the [DQM Playground](https://github.com/CMSTrackerDPG/MLplayground) DB aiming at gathering information from various sources and the data science framework chosen to create models for anomaly detection.

To build the cli:
```bash
git clone https://github.com/XavierAtCERN/dqm-playground-cli

cd dqm-playground-cli
pip3 install --upgrade -r requirements.txt
pip3 install --editable .
```

A naive skeleton of the cli (built using [Click](https://click.palletsprojects.com/en/8.0.x/)) can be found below.

### Runs
```bash
dqm_playground_cli runs --help
Usage: dqm_playground_cli runs [OPTIONS]

  This subcommand provides a list of runs and their variables

Options:
  --run_list BOOLEAN       Provides list of runs.
  --run_number INTEGER     Run number for variable exploration.
  --variable_list BOOLEAN  Provides list of variables.
  --help                   Show this message and exit.
```

Accessing all available runs:
```bash
dqm_playground_cli runs --run_list=True
```

Accessing all variables from a given run (315257):
```bash
dqm_playground_cli runs --variable_list=True --run_number=315257
```

### Lumisections

```bash
dqm_playground_cli lumisections --help
Usage: dqm_playground_cli lumisections [OPTIONS]

  This subcommand provides a list of lumisections associated to a run and
  their variables

Options:
  --run_number INTEGER        Run number for lumisection exploration
  --lumisection_list BOOLEAN  Provides list of lumisection for a given run
  --variable_list BOOLEAN     Provides list of variables for a given
                              lumisection
  --lumi_number INTEGER       Lumisection number for variable exploration
  --help                      Show this message and exit.
```


### Tasks

```bash
dqm_playground_cli tasks --help
Usage: dqm_playground_cli tasks [OPTIONS]

  This subcommand provides a list of the avaiable tasks

Options:
  --help  Show this message and exit.
```

### Going further

To go further with Click, a useful introduction can be found [here](https://www.youtube.com/watch?v=kNke39OZ2k0).
