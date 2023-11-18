"""IMPORTS"""
from typing import Dict, Iterator, List, Union

from .doc import Article, Document
from .utils import Entry, Dataset
from .utils import QA_FIELD as FIELD, QAField as Field


class QAPair(Entry):
    def __init__(
        self,
        index: str = None,
        article: str = None,
        question: str = None,
        answer: str = None,
        start: int = None,
        ans_type: str = None,
        is_impossible: bool = False,
    ) -> None:
        super().__init__(index=index)
        self._article = article
        self._question = question
        self._answer = answer
        self._start = start
        self._type = ans_type.upper()
        self._is_impossible = is_impossible

    @property
    def article(self):
        """Access to the article of this entry."""
        return self._article

    @article.setter
    def article(self, value):
        """Set the article of this entry."""
        self._article = value

    @property
    def question(self):
        """Access to the question of this entry."""
        return self._question

    @question.setter
    def question(self, value):
        """Set the question of this entry."""
        self._question = value

    @property
    def answer(self):
        """Access to the answer of this entry."""
        return self._answer

    @answer.setter
    def answer(self, value):
        """Set the answer of this entry."""
        self._answer = value

    @property
    def start(self):
        """Access to the start of this entry."""
        return self._start

    @start.setter
    def start(self, value):
        """Set the start of this entry."""
        self._start = value

    @property
    def type(self):
        """Access to the type of this entry."""
        return self._type

    @type.setter
    def type(self, value):
        """Set the summary of this entry."""
        self._type = value

    @property
    def is_impossible(self):
        """Access to the is_impossible of this entry."""
        return self._is_impossible

    @is_impossible.setter
    def is_impossible(self, value):
        """Set the context of this entry."""
        self._is_impossible = value

    def __call__(self, key: str = None) -> Union[str, int, bool, Dict, None]:
        try:
            match key:
                case Field.id:
                    return self.id
                case Field.article:
                    return self.article
                case Field.question:
                    return self.question
                case Field.answer:
                    return self.answer
                case Field.start:
                    return self.start
                case Field.type:
                    return self.type
                case Field.is_impossible:
                    return self.is_impossible
                case _:
                    return self.to_dict()
        except Exception as e:
            raise e

    def __getitem__(self, key: str = None) -> Union[str, int, bool, None]:
        try:
            match key:
                case Field.id:
                    return self.id
                case Field.article:
                    return self.article
                case Field.question:
                    return self.question
                case Field.answer:
                    return self.answer
                case Field.start:
                    return self.start
                case Field.type:
                    return self.type
                case Field.is_impossible:
                    return self.is_impossible
                case _:
                    return None
        except Exception as e:
            raise e

    def __eq__(self, __value: object) -> bool:
        try:
            if isinstance(__value, QAPair):
                return bool(
                    self.article == __value.article
                    and self.question == __value.question
                    and self.answer == __value.answer
                    and self.start == __value.start
                )
            return False
        except Exception as e:
            raise e

    def __ne__(self, __value: object) -> bool:
        try:
            if isinstance(__value, QAPair):
                return bool(
                    self.article != __value.article
                    and self.question != __value.question
                    and self.answer != __value.answer
                    and self.start != __value.start
                )
            return False
        except Exception as e:
            raise e

    def __lt__(self, __value: object) -> bool:
        try:
            if isinstance(__value, QAPair):
                if self.article < __value.article:
                    return True
                if self.question < __value.question:
                    return True
                if self.answer < __value.answer:
                    return True
                if self.start < __value.start:
                    return True
                return False
            return False
        except Exception as e:
            raise e

    def __gt__(self, __value: object) -> bool:
        try:
            if isinstance(__value, QAPair):
                if self.article > __value.article:
                    return True
                if self.question > __value.question:
                    return True
                if self.answer > __value.answer:
                    return True
                if self.start > __value.start:
                    return True
                return False
            return False
        except Exception as e:
            raise e

    def __le__(self, __value: object) -> bool:
        try:
            if isinstance(__value, QAPair):
                if self.article <= __value.article:
                    return True
                if self.question <= __value.question:
                    return True
                if self.answer <= __value.answer:
                    return True
                if self.start <= __value.start:
                    return True
                return False
            return False
        except Exception as e:
            raise e

    def __ge__(self, __value: object) -> bool:
        try:
            if isinstance(__value, QAPair):
                if self.article >= __value.article:
                    return True
                if self.question >= __value.question:
                    return True
                if self.answer >= __value.answer:
                    return True
                if self.start >= __value.start:
                    return True
                return False
            return False
        except Exception as e:
            raise e

    def __cmp__(self, __value: object) -> int:
        try:
            if isinstance(__value, QAPair):
                if self == __value:
                    return 0
                if self > __value:
                    return 1
                return -1
            return -1
        except Exception as e:
            raise e

    def to_list(self) -> List[Union[str, int, bool, None]]:
        try:
            return list(
                [
                    self.id,
                    self.article,
                    self.question,
                    self.answer,
                    self.start,
                    self.type,
                    self.is_impossible,
                ]
            )
        except Exception as e:
            raise e

    def to_dict(self) -> Dict[str, Union[str, int, bool, None]]:
        try:
            return dict({FIELD[idx]: field for idx, field in enumerate(self.to_list())})
        except Exception as e:
            raise e

    def get_article(self, document: Document) -> Article:
        """
        The function `get_article` takes a `Document` object and returns the `Article` object associated
        with it.

        Args:
          document (Document): The `document` parameter is of type `Document`. It is expected to be an
        object that contains articles.

        Returns:
          The code is returning an article object from the given document.
        """
        try:
            return document[self.article]
        except Exception as e:
            raise (e)


class QADataset(Dataset):
    def __init__(
        self,
        data: Union[
            List[Dict[str, Union[str, int, bool]]], Dict[str, Union[str, int, bool]]
        ] = None,
        field: List[str] = None,
    ) -> None:
        super().__init__()
        self.data: Dict[str, QAPair] = {}
        try:
            match data:
                case list():
                    for entry in data:
                        self.data[entry[field[0]]] = QAPair(
                            index=entry[field[0]],
                            article=entry[field[1]],
                            question=entry[field[2]],
                            answer=entry[field[3]],
                            start=entry[field[4]],
                            ans_type=entry[field[5]],
                            is_impossible=entry[field[6]],
                        )
                case dict():
                    for idx, index in enumerate(data[field[0]]):
                        self.data[index] = QAPair(
                            index=index,
                            article=data[field[1]][idx],
                            question=data[field[2]][idx],
                            answer=data[field[3]][idx],
                            start=data[field[4]][idx],
                            ans_type=data[field[5]][idx],
                            is_impossible=data[field[6]][idx],
                        )
                case _:
                    pass
        except Exception as e:
            raise e

    def __getitem__(
        self, key: Union[str, int, slice]
    ) -> Union[QAPair, list[QAPair], None]:
        try:
            match key:
                case str():
                    return self.data.get(key, QAPair())
                case int():
                    return list(self.data.values())[key]
                case slice():
                    return list(self.data.values())[key]
                case _:
                    return None
        except Exception as e:
            raise e

    def __iter__(self) -> Iterator[QAPair]:
        try:
            return iter(self.data.values())
        except Exception as e:
            raise e

    def __contains__(self, value: QAPair) -> bool:
        try:
            return (
                value.article in self.to_list(key="article")
                and value.question in self.to_list(key="question")
                and value.answer in self.to_list(key="answer")
                and value.start in self.to_list(key="start")
            )
        except Exception as e:
            raise e

    def append(self, entry: QAPair):
        try:
            self.data[entry.id] = entry
        except Exception as e:
            raise e

    def extend(self, entries: List[QAPair]):
        try:
            for entry in entries:
                self.data[entry.id] = entry
        except Exception as e:
            raise e

    def to_list(self, key: str = None) -> List[Dict[str, str | None]]:
        """
        The function `to_list` converts the values of a dictionary into a list of dictionaries, where
        each dictionary represents an entry and contains string key-value pairs.

        Returns:
          The code is returning a list of dictionaries, where each dictionary contains string keys and
        string or None values.
        """
        try:
            match key:
                case None:
                    return list(entry.to_dict() for entry in self.data.values())
                case "article":
                    return list(entry.article for entry in self.data.values())
                case "question":
                    return list(entry.question for entry in self.data.values())
                case "answer":
                    return list(entry.answer for entry in self.data.values())
                case "start":
                    return list(entry.start for entry in self.data.values())
                case "type":
                    return list(entry.type for entry in self.data.values())
                case _:
                    return list(entry.to_dict() for entry in self.data.values())
        except Exception as e:
            raise e

    def get_article(self, index: str, document: Document) -> Article:
        try:
            return document[self.data[index]]
        except Exception as e:
            raise e
