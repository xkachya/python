# Example Python snippet to remove trailing whitespace from the specified files
files_to_fix = ["../meshtastic/mesh_interface.py", "../meshtastic/node.py"]

for file_path in files_to_fix:
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        fixed_lines = [line.rstrip() + '\n' for line in lines]
        file.seek(0)
        file.writelines(fixed_lines)
        file.truncate()