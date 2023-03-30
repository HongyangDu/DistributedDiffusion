from diffusers import StableDiffusionPipeline
import torch
import numpy as np
import random
from PIL import Image
# import cv2
# 1
def seed_everywhere(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
# Previous model from hug face
model_id = "CompVis/stable-diffusion-v1-4"
# pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cpu")
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cpu")
# ====================================================

# seed = np.random.randint(100)
# print(seed)

seed = 41
seed_everywhere(seed)
step = 15
off_step = 4
scale = 7.5
savepath = "Offload/seed"+str(seed)+"step"+str(step)
# ss: use the offloading or not
# tt: the offloading processing point
seed_everywhere(seed)
prompt = "One Apple on Table"
image = pipe(prompt, num_inference_steps=step, tt=off_step, ss=True, guidance_scale=scale).images[0]
image.save(savepath + prompt + "_final.png")

seed_everywhere(seed)
prompt = "One Lemon on Table"
image = pipe(prompt, num_inference_steps=step, tt=off_step, ss=False, guidance_scale=scale).images[0]
image.save(savepath + prompt + str(off_step) + "_final.png")

# while off_step < step:
#     seed_everywhere(seed)
#     prompt = "Photo of One Apple on Table"
#     image = pipe(prompt, num_inference_steps=step, tt=off_step, ss=True, guidance_scale=scale).images[0]
#     image.save(savepath + prompt + "_final.png")
#
#     seed_everywhere(seed)
#     prompt = "Photo of One Lemon on Table"
#     image = pipe(prompt, num_inference_steps=step, tt=off_step, ss=False, guidance_scale=scale).images[0]
#     image.save(savepath + prompt + str(off_step) + "_final.png")
#
#     seed_everywhere(seed)
#     prompt = "Photo of One Nectarine on Table"
#     image = pipe(prompt, num_inference_steps=step, tt=off_step, ss=False, guidance_scale=scale).images[0]
#     image.save(savepath + prompt + str(off_step) + "_final.png")
#
#     seed_everywhere(seed)
#     prompt = "Photo of One Plum on Table"
#     image = pipe(prompt, num_inference_steps=step, tt=off_step, ss=False, guidance_scale=scale).images[0]
#     image.save(savepath + prompt + str(off_step) + "_final.png")
#
#     seed_everywhere(seed)
#     prompt = "Photo of One Quince on Table"
#     image = pipe(prompt, num_inference_steps=step, tt=off_step, ss=False, guidance_scale=scale).images[0]
#     image.save(savepath + prompt + str(off_step) + "_final.png")
#
#     seed_everywhere(seed)
#     prompt = "Photo of One Blueberry on Table"
#     image = pipe(prompt, num_inference_steps=step, tt=off_step, ss=False, guidance_scale=scale).images[0]
#     image.save(savepath + prompt + str(off_step) + "_final.png")
#
#     seed_everywhere(seed)
#     prompt = "Photo of One Kiwi fruit on Table"
#     image = pipe(prompt, num_inference_steps=step, tt=off_step, ss=False, guidance_scale=scale).images[0]
#     image.save(savepath + prompt + str(off_step) + "_final.png")
#
#     seed_everywhere(seed)
#     prompt = "Photo of One Persimmon on Table"
#     image = pipe(prompt, num_inference_steps=step, tt=off_step, ss=False, guidance_scale=scale).images[0]
#     image.save(savepath + prompt + str(off_step) + "_final.png")
#
#     seed_everywhere(seed)
#     prompt = "Photo of One Apricot on Table"
#     image = pipe(prompt, num_inference_steps=step, tt=off_step, ss=False, guidance_scale=scale).images[0]
#     image.save(savepath + prompt + str(off_step) + "_final.png")
#
#     off_step += 1



# prompt = "A cup on the desk"
# image = pipe(prompt, num_inference_steps= step, tt= off_step, ss=True, guidance_scale=scale).images[0]
# image.save(savepath + prompt + "_final.png")


