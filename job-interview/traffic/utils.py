import subprocess


def run_command(command: str) -> str:
    """execute shell commands and capture output"""
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode().strip()
    except subprocess.CalledProcessError as e:
        return e.output.decode().strip()
