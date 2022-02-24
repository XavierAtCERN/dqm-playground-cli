import click
import requests
import pandas as pd

ENDPOINT_RUNS = ''
ENDPOINT_RUN_CERTIFICATION = ''
ENDPOINT_RUN_HISTOS = ''

ENDPOINT_LUMISECTIONS = ''
ENDPOINT_LUMISECTION_CERTIFICATION = ''
ENDPOINT_LUMISECTION_1D_HISTOS = ''
ENDPOINT_LUMISECTION_2D_HISTOS = ''

ENDPOINT_TASKS = ''
ENDPOINT_SOLUTIONS = ''

def get_runs():
    run_numbers = [0, 1, 2]
    print(run_numbers)
    return

def get_variables():
    variables = ['mean', 'rms', 'kurtosis']
    print(variables
    return

@click.command()
@click.option('--run_list', default=False, help='Provides list of runs.')
@click.option('--variable_list', default=False, help='Provides list of variables.')
def cli(run_list, variable_list):
    """Simple program that provides list of runs / list of variables"""
    if run_list == True:
        print('List of runs available')
        get_runs()
    elif variable_list == True:
        print('List of variables available')
        get_variables()
    else:
        return
