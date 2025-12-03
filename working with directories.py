from pathlib import Path
path = Path("emails")
print(path.mkdir())

from pathlib import Path
path = Path("emails")
print(path.rmdir())

from pathlib import Path
path = Path()
for file in path.glob('*.py'):
    print(file)

from pathlib import Path
path = Path()
for file in path.glob('*'):
    print(file)
