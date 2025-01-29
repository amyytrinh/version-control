from datetime import datetime
now = datetime.now()

version_file = "version.md"
with open(version_file, 'w') as file:
    file.write(f"{now}\n")