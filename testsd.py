from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float32
)

# Force CPU
pipe.to("cpu")

prompt = "a futuristic robot cat, digital art, blue lighting"

image = pipe(prompt, num_inference_steps=20).images[0]

image.save("output.png")
