import argparse
from pathlib import Path
from typing import Iterator

from common.models import PubMedDrug
from common.utils import read_drug_file, write_csv, read_pubmed_file


def execute(pubmed_file: Path, drug_file: Path) -> Iterator[PubMedDrug]:
    drug_data = list(read_drug_file(drug_file))
    for pubmed in read_pubmed_file(pubmed_file):
        for drug in drug_data:
            if drug.name.lower() in pubmed.title.lower():
                yield PubMedDrug(pubmed.id, pubmed.title, pubmed.date, pubmed.journal, drug.atccode, drug.name)


def main(pubmed_file: Path, drug_file: Path, output_file: Path) -> None:
    write_csv(output_file, execute(pubmed_file, drug_file),
              lambda pubmed_drug: [pubmed_drug.id, pubmed_drug.title, pubmed_drug.date, pubmed_drug.journal,
                                   pubmed_drug.atccode, pubmed_drug.name])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--pubmed_file', required=True, help='pubmed file')
    parser.add_argument('--drug_file', required=True, help='drug file')
    parser.add_argument('--output_file', required=True, help='output file')
    args = parser.parse_args()
    main(Path(args.pubmed_file), Path(args.drug_file), Path(args.output_file))


