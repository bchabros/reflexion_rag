# Reflexion Agent

## Introduction

Simple ReactAgent where in first step it looking something in internet using TAVILY and then model critique answer and add their suggestions.

### General information

- This project uses conda as an environment manager. The user must have Anaconda or Miniconda installed.
- This project uses git-hooks to check code quality when creating commits.

### Repository

- https://github.com/bchabros/reflexion_rag.git

### Local env setup

#### 1. Conda

- Install conda (miniconda version): https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
- Install conda (anaconda navigator version): https://anaconda.org/anaconda/conda
- Make sure conda directory (`C:\Users\<USER>\AppData\Local\miniconda3`) or (`C:\Users\<USER>\AppData\Local\conda`) is added to PATH environment variable in Windows
- Create conda environment from `env.yaml`: `conda env create -f env.yaml`
- Activate environment: `conda activate reflexion_agent`

#### 2. .env file

- Create `.env` file in the project's root directory (based on .env-sample file). The content of `.env` is not stored in Git repository, because it contains secrets.

#### 3. PyCharm settings

- Edit Run/Debug configurations in PyCharm and make sure to select the correct `.env` file and conda environment
- In PyCharm choose `File -> Settings -> Python interpreter` and select `reflexion_agent` environment

#### 4. Main File:

[main.py](main.py) - It's based on basic streamlit library so to run app you have to run command `streamlit run main.py`

#### 5. Reflexion Agent Algorithm

Pipeline is Reflexion Agent where in first step we send it prompt then he is looking for info using Tavily and after that it's checking his answer few times to get better results.

![graph.png](png/graph_readme.png)

#### 6. LangGraph Studio
In repo is [langgraph.json](langgraph.json) which is compatible with LangGraph Studio: https://blog.langchain.dev/langgraph-studio-the-first-agent-ide/


