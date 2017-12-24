import subprocess
import shlex
import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


class ScriptOutput:
    def __init__(self, status, process, output=""):
        self.status = status
        self.process = process
        self.output = output


def run_command(command):
    """
    Runs a single line command

    :param command: (string)
    :return: (ScriptOutput)
    """
    logging.info('Command: {}'.format(command))
    commands = shlex.split(command)
    file = open("test_file", "w")
    try:
        process = subprocess.run(commands, stdout=file)
        file.close()
        file = open("test_file")
        output = file.read()
        file.close()
        return ScriptOutput(True, process, output)
    except Exception as e:
        print(e)
        file.close()
        file = open("test_file")
        error = file.read()
        file.close()
        return ScriptOutput(False, None, error)
    pass


def get_commands_split(command):
    """
    Splits multi line commands to list of commands

    :param command: (string)
    :return: (list)
    """
    ans = []
    for command in [x.strip() for x in command.split("\n")]:
        if command:
            ans.append(command)
    return ans
