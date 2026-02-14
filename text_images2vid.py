import os
#from moviepy.editor import *
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
from PIL import Image
import soundfile as sf
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

# ---------------------------
# 1. SETUP PATHS
# ---------------------------
IMAGE_FOLDER = "images"
SCRIPT_PATH = "script.txt"
OUTPUT_VIDEO = "final_video.mp4"
TEMP_AUDIO_FOLDER = "audio"
TEMP_FRAME_FOLDER = "frames"

os.makedirs(TEMP_AUDIO_FOLDER, exist_ok=True)
os.makedirs(TEMP_FRAME_FOLDER, exist_ok=True)

# ---------------------------
# 2. LOAD OPENVOICE TTS
# ---------------------------
print("Loading OpenVoice model...")
tts = pipeline(
    task=Tasks.text_to_speech,
    model="openvoice",
    model_revision="v1.0.0",
    model_dir="openvoice",
)

# ---------------------------
# 3. READ IMAGES FROM FOLDER
# ---------------------------
def load_images(folder):
    imgs = []
    for f in sorted(os.listdir(folder)):
        if f.lower().endswith((".jpg", ".jpeg", ".png")):
            imgs.append(os.path.join(folder, f))
    return imgs

images = load_images(IMAGE_FOLDER)
print(f"Loaded {len(images)} images")

# ---------------------------
# 4. READ SCRIPT LINES
# ---------------------------
with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]

print(f"Loaded {len(lines)} spoken lines")

# Ensure same count
if len(lines) != len(images):
    raise ValueError("Number of images must match number of text lines!")

# ---------------------------
# 5. GENERATE AUDIO PER LINE
# ---------------------------
audio_files = []

print("Generating speech...")
for idx, text in enumerate(lines):
    out_path = f"{TEMP_AUDIO_FOLDER}/line_{idx}.wav"

    audio = tts({"text": text})["output_wav"]
    sf.write(out_path, audio, 24000)  # 24 kHz output

    audio_files.append(out_path)
    print(f"Generated TTS: {out_path}")

# ---------------------------
# 6. CREATE CLIPS (Image + Audio)
# ---------------------------
clips = []

for idx, (img_path, audio_path) in enumerate(zip(images, audio_files)):
    # Load audio
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration

    # Resize image to 1080p
    img = Image.open(img_path)
    img = img.resize((1080, 1080))
    fixed_path = f"{TEMP_FRAME_FOLDER}/frame_{idx}.jpg"
    img.save(fixed_path)

    # Create video clip
    clip = ImageClip(fixed_path).set_duration(duration).set_audio(audio_clip)

    clips.append(clip)
    print(f"Created clip {idx}")

# ---------------------------
# 7. CONCAT ALL CLIPS
# ---------------------------
print("Building final video...")
final = concatenate_videoclips(clips, method="compose")
final.write_videofile(OUTPUT_VIDEO, fps=30, codec="libx264", audio_codec="aac")

print("DONE! Video saved as:", OUTPUT_VIDEO)
