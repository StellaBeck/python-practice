from typing import NamedTuple
from moviepy import ImageClip, TextClip, AudioFileClip, CompositeVideoClip, concatenate_videoclips
from PIL import Image

# ----------------------------
# NamedTuple for each scene
# ----------------------------
class Scene(NamedTuple):
    script: str
    image: str
    audio: str

# ----------------------------
# Helper: center-crop image to target size
# ----------------------------
def center_crop_resize(image_path, target_width, target_height):
    img = Image.open(image_path)
    w, h = img.size

    # Determine crop box (center crop)
    target_ratio = target_width / target_height
    img_ratio = w / h

    if img_ratio > target_ratio:
        # image too wide, crop sides
        new_w = int(h * target_ratio)
        offset = (w - new_w) // 2
        box = (offset, 0, offset + new_w, h)
    else:
        # image too tall, crop top/bottom
        new_h = int(w / target_ratio)
        offset = (h - new_h) // 2
        box = (0, offset, w, offset + new_h)

    cropped = img.crop(box)
    resized = cropped.resize((target_width, target_height))
    return resized

# ----------------------------
# Main function
# ----------------------------
def make_video(scenes, output_path, target_size=(1080, 1080), fps=30):
    clips = []

    for scene in scenes:
        # Load audio
        audio_clip = AudioFileClip(scene.audio)
        duration = audio_clip.duration

        # Load and resize image
        img = center_crop_resize(scene.image, *target_size)
        img_path_temp = "temp_resized.jpg"
        img.save(img_path_temp)

        img_clip = ImageClip(img_path_temp).set_duration(duration)

        # Text overlay
        txt_clip = TextClip(
            scene.script,
            fontsize=40,
            color="white",
            stroke_color="black",
            stroke_width=3,
            method="caption",
            size=(img_clip.w - 100, None),
        ).set_position(("center", "bottom")).set_duration(duration)

        # Combine image + text + audio
        composite = CompositeVideoClip([img_clip, txt_clip]).set_audio(audio_clip)
        clips.append(composite)

    # Concatenate all clips
    final = concatenate_videoclips(clips)
    final.write_videofile(output_path, fps=fps)
