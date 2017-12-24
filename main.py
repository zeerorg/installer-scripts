import click
from scripts import mongodb


@click.group()
def cli():
    pass


@cli.group(name="mongodb")
def mongo():
    """
    Admin tasks related to Mongo DB
    """
    click.echo("Working on MongoDB for Ubuntu 16.04")


@mongo.command(name="install")
def mongo_install():
    """
    Install MongoDB
    """
    click.echo("\n")
    mongodb.install()
    click.echo("\n")


@mongo.command(name="test")
def mongo_test():
    """
    Test MongoDB
    """
    mongodb.test()


@mongo.command(name="uninstall")
def mongo_uninstall():
    """
    Uninstall MongoDB
    """
    mongodb.uninstall()
