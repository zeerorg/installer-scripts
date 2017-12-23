import subprocess
import shlex


class ScriptOutput:
    def __init__(self, status, process, output=""):
        self.status = status
        self.process = process
        self.output = output


def run_command(command, **kwargs):
    print('Command: {}'.format(command))
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
    :param command:
    :return: list
    """
    ans = []
    for command in [x.strip() for x in command.split("\n")]:
        if command:
            ans.append(shlex.split(command))
    return ans
