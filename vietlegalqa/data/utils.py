"""IMPORTS"""
import dataclasses
import json
import pickle
from typing import Dict, Iterator, List, Union
from datasets import Dataset as hf_dataset

FIELD = list(["id"])
DOC_FIELD = list(
    [
        FIELD[0],
        "title",
        "summary",
        "context",
    ]
)
QA_FIELD = list(
    [
        FIELD[0],
        "article",
        "question",
        "answer",
        "start",
        "type",
        "is_impossible",
    ]
)


@dataclasses.dataclass
class Field:
    """
    A placeholder for a future implementation.
    """

    @property
    def id(self) -> str:
        """
        Access the index field name of the dataset.
        """
        return FIELD[0]


@dataclasses.dataclass
class DocField(Field):
    """
    The dataclass presenting the default field name (or column name) of the `Document` class.
    """

    @property
    def title(self) -> str:
        """
        Access the title field name of the dataset.
        """
        return FIELD[1]

    @property
    def summary(self) -> str:
        """
        Access the summary field name of the dataset.
        """
        return FIELD[2]

    @property
    def context(self) -> str:
        """
        Access the context field name of the dataset.
        """
        return FIELD[3]


@dataclasses.dataclass
class QAField(Field):
    """
    The dataclass presenting the default field name (or column name) of the `QADataset` class.
    """

    @property
    def article(self) -> str:
        """
        Access the article field name of the dataset.
        """
        return FIELD[1]

    @property
    def question(self) -> str:
        """
        Access the question field name of the dataset.
        """
        return FIELD[2]

    @property
    def answer(self) -> str:
        """
        Access the answer field name of the dataset.
        """
        return FIELD[3]

    @property
    def start(self) -> str:
        """
        Access the start field name of the dataset.
        """
        return FIELD[4]

    @property
    def type(self) -> str:
        """
        Access the type field name of the dataset.
        """
        return FIELD[5]

    @property
    def is_impossible(self) -> str:
        """
        Access the is_impossible field name of the dataset.
        """
        return FIELD[6]


def get_extension(filename: str, filetype: str = None) -> str:
    """
    Convert the filename into a formatted one with file extension if the filename does not contain the extension, otherwise return the unchanged filename.

    Args:
        filename (`str`):
            The name of the file.
        type (`str`, default to `None`):
            The desired file extension. It can be either "json" or "pickle". If no `type` is provided, the function will return the filename as is.

    Returns:
        (`str`)
            The filename with the specified extension. If the filename does not already have the specified extension, it will be added.

    Examples:

    Convert a filename that does not have an extension to the `json` type:

    ```py
    >>> filename = get_extension("abc", "json")
    >>> filename
    'abc.json'
    ```

    Convert a filename that already has an extension of `pickle` type:

    ```py
    >>> filename = get_extension("abc.pkl", "pickle")
    >>> filename
    'abc.pkl'
    ```
    """
    match filetype:
        case "json":
            return (
                f"{filename.strip()}.json"
                if not filename.strip().endswith(".json")
                else filename.strip()
            )
        case "pickle":
            return (
                f"{filename.strip()}.pkl"
                if not filename.strip().endswith(".pkl")
                else filename.strip()
            )
        case _:
            return filename.strip()


class Entry:
    """
    Abstract class, presenting an element of an instance of the class `Dataset`.
    """

    def __init__(
        self,
        index: str = None,
    ) -> None:
        """
        Initializes an entry with an optional id parameter.

        Args:
            id (`str`, default to `None`):
                The identifier for the entry.
        """
        self._id = index

    @property
    def id(self):
        """Access to the ID of this entry."""
        return self._id

    @id.setter
    def id(self, value):
        """Set the ID of this entry."""
        self._id = value

    def __call__(
        self, key: str = None
    ) -> Union[str, Dict[str, Union[str, None]], None]:
        """
        Returns the value of a specific field if the key matches, otherwise returns a dictionary representation of the object.

        Args:
            key (`str`, default to `None`):
                The `key` parameter is an optional string that represents the property needed to be accessed.

        Returns:
            `str` or `dict`

        Examples:

        Access the ID of the entry:

        ```py
        >>> entry = Entry(id='id_00')
        >>> entry('id')
        'id_00'
        ```

        Call the dictionary of the entry:

        ```py
        >>> entry = Entry(id='id_00')
        >>> entry()
        {'id':'id_00'}
        ```
        """
        try:
            match key:
                case Field.id:
                    return self.id
                case _:
                    return self.to_dict()
        except Exception as e:
            raise e

    def __getitem__(self, key: str) -> Union[str, None]:
        """
        Returns the value of a specific field if the key matches, otherwise returns None.

        Args:
            key (`str`, default to `None`):
                The `key` parameter is an optional string that represents the property needed to be accessed.

        Returns:
            `str` or `NoneType`

        Examples:

        Access the ID of the entry:

        ```py
        >>> entry = Entry(id='id_00')
        >>> entry['id']
        'id_00'
        ```
        """
        try:
            match key:
                case Field.id:
                    return self.id
                case _:
                    return None
        except Exception as e:
            raise e

    def __str__(self) -> str:
        try:
            return str(self.__call__())
        except Exception as e:
            raise e

    def __repr__(self) -> str:
        try:
            return str(self.__call__())
        except Exception as e:
            raise e

    def to_list(self) -> List[Union[str, None]]:
        """
        Converts all the properties of the entry to a list.

        Returns:
          The method `to_list` is returning a list containing the value of `self.id`.
        """
        try:
            return list([self.id])
        except Exception as e:
            raise e

    def to_dict(self) -> Dict[str, Union[str, None]]:
        """
        Converts all the properties of the entry to a dictionary.

        Returns:
          The method `to_list` is returning a list containing the value of `self.id`.
        """
        try:
            return dict({FIELD[idx]: field for idx, field in enumerate(self.to_list())})
        except Exception as e:
            raise e


class Dataset:
    """
    Abstract class, represent a dataset.
    """

    def __init__(self) -> None:
        self.data: Dict[str, Entry] = {}

    def __call__(self) -> Dict[str, Entry]:
        try:
            return self.data
        except Exception as e:
            raise e

    def __len__(self) -> int:
        try:
            return len(self.data)
        except Exception as e:
            raise e

    def __getitem__(
        self, key: Union[str, int, slice]
    ) -> Union[Entry, list[Entry], None]:
        try:
            match key:
                case str():
                    return self.data.get(key, Entry())
                case int():
                    return list(self.data.values())[key]
                case slice():
                    return list(self.data.values())[key]
                case _:
                    return None
        except Exception as e:
            raise e

    def __iter__(self) -> Iterator[Entry]:
        try:
            return iter(self.data.values())
        except Exception as e:
            raise e

    def __str__(self) -> str:
        try:
            return "\n\n".join(map(str, self.to_list()))
        except Exception as e:
            raise e

    def __repr__(self) -> str:
        try:
            return str(self.__call__())
        except Exception as e:
            raise e

    def append(self, entry: Entry):
        """
        The function appends an entry to a dictionary called "data" using the entry's id as the key.

        Args:
          entry (Entry): The parameter "entry" is of type "Entry".
        """
        try:
            self.data[entry.id] = entry
        except Exception as e:
            raise e

    def extend(self, entries: List[Entry]):
        """
        The function extends a dictionary by adding entries with their IDs as keys.

        Args:
          entries (List[Entry]): The `entries` parameter is a list of `Entry` objects.
        """
        try:
            for entry in entries:
                self.data[entry.id] = entry
        except Exception as e:
            raise e

    def to_list(self) -> List[Dict[str, str | None]]:
        """
        The function `to_list` converts the values of a dictionary into a list of dictionaries, where
        each dictionary represents an entry and contains string key-value pairs.

        Returns:
          The code is returning a list of dictionaries, where each dictionary contains string keys and
        string or None values.
        """
        try:
            return list([entry.to_dict() for entry in self.data.values()])
        except Exception as e:
            raise e

    def to_dataset(self) -> hf_dataset:
        """
        The function converts a custom object to a Hugging Face dataset object.

        Returns:
          The code is returning an instance of `hf_dataset` class.
        """
        try:
            return hf_dataset.from_list(self.to_list())
        except Exception as e:
            raise e

    def to_json(self, path: str, indent: int = 4, ensure_ascii: bool = False) -> None:
        """
        The function `to_json` converts an object to JSON format and saves it to a file specified by the
        `path` parameter, with optional parameters for indentation and ASCII encoding.

        Args:
          path (str): The `path` parameter is a string that specifies the file path where the JSON data
        will be saved.
          indent (Optional[int]): The `indent` parameter specifies the number of spaces to use for
        indentation in the JSON output. If `indent` is not provided, the default value is 4. Defaults to
        4
          ensure_ascii (Optional[bool]): The `ensure_ascii` parameter is a boolean flag that specifies
        whether non-ASCII characters in the JSON output should be escaped or not. If `ensure_ascii` is
        set to `True`, all non-ASCII characters will be escaped using the  notation. If `ensure_ascii` is. Defaults to False
        """
        try:
            with open(
                file=get_extension(filename=path, filetype="json"),
                mode="w",
                encoding="utf-8",
            ) as file:
                json.dump(
                    obj=self.to_list(),
                    fp=file,
                    ensure_ascii=ensure_ascii,
                    indent=indent,
                )
        except Exception as e:
            raise e

    def to_pickle(self, path: str) -> None:
        """
        The function `to_pickle` saves an object to a pickle file at the specified path.

        Args:
          path (str): The `path` parameter is a string that represents the file path where the pickled
        object will be saved.
        """
        try:
            with open(
                file=get_extension(filename=path, filetype="pickle"),
                mode="wb",
            ) as file:
                pickle.dump(obj=self, file=file, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            raise e

    def push_to_hub(self, repo_id: str, token: str):
        """
        The function pushes a dataset to a specified path on a hub using a provided token.

        Args:
          path (str): The `path` parameter is a string that represents the path where you want to push
        the dataset to on the hub. It specifies the location where the dataset will be stored on the
        hub.
          token (str): The `token` parameter is a string that represents the access token for the
        repository where you want to push the dataset. This token is used to authenticate and authorize
        the push operation.
        """
        try:
            self.to_dataset().push_to_hub(repo_id=repo_id, token=token)
        except Exception as e:
            raise e
