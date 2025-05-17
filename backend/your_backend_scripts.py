import os
import shutil

# Path to the generated file
generated_file = os.path.abspath('path/to/generated_file.ext')

# Destination path in the public directory
destination = os.path.join('public', 'output', 'generated_file.ext')

# Ensure the destination directory exists
os.makedirs(os.path.dirname(destination), exist_ok=True)

# Move the file
shutil.move(generated_file, destination)
