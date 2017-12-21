import run_wrapper

def test():
    print("working ...")

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
    print("Installing MongoDB 3.4 in ubuntu 16.04")
    for command in commands.split("\n"):
        script_output = run_wrapper.run_command(commands)
        if not script_output.status:
            print("Failed ...\n Error is: ")
            print(script_output.output)
            return
        else:
            print("Installation complete")
    pass