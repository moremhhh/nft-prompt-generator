import pandas as pd
import json
import random

# CSV ফাইলটি লোড করা হচ্ছে
df = pd.read_csv("NFT_DATASET.csv")

# প্রতি কলম থেকে খালি ঘর বাদে ডেটা লিস্টে নেওয়া হচ্ছে
accessories = df['Accessories'].dropna().tolist()
expressions = df['Expressions'].dropna().tolist()
backgrounds = df['Background'].dropna().tolist()
palettes = df['Color palettes'].dropna().tolist()
companions = df['Companion effects'].dropna().tolist()

# প্রম্পটের মূল টেমপ্লেট
template = """Create a premium 3D PFP NFT, 1024x1024.

IMPORTANT:
Use the supplied reference image ONLY to lock the exact body position, framing, camera angle, shoulder crop, head scale and composition.
Never change pose, never tilt camera, never rotate body.
Half-body profile-picture framing only.

Ultra-clean, high-definition render with smooth lighting, soft shadows, crisp edges.

Background:
{background}

Color palette:
{palette}

Character body color:
(Automatically determined from the selected Color palette)

Face color:
(Automatically determined from the selected Color palette)

Facial expression:
{expression}

Main accessory/theme:
{accessory}

Companion effect:
{companion}

Do NOT use sunglasses, earrings, crowns, stickers or duplicate accessories in the same location.

Use tasteful, unique, high-quality accessories only when appropriate and avoid clutter."""

prompts_list = []

# ১০,০০০টি ইউনিক/র‍্যান্ডম প্রম্পট জেনারেট করার লুপ
random.seed(42) # ফলাফল সবসময় একই রাখার জন্য seed ব্যবহার করা হয়েছে
for i in range(1, 10001):
    prompt_text = template.format(
        background=random.choice(backgrounds),
        palette=random.choice(palettes),
        expression=random.choice(expressions),
        accessory=random.choice(accessories),
        companion=random.choice(companions)
    )
    
    # JSON ফরম্যাট (id এবং prompt)
    prompts_list.append({
        "id": i,
        "prompt": prompt_text
    })

# JSON ফাইল হিসেবে সেভ করা
with open("nft_prompts_10000.json", "w", encoding="utf-8") as f:
    json.dump(prompts_list, f, indent=4)

print("১০,০০০টি প্রম্পট সফলভাবে nft_prompts_10000.json ফাইলে তৈরি হয়েছে!")
