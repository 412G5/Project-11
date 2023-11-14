# cli.py
import click
import requests

API_BASE_URL = "http://localhost:8000" 

@click.command()
@click.argument('endpoint', type=click.Choice(['md5', 'factorial', 'fibonacci', 'is-prime', 'slack-alert', 'keyval']))
@click.argument('params', nargs=-1)
def main(endpoint, params):
    """CLI for controlling the API."""
    url = f"{API_BASE_URL}/{endpoint}/{'/'.join(params)}"
    response = requests.get(url)

    if response.status_code == 200:
        click.echo(response.json())
    else:
        click.echo(f"Error: {response.status_code}, {response.text}")

if __name__ == '__main__':
    main()
