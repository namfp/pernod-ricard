import pathlib

import pubmed_format.main as pubmed_format

import pubmed_drug.main as pubmed_drug
import clinical_drug.main as clinical_drug
import journal_drug.main as journal_drug
from api.main import name_most_cited


def test_pipeline():
    current_path = pathlib.Path(__file__).parent.resolve()
    pubmed_source = current_path.joinpath("fixtures/pubmed_source")
    pubmed_clean = current_path.joinpath("fixtures/pubmed_clean/output.csv")
    pubmed_clean.parent.mkdir(parents=True, exist_ok=True)
    drug_file = current_path.joinpath("fixtures/drugs.csv")
    clinical_trials_file = current_path.joinpath("fixtures/clinical_trials_source/clinical_trials.csv")
    clinical_trials_drug = current_path.joinpath("fixtures/clinical_trials_drug/clinical_trials_drug.csv")
    clinical_trials_drug.parent.mkdir(parents=True, exist_ok=True)

    pubmed_drug_file = current_path.joinpath("fixtures/pubmed_drug/pubmed_drug.csv")

    pubmed_drug_file.parent.mkdir(parents=True, exist_ok=True)

    journal_drug_file = current_path.joinpath("fixtures/journal_drug/journal_drug.csv")
    journal_drug_file.parent.mkdir(parents=True, exist_ok=True)

    pubmed_format.execute(pubmed_source, pubmed_clean)
    pubmed_drug.main(pubmed_clean, drug_file, pubmed_drug_file)
    clinical_drug.main(drug_file, clinical_trials_file, clinical_trials_drug)
    journal_drug.main(pubmed_drug_file, clinical_trials_drug, journal_drug_file)
    print(name_most_cited(journal_drug_file))

    assert 1 == 1
