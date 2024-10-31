import os
import json

def generate_data_json():
    data = {
        "name": "Raghuvamsha",
        "description": "Text Source: <a href='https://sanskritsahitya.org/raghuvansham'>https://sanskritsahitya.org/raghuvansham</a>\n<br>\nAudio Source: <a href='https://archive.org/details/Raghuvamsha-mUlam-vedabhoomi.org'>https://archive.org/details/Raghuvamsha-mUlam-vedabhoomi.org</a>",
        "data": []
    }

    text_dir = "text"
    audio_dir = "audio"
    alignment_dir = "alignment"

    text_files = sorted(os.listdir(text_dir))
    audio_files = sorted(os.listdir(audio_dir))
    alignment_files = sorted(os.listdir(alignment_dir))

    for text_file, audio_file, alignment_file in zip(text_files, audio_files, alignment_files):
        chapter_id = text_file.replace(".txt", "")
        chapter_name = chapter_id.replace("-", " ")

        data["data"].append({
            "id": chapter_id,
            "name": chapter_name,
            "audio_url": f"{audio_dir}/{audio_file}",
            "word_alignment": f"{alignment_dir}/{alignment_file}",
            "text": f"{text_dir}/{text_file}"
        })

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_data_json()
