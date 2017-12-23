import subprocess
import shlex


class ScriptOutput:
    def __init__(self, status, process, output=""):
        self.status = status
        self.process = process
        self.output = output


def run_command(commands, **kwargs):
    commands = shlex.split(commands)
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
