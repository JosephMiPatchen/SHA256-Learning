#!/bin/bash

# Step 1: Create a virtual environment
python3 -m venv lorenz_env

# Step 2: Activate the virtual environment
source lorenz_env/bin/activate

# Step 3: Install required Python packages
pip install --upgrade pip
pip install matplotlib numpy

# Step 4: Run the Python script from ./lorenz_attractor/sim.py
python ./lorenz_attractor/sim.py

# Step 5: Deactivate the virtual environment
deactivate
