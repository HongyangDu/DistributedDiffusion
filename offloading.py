# Import necessary modules
from diffusers import StableDiffusionPipeline  # Pipeline for Diffusion Models
import torch  # PyTorch for tensor computations
import numpy as np  # Numpy for numerical operations
import random  # Python built-in random module
from PIL import Image  # Python Imaging Library for image operations

# Function to set seed for all random operations, ensuring reproducibility
def seed_everywhere(seed):
    torch.manual_seed(seed)  # Sets the seed for generating random numbers for PyTorch
    torch.cuda.manual_seed(seed)  # Sets the seed for generating random numbers for CUDA
    torch.cuda.manual_seed_all(seed)  # Sets the seed for generating random numbers on all GPUs
    np.random.seed(seed)  # Sets the seed for generating random numbers for Numpy
    random.seed(seed)  # Sets the seed for generating random numbers for Python's built-in random module

# Define model_id for the pretrained model from Hugging Face
model_id = "CompVis/stable-diffusion-v1-4"

# Instantiate pipeline with the pretrained model
# For Mac (recommended)
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32).to("cpu")
# For Windows (recommended)
# pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")

# Define parameters for image generation
seed = 41  # Seed for random operations
seed_everywhere(seed)  # Apply the seed
step = 15  # Inference steps for the pipeline
off_step = 4  # Offloading processing point
scale = 7.5  # Guidance scale for the pipeline
savepath = "seed"+str(seed)+"step"+str(step)  # Save path for the generated images

# Generate the first image with the prompt "One Apple on Table"
prompt = "One Apple on Table"
image = pipe(prompt, num_inference_steps=step, tt=off_step, ss=True, guidance_scale=scale).images[0]
image.save(savepath + prompt + "_final.png")  # Save the generated image

# Generate the second image with the prompt "One Lemon on Table"
seed_everywhere(seed)  # Apply the seed again to ensure reproducibility
prompt = "One Lemon on Table"
image = pipe(prompt, num_inference_steps=step, tt=off_step, ss=False, guidance_scale=scale).images[0]
image.save(savepath + prompt + str(off_step) + "_final.png")  # Save the generated image
