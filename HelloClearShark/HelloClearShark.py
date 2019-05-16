import subprocess

print("Hello, ClearShark!")

command = "ls"

subprocess.call(command, shell=False)
