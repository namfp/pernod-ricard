import csv
import functools
from pathlib import Path
from typing import Iterator, TypeVar, List, Callable, Iterable

from common.models import Drug, PubMed


def read_drug_file(drug_file: Path) -> Iterator[Drug]:
    with drug_file.open() as f:
        csv_reader = csv.reader(f, delimiter=",")
        next(csv_reader)  # skip header
        for row in csv_reader:
            if len(row) == 1:
                continue
            yield Drug(row[0], row[1])


T = TypeVar("T")


def write_csv(csv_file: Path, data: Iterator[T], getter: Callable[[T], List[str]]):
    with csv_file.open("w") as f:
        csv_writer = csv.writer(f, delimiter=',')
        for pubmed_drug in data:
            csv_writer.writerow(getter(pubmed_drug))


def read_csv(setter: Callable[[Iterable[str]], T], has_header: bool, file_path: Path) -> Iterator[T]:
    with file_path.open() as f:
        csv_reader = csv.reader(f, delimiter=",")
        if has_header:
            next(csv_reader)
        for row in csv_reader:
            if len(row) > 1:
                yield setter(row)


read_pubmed_file = functools.partial(read_csv, lambda x: PubMed(x[0], x[1], x[2], x[3]), True)
