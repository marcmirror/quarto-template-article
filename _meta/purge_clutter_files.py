
import os
import glob

# Type of files that should be deleted after rendering
extensions = [
    '*.html',
    '*.lop'
]

# Iterate recursively through every directory and find files that match any
# of the extensions
files = [f for ext in extensions for f in glob.glob(
    os.path.join('.', '**', ext),
    recursive=True
)]

# Delete the files
for file in files:
    os.remove(file)
