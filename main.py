import click
from scripts import mongodb


@click.group()
def cli():
    pass


@cli.command(name="mongodb")
@click.argument("task", default="test")
def task_mongo(task):
    """
    Admin tasks related to Mongo DB
    """
    click.echo("Working on MongoDB for Ubuntu 16.04")
    if task == "install":
        mongodb.install()
    elif task == "test":
        mongodb.test()
    elif task == "uninstall":
        mongodb.uninstall()
