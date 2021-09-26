import argparse
from pathlib import Path
from typing import Iterator

from common.models import ClinicalTrialDrug, PubMedDrug, JournalDrug
from common.utils import read_csv, write_csv


def _yield_journal_drug(pubmed_drug_file: Path, clinical_drug_file: Path) -> Iterator[JournalDrug]:
    pubmed_drug_data = read_csv(lambda x: PubMedDrug(*x), False, pubmed_drug_file)

    for pubmed_drug in pubmed_drug_data:
        yield JournalDrug(pubmed_drug.title, pubmed_drug.date, pubmed_drug.journal, pubmed_drug.atccode,
                          pubmed_drug.name)

    clinical_drug_data = read_csv(lambda x: ClinicalTrialDrug(*x), False, clinical_drug_file)
    for clinical_drug in clinical_drug_data:
        yield JournalDrug(clinical_drug.scientific_title, clinical_drug.date, clinical_drug.journal,
                          clinical_drug.atccode, clinical_drug.name)


def main(pubmed_drug_file: Path, clinical_drug_file: Path, output_file: Path) -> None:
    write_csv(output_file, _yield_journal_drug(pubmed_drug_file, clinical_drug_file),
              lambda x: [x.title, x.date, x.journal, x.atccode, x.name])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--drug_file', required=True, help='drug file')
    parser.add_argument('--clinical_trials_file', required=True, help='clinical trials file')
    parser.add_argument('--output_file', required=True, help='output aggregated file in csv format')
    args = parser.parse_args()
