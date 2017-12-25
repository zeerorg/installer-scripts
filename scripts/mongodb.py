import click
import pymongo

from scripts import run_wrapper
from pymongo.errors import ServerSelectionTimeoutError


def test(username=None, password=None):
    """
    Test a client connection to local MongoDB install

    :param username: (str)
    :param password: (str)
    :return: (bool)
    """
    client = pymongo.MongoClient(username=username, password=password, serverSelectionTimeoutMS=200)
    try:
        client.server_info()
    except ServerSelectionTimeoutError as err:
        return False
    return True


def install():
    """
    Installs MongoDB in ubuntu 16.04
    """
    commands = """
        sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
        echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
        sudo apt-get update
        sudo apt-get install mongodb-org -y
        sudo systemctl start mongod
        sudo systemctl enable mongod
    """
    click.echo("Installing MongoDB 3.4 in ubuntu 16.04")
    for command in run_wrapper.get_commands_split(commands):
        script_output = run_wrapper.run_command(command)

    click.echo("Installation complete")


def uninstall():
    """
    Uninstall MongoDb ubuntu 16.04
    """
    commands = """
        sudo apt-get remove mongodb* --purge -y
        sudo rm /etc/apt/sources.list.d/mongodb-org-3.6.list
    """
    for command in run_wrapper.get_commands_split(commands):
        script_output = run_wrapper.run_command(command)

    click.echo("Uninstalled MongoDB")
