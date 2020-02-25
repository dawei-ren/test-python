"""
click模块提供更加方便的创建命令

使用方法
python test_click.py --help
python test_click.py --count 3
"""
import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)


@click.group()
def cli():
    """
    定义一组命令
    """
    pass


@cli.command()
def initdb():
    click.echo('Initialized the database')


@cli.command()
def dropdb():
    click.echo('Dropped the database')


if __name__ == '__main__':
    hello()
    # cli()
