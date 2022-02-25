import click
import requests
import pandas as pd

ENDPOINT_RUNS = ""
ENDPOINT_RUN_CERTIFICATION = ""
ENDPOINT_RUN_HISTOS = "https://ml4dqm-playground.web.cern.ch/runHistos/API/?primary_dataset=JetHT&run__run_number__in="

ENDPOINT_LUMISECTIONS = ""
ENDPOINT_LUMISECTION_CERTIFICATION = ""
ENDPOINT_LUMISECTION_1D_HISTOS = ""
ENDPOINT_LUMISECTION_2D_HISTOS = ""

ENDPOINT_TASKS = ""
ENDPOINT_SOLUTIONS = ""

# helper functions


def get_runs():
    run_numbers = [0, 1, 2]
    print(run_numbers)
    return


def get_variables(run_number):
    run_endpoint = ENDPOINT_RUN_HISTOS + f"{run_number}"
    response = requests.get(run_endpoint)
    print(f"response status code: {response.status_code}")
    df = pd.read_json(response.text)
    print(df["title"].tolist())
    return


# click context


class Config(object):
    def __init__(self):
        self.verbose = False


pass_config = click.make_pass_decorator(Config, ensure=True)

# cli
@click.group()
@click.option("--verbose", is_flag=True)
@pass_config
def cli(config, verbose):
    config.verbose = verbose
    if verbose:
        click.echo("We are in verbose mode")


# runs
@cli.command()
@click.option("--run_list", default=False, help="Provides list of runs.")
@click.option("--run_number", default=0, help="Run number for variable exploration.")
@click.option("--variable_list", default=False, help="Provides list of variables.")
@pass_config
def runs(config, run_list, run_number, variable_list):
    """This subcommand provides a list of runs and their variables"""
    if config.verbose:
        click.echo("We are in verbose mode")
    if run_list == True:
        click.echo("List of runs available")
        get_runs()
    elif variable_list == True:
        click.echo("List of variables available")
        get_variables(run_number)
    else:
        click.echo("")


# lumisections
@cli.command()
@click.option("--run_number", default=0, help="Run number for lumisection exploration")
@click.option(
    "--lumisection_list",
    default=False,
    help="Provides list of lumisection for a given run",
)
@click.option(
    "--variable_list",
    default=False,
    help="Provides list of variables for a given lumisection",
)
@click.option(
    "--lumi_number", default=0, help="Lumisection number for variable exploration"
)
@pass_config
def lumisections(config, run_number, lumisection_list, variable_list, lumi_number):
    """This subcommand provides a list of lumisections associated to a run and their variables"""
    click.echo("Lumisection report ---")


# tasks
@cli.command()
@pass_config
def tasks(config):
    """This subcommand provides a list of the avaiable tasks"""
    click.echo("Tasks report ---")


# predictions
