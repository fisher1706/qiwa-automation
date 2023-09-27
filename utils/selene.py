from typing import Tuple

from selene.core.condition import Condition
from selene.core.entity import Collection, Element
from selene.core.wait import Query


def index_of_element_by(condition: Condition[Element]):
    def index_if_exist(collection: Collection):
        def matches(indexed_item: Tuple[int, Element]):
            return indexed_item[1].matching(condition)

        cached = collection.cached
        index, _ = next(filter(matches, enumerate(cached)))
        return index

    return Query(
        f"index of element by {condition}",
        index_if_exist,
    )
