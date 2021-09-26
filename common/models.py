from dataclasses import dataclass


@dataclass
class PubMed:
    id: str
    title: str
    date: str  # TODO: control date type
    journal: str


DrugName = str


@dataclass
class Drug:
    atccode: str
    name: str


@dataclass
class PubMedDrug:
    id: str
    title: str
    date: str
    journal: str
    atccode: str
    name: str


@dataclass
class ClinicalTrial:
    id: str
    scientific_title: str
    date: str
    journal: str


@dataclass
class ClinicalTrialDrug:
    id: str
    scientific_title: str
    date: str
    journal: str
    atccode: str
    name: str

@dataclass
class JournalDrug:
    title: str
    date: str
    journal: str
    atccode: str
    name: str