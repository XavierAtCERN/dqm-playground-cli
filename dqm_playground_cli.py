import click
import requests
import pandas as pd

ENDPOINT_RUNS = ""
ENDPOINT_RUN_CERTIFICATION = ""
ENDPOINT_RUN_HISTOS = "https://ml4dqm-playground.web.cern.ch/runHistos/API/?primary_dataset=JetHT&run__run_number__in="

ENDPOINT_LUMISECTIONS = ""
ENDPOINT_LUMISECTION_CERTIFICATION = ""
ENDPOINT_LUMISECTION_1D_HISTOS = "https://ml4dqm-playground.web.cern.ch/lumisectionHistos1D/API/?title=adc_PXDisk_-1&lumisection__run__run_number__in="
ENDPOINT_LUMISECTION_1D_NO_RUN = "https://ml4dqm-playground.web.cern.ch/lumisectionHistos1D/API/?title=adc_PXDisk_-1"
ENDPOINT_LUMISECTION_2D_HISTOS = ""

ENDPOINT_TASKS = ""
ENDPOINT_SOLUTIONS = ""

TASK_FILE = "task.csv"

# helper functions


def get_runs():
    run_numbers = [0, 1, 2]
    print(run_numbers)
    return


def get_variables(run_number):
    run_endpoint = ENDPOINT_RUN_HISTOS + f"{run_number}"
    response = requests.get(run_endpoint)
    click.echo(f"response status code: {response.status_code}")
    df = pd.read_json(response.text)
    click.echo(df["title"].tolist())
    return


def get_lumisections_1D_histos(run_number):
    lumisection_1D_endpoint = ENDPOINT_LUMISECTION_1D_HISTOS + f"{run_number}"
    response = requests.get(lumisection_1D_endpoint)
    click.echo(f"response status code: {response.status_code}")
    df = pd.read_json(response.text)
    # click.echo(df.head())
    columns = df.columns.tolist()
    if "run" in columns:
        click.echo("Valid run number")
        click.echo(df[["run", "lumisection"]])
        click.echo(f"Extracted {df.shape[0]} lumisections from DB")
    else:
        click.echo("Run not found in the DB")
    return


def create_dummy_task(run_number):
    lumisection_1D_endpoint = ENDPOINT_LUMISECTION_1D_HISTOS + f"{run_number}"
    response = requests.get(lumisection_1D_endpoint)
    click.echo(f"response status code: {response.status_code}")
    df = pd.read_json(response.text)
    click.echo(df[["run", "lumisection"]].head())
    df[["run", "lumisection"]].sample(n=10).to_csv("task.csv", index=False)
    return


def get_dummy_task(task_file):
    df = pd.read_csv(task_file)
    click.echo(df.head())
    return df


def get_variables_for_task(task):
    click.echo("Acquiring variable for task")
    lumisection_1D_endpoint = ENDPOINT_LUMISECTION_1D_NO_RUN
    response = requests.get(lumisection_1D_endpoint)
    df = pd.read_json(response.text)

    click.echo("Task definition")
    click.echo(task.head())
    click.echo("Inputs")
    click.echo(df.head())

    # select relevant run + lumi through merge
    # this should be moved to the backend side later
    variables = task.merge(df, on=['run', 'lumisection']) 
    click.echo("Merged to select run+lumisections")
    click.echo(variables.head())
    df[["run", "lumisection", "title", "data"]].to_csv("inputs_to_data_science.csv", index=False)
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
    if lumisection_list == True:
        get_lumisections_1D_histos(run_number)
    elif variable_list == True:
        click.echo("Need new endpoint formatting")


# tasks
@cli.command()
@click.option("--run_number", default=0, help="Run number for lumisection exploration")
@click.option(
    "--dummy_task",
    default=False,
    help="Create dummy task by sampling 10 lumisections from run_number",
)
@click.option(
    "--variables_for_task",
    default=False,
    help="Create file with variables needed for (dummy) task",
)
@pass_config
def tasks(config, run_number, dummy_task, variables_for_task):
    """This subcommand provides a list of the avaiable tasks"""
    click.echo("Tasks report ---")
    if dummy_task == True:
        create_dummy_task(run_number)
    elif variables_for_task == True:
        task = get_dummy_task(TASK_FILE)
        get_variables_for_task(task)

# predictions
