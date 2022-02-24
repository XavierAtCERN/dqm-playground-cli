import click
import requests
import pandas as pd

ENDPOINT_RUNS = ''
ENDPOINT_RUN_CERTIFICATION = ''
ENDPOINT_RUN_HISTOS = 'https://ml4dqm-playground.web.cern.ch/runHistos/API/?primary_dataset=JetHT&run__run_number__in='

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

def get_variables(run_number):
    run_endpoint = ENDPOINT_RUN_HISTOS+f'{run_number}'
    response = requests.get(run_endpoint)
    print(f'response status code: {response.status_code}')
    df = pd.read_json(response.text)
    print(df['title'].tolist())
    return

@click.command()
@click.option('--run_list', default=False, help='Provides list of runs.')
@click.option('--variable_list', default=False, help='Provides list of variables.')
@click.option('--run_number', default=0, help='Run number for variable exploration.')
def cli(run_list, variable_list, run_number):
    """Simple program that provides list of runs / list of variables"""
    if run_list == True:
        print('List of runs available')
        get_runs()
    elif variable_list == True:
        print('List of variables available')
        get_variables(run_number)
    else:
        print('')
