echo [$(date)]: "START"

echo [$(date)]: "Creating environment with Python 3.9 version"

conda create --prefix ./env python=3.9 -y

echo [$(date)]: "Activating the environment"

source activate ./env

echo [$(date)]: "Installing the development requirements"

pip install -r requirements.txt

echo [$(date)]: "END"
