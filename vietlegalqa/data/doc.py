"""IMPORTS"""
from typing import Dict, Iterator, List, Union

from .utils import Entry, Dataset
from .utils import DOC_FIELD as FIELD, DocField as Field


class Article(Entry):
    """
    subclass of the Entry class, representing an element of a document dataset.
    """

    def __init__(
        self,
        index: str = None,
        title: str = None,
        summary: List[str] = None,
        context: List[str] = None,
    ) -> None:
        super().__init__(index=index)
        self._title = title
        self._summary = summary
        self._context = context

    @property
    def title(self):
        """Access to the title of this entry."""
        return self._title

    @title.setter
    def title(self, value):
        """Set the title of this entry."""
        self._title = value

    @property
    def summary(self):
        """Access to the summary of this entry."""
        return self._summary

    @summary.setter
    def summary(self, value):
        """Set the summary of this entry."""
        self._summary = value

    @property
    def context(self):
        """Access to the context of this entry."""
        return self._context

    @context.setter
    def context(self, value):
        """Set the context of this entry."""
        self._context = value

    def __call__(
        self, key: str = None
    ) -> Union[str, List[str], Dict[str, Union[str, List[str], None]], None]:
        try:
            match key:
                case Field.id:
                    return self.id
                case Field.title:
                    return self.title
                case Field.summary:
                    return self.summary
                case Field.context:
                    return self.context
                case _:
                    return self.to_dict()
        except Exception as e:
            raise e

    def __getitem__(self, key: str) -> Union[str, List[str], None]:
        try:
            match key:
                case Field.id:
                    return self.id
                case Field.title:
                    return self.title
                case Field.summary:
                    return self.summary
                case Field.context:
                    return self.context
                case _:
                    return None
        except Exception as e:
            raise e

    def to_list(self) -> List[Union[str, List[str], None]]:
        try:
            return list([self.id, self.title, self.summary, self.context])
        except Exception as e:
            raise e

    def to_dict(self) -> Dict[str, Union[str, List[str], None]]:
        try:
            return dict({FIELD[idx]: field for idx, field in enumerate(self.to_list())})
        except Exception as e:
            raise e


class Document(Dataset):
    """
    Subclass of the Dataset class, representing a collection of document
    """

    def __init__(
        self,
        data: Union[
            List[Dict[str, Union[str, List[str]]]], Dict[str, List[str]]
        ] = None,
        field: List[str] = None,
    ) -> None:
        super().__init__()
        self.data: Dict[str, Article] = {}
        try:
            match data:
                case list():
                    for entry in data:
                        self.data[entry[field[0]]] = Article(
                            index=entry[field[0]],
                            title=entry[field[1]],
                            summary=entry[field[2]],
                            context=entry[field[3]],
                        )
                case dict():
                    for idx, index in enumerate(data[field[0]]):
                        self.data[index] = Article(
                            index=index,
                            title=data[field[1]][idx],
                            summary=data[field[2]][idx],
                            context=data[field[3]][idx],
                        )
                case _:
                    pass
        except Exception as e:
            raise e

    def __getitem__(
        self, key: Union[str, int, slice]
    ) -> Union[Article, list[Article], None]:
        try:
            match key:
                case str():
                    return self.data.get(key, Article())
                case int():
                    return list(self.data.values())[key]
                case slice():
                    return list(self.data.values())[key]
                case _:
                    return None
        except Exception as e:
            raise e

    def __iter__(self) -> Iterator[Article]:
        try:
            return iter(self.data.values())
        except Exception as e:
            raise e

    def append(self, entry: Article):
        try:
            self.data[entry.id] = entry
        except Exception as e:
            raise e

    def extend(self, entries: List[Article]):
        try:
            for entry in entries:
                self.data[entry.id] = entry
        except Exception as e:
            raise e
