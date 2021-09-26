import operator
from collections import defaultdict
from pathlib import Path
from typing import Tuple, Optional

from common.models import JournalDrug
from common.utils import read_csv


def name_most_cited(journal_path: Path) -> Optional[Tuple[str, int]]:
    journal_drug = read_csv(lambda x: JournalDrug(*x), False, journal_path)
    holder = defaultdict(list)
    for journal in journal_drug:
        holder[journal.title].append(journal.name)
    journal_count = {title: len(names) for title, names in holder.items()}
    sorted_journal = sorted(list(journal_count.items()), key=operator.itemgetter(1), reverse=True)
    if sorted_journal:
        first = sorted_journal[0]
        return first[0], first[1]
    else:
        return None