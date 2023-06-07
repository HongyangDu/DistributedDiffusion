# DistributedDiffusion

This repository holds a partial implementation of the system design and algorithm detailed in the paper: 

**"Exploring Collaborative Distributed Diffusion-Based AI-Generated Content (AIGC) in Wireless Networks"**

## Getting Started

The instructions below guide you through the steps needed to get the project up and running on your local machine.

### Step 1: Environment Setup

Firstly, create a new conda environment by running the following command:

conda create --name disdiff python==3.9

### Step 2: Activate Environment

Next, activate the created environment with:

conda activate disdiff

### Step 3: Install Required Packages

Install the necessary packages using pip:

pip install diffusers==0.13.1
pip install torch
pip install transformers
pip install accelerate

### Step 4: Locate StableDiffusionPipeline

Open `offloading.py` in your code editor. Hold `ctrl` key and click on `StableDiffusionPipeline` if you are on Windows or `command` key if you are on Mac.

![Location of StableDiffusionPipeline](img1.png)

This will navigate to the file `pipeline_stable_diffusion.py`. To locate this file in your directory, right-click on the filename and choose 'open in' -> 'finder'.

### Step 5: Replace with Project File

Replace `pipeline_stable_diffusion.py` with the file of the same name from this repository.

### Step 6: Run the Program

Finally, run `offloading.py` to start the program.

## Cite Our Work

If our code proves useful in your research, please consider citing our work:

@article{du2023exploring,
  title={Exploring Collaborative Distributed Diffusion-Based AI-Generated Content (AIGC) in Wireless Networks},
  author={Du, Hongyang and Zhang, Ruichen and Niyato, Dusit and Kang, Jiawen and Xiong, Zehui and Kim, Dong In and Poor, H Vincent and others},
  journal={arXiv preprint arXiv:2304.03446},
  year={2023}
}

Thank you for your interest in our project!
