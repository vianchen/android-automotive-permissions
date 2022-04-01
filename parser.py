import json
import os

cwd = os.path.dirname(__file__)

with open(os.path.join(cwd, 'Manifest.json'), 'r') as infile:
  data = json.load(infile)
  with open(os.path.join(cwd, 'Permissions'), 'w') as outfile:
    for perm in data['manifest']['permission']:
      outfile.write(perm['@android:name'] + '\n')
