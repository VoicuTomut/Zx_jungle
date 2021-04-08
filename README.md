# McSimulator
## Experimental code during the QOSF programme

To install and configure a virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
pip install -U -r requirements.txt
```

To use `git` a distributed fashion, after forking the repository 
add an `upstream` reference to the forked repository 
using the instructions from
https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork

For formatting the code
```
python -m black .
```