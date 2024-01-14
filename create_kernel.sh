#!/bin/bash

poetry run pip install ipykernel
poetry run python -m ipykernel install --user --name=spotification
