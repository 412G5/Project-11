# cli.py
import click
import requests

API_BASE_URL = "http://10.3.125.248:4000"  # Replace with the actual URL of your API

@click.command()
@click.argument('endpoint', type=click.Choice(['md5', 'factorial', 'fibonacci', 'is-prime', 'slack-alert', 'keyval']))
@click.argument('params', nargs=-1)
def main(endpoint, params):
    """Command line interface for interacting with the REST API."""
    url = f"{API_BASE_URL}/{endpoint}/{'/'.join(params)}"
    response = requests.get(url)

    if response.status_code == 200:
        click.echo(response.json())
    else:
        click.echo(f"Error: {response.status_code}, {response.text}")

if __name__ == '__main__':
    main()
