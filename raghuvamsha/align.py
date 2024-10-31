# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "py3-aeneas",
# ]
# ///
import json
import sys

# Use `py3-aeneas` instead of `aeneas` because of installation error:
# https://github.com/readbeyond/aeneas/issues/306
import aeneas
from aeneas.executetask import ExecuteTask
from aeneas.task import Task
from aeneas.runtimeconfiguration import RuntimeConfiguration


def align(text_path, audio_path, align_out_path):
    # create Task object
    config_string = '|'.join(["task_language=hi",
                              "os_task_file_format=json",
                              "os_task_file_levels=3",
                              "is_text_type=mplain"])
    rconf = RuntimeConfiguration()
    rconf[RuntimeConfiguration.MFCC_MASK_NONSPEECH] = True
    rconf[RuntimeConfiguration.MFCC_MASK_NONSPEECH_L3] = True

    task = Task(config_string=config_string)
    task.text_file_path_absolute = text_path
    task.audio_file_path_absolute = audio_path
    task.sync_map_file_path_absolute = align_out_path

    ExecuteTask(task, rconf=rconf).execute()

    # output sync map to file
    task.output_sync_map_file()
    # Write back the file using Unicode characters (like "च")
    # instead of Unicode escapes (like "\u091a").
    with open(align_out_path, 'r', encoding='utf8') as f:
        alignment = json.load(f)
    with open(align_out_path, 'w', encoding='utf8') as f:
        json.dump(alignment, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    # Usage: align.py text.txt audio.mp3 output.json
    align(*sys.argv[1:4])
