# cli.py by Lauren and Harley
import click
import requests

API_BASE_URL = "http://34.174.168.30/"

def call_api(endpoint, params):
    url = f"{API_BASE_URL}/{endpoint}/{params}"
    response = requests.get(url)

    if response.status_code == 200:
        click.echo(response.json())
    else:
        click.echo(f"Error: {response.status_code}, {response.text}")

@click.command()
def main():
    click.echo("Welcome to our API CLI.")

    while True:
        menu = """
        Menu:
        1. MD5 Hash
        2. Factorial
        3. Fibonacci
        4. Is Prime
        5. Slack Alert
        6. Quit
        """
        click.echo(menu)

        choice = click.prompt("Choose a function (1-5). If you would like to exit, enter 6", type=int, default=1, show_default=True)

        if choice == 6:
            click.echo("Exiting the API CLI.")
            break

        if choice == 1:
            endpoint = 'md5'
            params = click.prompt("Enter a string for MD5 hash", type=str)
        elif choice == 2:
            endpoint = 'factorial'
            params = click.prompt("Enter a positive integer for factorial", type=int)
        elif choice == 3:
            endpoint = 'fibonacci'
            params = click.prompt("Enter a positive integer for Fibonacci", type=int)
        elif choice == 4:
            endpoint = 'is-prime'
            params = click.prompt("Enter an integer for primality check", type=int)
        elif choice == 5:
            endpoint = 'slack-alert'
            params = click.prompt("Enter a string for Slack Alert", type=str)
        else:
            click.echo("Invalid choice. Please enter a number from 1 to 6.")
            continue

        call_api(endpoint, params)

if __name__ == '__main__':
    main()
