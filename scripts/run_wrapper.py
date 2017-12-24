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
    process = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errs = process.communicate()
    if errs:
        return ScriptOutput(False, None, errs.decode("utf-8"))
    return ScriptOutput(True, process, output.decode("utf-8"))


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
