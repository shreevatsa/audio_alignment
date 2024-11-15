# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "numpy>=2, <2.1",
#     "librosa",
# ]
# ///
import json
import logging
import sys

import librosa
import numpy as np


def create_basic_alignment(audio_path, text_path):
    logging.warning('Loading audio')
    y, sr = librosa.load(audio_path)
    logging.warning('Loaded audio')
    duration = librosa.get_duration(y=y, sr=sr)

    # Load text
    with open(text_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    # Create uniform timestamps (one for start of each line)
    # Assuming each line takes equal time
    num_lines = len(lines)
    line_timestamps = np.linspace(0, duration, num_lines + 1)

    # Create word-level alignments
    alignments = []
    for i, line in enumerate(lines):
        line_start = line_timestamps[i]
        line_duration = line_timestamps[i + 1] - line_start

        # Split line into words
        words = [word for word in line.split() if word]

        # Calculate relative durations based on word lengths
        word_lengths = [len(word) for word in words]
        total_length = sum(word_lengths)
        relative_durations = [length/total_length for length in word_lengths]

        # Calculate word timestamps
        word_durations = [fraction *
                          line_duration for fraction in relative_durations]
        word_starts = np.cumsum([line_start] + word_durations[:-1])
        word_ends = word_starts + word_durations

        # Create alignment entry, following the conventions of the other files.
        for j, word in enumerate(words):
            alignments.append({
                'begin': str(word_starts[j]),
                'end': str(word_ends[j]),
                'id': f'p000001s{i+1:06}w{j+1:06}',
                'lines': [word],
            })
    return alignments


if __name__ == "__main__":
    text_path, audio_path, align_out_file = sys.argv[1:4]
    alignments = create_basic_alignment(audio_path, text_path)
    out = {'fragments': alignments}
    json.dump(out, open(align_out_file, 'w'), ensure_ascii=False, indent=2)
