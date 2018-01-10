from scripts import run_wrapper
import click


def test():
    click.echo("Testing mongodb module")


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
        if not script_output.status:
            click.echo("Failed ...\n Error is: ")
            click.echo(script_output.output)
            if input("Continue (Y/n): ").lower() == 'n':
                return

    click.echo("Installation complete")


def uninstall():
    """
    Uninstall MongoDb ubuntu 16.04
    """
    commands = """
        sudo systemctl stop mongod
        sudo systemctl disable mongod
        sudo apt-get remove mongodb* --purge -y
        sudo rm /etc/apt/sources.list.d/mongodb-org-3.6.list
        sudo apt-key del 0C49F3730359A14518585931BC711F9BA15703C6
    """
    for command in run_wrapper.get_commands_split(commands):
        script_output = run_wrapper.run_command(command)
        if not script_output.status:
            click.echo("Failed ...\n Error is: ")
            click.echo(script_output.output)
            if input("Continue (Y/n): ").lower() == 'n':
                return

    click.echo("Uninstalled MongoDB")
