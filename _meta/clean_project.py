import os
from os import listdir

# Remove clutter
for file_name in listdir('.'):
    if file_name.endswith(('.html', '.lop')):
        os.remove(file_name)
