#!/bin/sh

mkdir -p alignment
for f in audio/Raghuvamsha-Sarga*.mp3; do
    g=$(basename "$f" .mp3)
    echo "Processing: $g"
    uv run align.py "text/$g.txt" "audio/$g.mp3" "alignment/$g.json"
done
