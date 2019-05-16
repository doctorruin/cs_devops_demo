import subprocess

print("Hello, ClearShark!")

command = ["ls", "-l"]

subprocess.run(command, shell=False)
