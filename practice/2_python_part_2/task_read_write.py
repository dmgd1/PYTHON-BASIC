"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os
from typing import AnyStr

all_files = os.listdir(f'{os.getcwd()}/files/')
merged_content_file = f'{os.getcwd()}/files/merged_content_from_all_files.txt'


def merge_files(*files) -> AnyStr:
    with open(merged_content_file, 'w+', encoding="utf-8") as merged_content_f:
        merged_content = []
        for file in files[0]:
            current_file = f'{os.getcwd()}/files/{file}'
            with open(current_file, 'r', encoding='utf-8') as f:
                data = f.read()
                merged_content.append(data)

        merged_content_f.write(', '.join(merged_content))

    with open(merged_content_file, 'r', encoding="utf-8") as f:
        return f.read()


print(merge_files(all_files))
