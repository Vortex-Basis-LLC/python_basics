# python_basics

## Setup
- Install Miniconda
  - Verify that you can create and use environments with conda command.

- Open terminal and go to root folder of the project (with environment.yml).

- Create the conda environment:
```
conda env create -f environment.yml
```

- If you later need to update the environment (where --prune removes whatever was
removed from environment.yml):
```
conda env update -f environment.yml --prune
```

- NOTE: You can later remove this environment with:
```
conda remove -n vbg_basics --all
```

- Activate the conda environment:
```
conda activate vbg_basics
```

- Open Jupyter Lab to explore the examples:
```
jupyter lab
```

## Environment Settings

Some samples will required environment settings in a ".env" file in the root directory of this project
will be loaded via load_dotenv(override=True) and os.getenv("KEYNAME").

Here are some examples of some you might need to set:
```
HUGGINGFACE_TOKEN=...
```