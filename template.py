import os
from pathlib import Path

package_name = "Insurance_Premium_Prediction"

list_of_files = [
    "github/workflows/.gitkeep",
    f"{package_name}/__init__.py",
    f"{package_name}/components/__init__.py",
    f"{package_name}/components/data_ingestion.py",
    f"{package_name}/components/data_transformation.py",
    f"{package_name}/components/model_trainer.py",
    f"{package_name}/pipelines/__init__.py",
    f"{package_name}/pipelines/training_pipeline.py",
    f"{package_name}/pipelines/prediction_pipeline.py",
    f"{package_name}/logger.py",
    f"{package_name}/exception.py",
    f"{package_name}/utils/__init__.py",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "setup.py",
    "init_setup.sh",
]

# Creating directories if they don't exist
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # If directory doesn't exist, create it
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # Creating empty file if it doesn't exist or empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print("File already exists")
