import argparse
from pathlib import Path
from typing import List, Iterator

from common.models import ClinicalTrial, Drug, ClinicalTrialDrug
from common.utils import read_drug_file, read_csv, write_csv


def _yield_clinical_trial_drug(drug_file: Path, clinical_trials_file: Path) -> Iterator[ClinicalTrialDrug]:
    drug_data: List[Drug] = list(read_drug_file(drug_file))
    clinical_trials_data: List[ClinicalTrial] = list(read_csv(lambda row: ClinicalTrial(row[0], row[1], row[2], row[3]),
                                                         True, clinical_trials_file))
    for clinical_trial in clinical_trials_data:
        for drug in drug_data:
            if drug.name.lower() in clinical_trial.scientific_title.lower():
                yield ClinicalTrialDrug(clinical_trial.id, clinical_trial.scientific_title, clinical_trial.date,
                                        clinical_trial.journal, drug.atccode, drug.name)


def main(drug_file: Path, clinical_trials_file: Path, output_file: Path) -> None:
    write_csv(output_file, _yield_clinical_trial_drug(drug_file, clinical_trials_file),
              lambda elem: [elem.id, elem.scientific_title, elem.date, elem.journal, elem.atccode, elem.name])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--drug_file', required=True, help='drug file')
    parser.add_argument('--clinical_trials_file', required=True, help='clinical trials file')
    parser.add_argument('--output_file', required=True, help='output aggregated file in csv format')
    args = parser.parse_args()
    main(Path(args.drug_file), Path(args.clinical_trials_file), Path(args.output_file))
