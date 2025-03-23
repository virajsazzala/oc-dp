# Discord presence with OpenComic

Discord presence integration with OpenComic

> *It isn't production ready, but works!*

## Prerequisites

- Create an application on [discord developers](https://discord.com/developers/applications) portal.
- Name the application as required. (it appears on the "widget")
- Copy the client id from the installation section. (keep it, as it's used in setup)

## Setup

To setup & run, use [Poetry](https://python-poetry.org/) for Python.

```sh
# clone repository
git clone git@github.com:virajsazzala/os-dp.git
cd daisq

# create .env file (put the client id here)
touch .env

# install required deps
poetry install

# activate poetry shell
eval $(poetry env activate)
```

## Usage

To use Presence with OpenComic, use these commands.

```sh
# with poetry activated
python presence.py

# without poetry activated
poetry run python presence.py
```

## Example

Here is an example, of how it'll look..

![presence-example](./examples/dp-example.png)