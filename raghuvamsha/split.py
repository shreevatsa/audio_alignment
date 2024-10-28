import json
import re
import glob

verses = json.load(open('raghuvamsha.json'))
audio_files = sorted(glob.glob('audio/*.mp3'))

verse_index = 0

for audio_file in audio_files:
    match = re.match(
        r'audio/Raghuvamsha-Sarga(\d+)-(\d+)-(\d+)\.mp3', audio_file)
    assert match, audio_file
    chapter = int(match.group(1))
    start_verse = int(match.group(2))
    end_verse = int(match.group(3))
    # Write verses belonging to this range to the corresponding text file
    txt_filename = audio_file.replace('.mp3', '.txt')
    with open(txt_filename, 'w', encoding='utf-8') as txt_file:
        while verse_index < len(verses):
            verse = verses[verse_index]
            verse_chapter = int(verse['c'])
            verse_number = int(verse['n'])
            if start_verse <= verse_number <= end_verse:
                assert verse_chapter == chapter
                txt_file.write(verse['v'] + '\n')
                verse_index += 1
            else:
                break
    print(f'Generated: {txt_filename}')
