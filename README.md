# EE4147 Group Project
Topic:  San Francisco Crime Classification
---

## Getting Started

### Project Structure

```bash
.
├── data --- "the location of the dataset"
├── libs  --- "the location of the helper functions"
├── notebooks  --- "the location of the notebooks, consists of all the driver code"
├── results --- "the location of the experimental results. i.e. the plots" 
├── README.md
└── ref  --- "any references for report writing"
```

### Dependencies Installation
In this project, Conda is used for virual environment management, all the dependencies are stated in requirements.txt.

Please feel free to add any libraries your need, but you need to remember to use `pip freeeze > requirements.txt` to update the dependencies list before push to the remote and also notify the groupmates.

#### Create a virtual environment and install the dependencies
```
conda create --name <your-environment-name> python=3.8
conda activiate <your-environment-name>
pip install -r requirements.txt
```



### Development Guide

* Python is the main development language
* Try not to write the long functions directly in notebooks, write it in a separate Python script and import it in the notebook is better (Easy to debug)

### References
https://www.kaggle.com/c/sf-crime/overview