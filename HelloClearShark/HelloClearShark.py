import subprocess

print("Hello, ClearShark!")

command = "ls"

if command == "ls":
    subprocess.run(command, shell=False)
