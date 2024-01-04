# DistributedDiffusion

This repository contains a demo implementation of the algorithm as presented in:

> **"User-Centric Interactive AI for Distributed Diffusion Model-based AI-Generated Content" [Download Paper](journal_paper.pdf)**

and

> **"Exploring Collaborative Distributed Diffusion-Based AI-Generated Content (AIGC) in Wireless Networks" [Download Paper](mag_paper.pdf)**

![System Model](readme/img0.png)

---

## 📝 Table of Contents
- [Environment Setup](#-environment-setup)
- [Activate Environment](#-activate-environment)
- [Install Required Packages](#-install-required-packages)
- [Locate StableDiffusionPipeline](#-locate-stablediffusionpipeline)
- [Replace with Project File](#-replace-with-project-file)
- [Run the Program](#-run-the-program)
- [Cite Our Work](#-cite-our-work)

---

## 🔧 Environment Setup
To create a new conda environment, run the following command:

```bash
conda create --name disdiff python==3.9
```
## ⚡Activate Environment
Activate the created environment with:
```bash
conda activate disdiff
```

## 📦 Install Required Packages
You need to install the following packages using pip:
```bash
pip install diffusers==0.13.1
pip install torch
pip install transformers
pip install accelerate
```

## 🔍 Locate StableDiffusionPipeline
Open `offloading.py` in your code editor. Hold `ctrl` key if you are on Windows or `command` key if you are on Mac, and click on `StableDiffusionPipeline`

![Location of StableDiffusionPipeline](readme/img1.png)

This will navigate to the file `pipeline_stable_diffusion.py`. To locate this file in your directory, right-click on the filename and choose 'open in' -> 'finder'.

![Location of StableDiffusionPipeline](readme/img2.png)

## 🔄 Replace with Project File
Replace `pipeline_stable_diffusion.py` with the file of the same name from this repository.

![Replace `pipeline_stable_diffusion.py`](readme/img3.png)

## 🏃‍♀️ Run the Program
Finally, run `offloading.py` to start the program.

 Please note that the model will be downloaded automatically if you are running this code for the first time.
 
![Download Automatically](readme/img4.png)

## 🔍 Check the results

The parameter "tt" is the offloading processing point

The parameter "ss" is the total denosing steps

For more details, please check the `offloading.py`

![Results](readme/img5.png)
 
---

## 📚 Cite Our Work

If our code proves useful in your research, please consider citing our work:

```bibtex
@article{du2023user,
  title={User-Centric Interactive AI for Distributed Diffusion Model-based AI-Generated Content},
  author={Du, Hongyang and Zhang, Ruichen and Niyato, Dusit and Kang, Jiawen and Xiong, Zehui and Cui, Shuguang and Shen, Xuemin and Kim, Dong In},
  journal={arXiv preprint arXiv:2311.11094},
  year={2023}
}
```


```bibtex
@article{du2023exploring,
  title={Exploring Collaborative Distributed Diffusion-Based AI-Generated Content (AIGC) in Wireless Networks},
  author={Du, Hongyang and Zhang, Ruichen and Niyato, Dusit and Kang, Jiawen and Xiong, Zehui and Kim, Dong In and Poor, H Vincent},
  journal={arXiv preprint arXiv:2304.03446},
  year={2023}
}
```
