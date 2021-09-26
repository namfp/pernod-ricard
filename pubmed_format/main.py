import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

from common.utils import write_csv, read_csv, read_pubmed_file


@dataclass
class PubMed:
    id: str
    title: str
    date: str  # TODO: control date type
    journal: str


def _process_json_file(json_file: Path) -> Iterator[PubMed]:
    with json_file.open() as f:
        data = json.load(f)
        for elem in data:
            yield PubMed(elem["id"], elem["title"], elem["date"], elem["journal"])


def _yield_line(input_folder: Path):
    for file_path in input_folder.iterdir():
        if file_path.is_file() and file_path.name.endswith(".json"):
            yield from _process_json_file(file_path)
        elif file_path.is_file() and file_path.name.endswith(".csv"):
            yield from read_pubmed_file(file_path)


def execute(input_folder: Path, output_file: Path) -> None:
    if not input_folder.is_dir():
        raise Exception(f"Input folder {input_folder} is not a folder")
    write_csv(output_file, _yield_line(input_folder),
              lambda pubmed: [pubmed.id, pubmed.title, pubmed.date, pubmed.journal])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_folder', required=True, help='input folder')
    parser.add_argument('--output_file', required=True, help='output aggregated file in csv format')
    args = parser.parse_args()
    execute(Path(args.input_folder), (args.output_file))


if __name__ == "__main__":
    pass
