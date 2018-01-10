# Qstaller (Quick Installer)

Project aimed at providing scripts for installing development packages easily.

### Usage: 
Install:
```bash
git clone https://github.com/zeerorg/installer-scripts.git
cd installer-scripts
sudo pip install -e .
```

Launch:

`qstaller`

### Starter Packages:
1. mongodb - install and uninstall
2. postgresql - install and uninstall
3. mysql - install and uninstall
4. parse-server - install and uninstall

### Some points:
1. Tests go in `tests/`
2. Suggestions wanted: Use docker for tests or use [docker-test-runner](https://github.com/zeerorg/docker-test-runner.git)