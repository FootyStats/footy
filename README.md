# Football Statistics

Jupyter notebooks for and modules for the statistical analysis of football
(soccer) data.

To start, see the
[background Jupyter notebook](background.ipynb).

Documentation for the `footy` module is available at
[docs/index.md](docs/index.md)

## Requirements

We *strongly* recommend looking at
[pyenv](https://github.com/pyenv/pyenv) and
[pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) so that you can
install virtual Python environments without permanently filling up your laptop
with crap.

On MacOS, these can be installed using:

```
brew install pyenv pyenv-virtualenv xz
```

The `xz` package is required to avoid the following message when using the
[pandas](https://pandas.pydata.org/) package:

```
UserWarning: Could not import the lzma module. Your installed Python is
incomplete. Attempting to use lzma compression will result in a RuntimeError. 
```

Then follow the links above to ensure that your virtual environment is setup
correctly.  At the moment, development is been carried out with Python 3.8.2.

Once that has been setup, install the Python packages required with:

```
pip install -r requirements.txt
```
