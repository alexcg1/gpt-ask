import readline
import subprocess

import click
from rich import print
from rich.prompt import Prompt


def get_response(query):
    response = subprocess.run(
        ['gpto', '-p', f'{query}?'],
        stdout=subprocess.PIPE,
        universal_newlines=True,
    ).stdout.strip()
    output = f'[bold red]GPT3[/bold red]: {str(response)}'

    return output


@click.command()
@click.option('--model', default='text-davinci-003')
@click.option('--temperature', default=0.9)
@click.argument('query', nargs=-1)
def main(query: str, model: str, temperature: float):
    if len(query) == 0:
        while True:
            query = Prompt.ask('[bold green]User[/bold green]')
            print(get_response(query))

    else:
        query = ' '.join(query)
        print(get_response(query))


if __name__ == '__main__':
    main()
