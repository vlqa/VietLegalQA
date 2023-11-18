"""IMPORTS"""
import json
import pickle
from typing import Any, List, Tuple, Union
from datasets import load_dataset

from .doc import Document
from .qa import QADataset
from .utils import DOC_FIELD, QA_FIELD, get_extension


def load_document_hf(
    path: str,
    split: str = "train",
    field: List[str] = None,
    select: Union[int, Tuple[int, int], Tuple[int, int, int]] = None,
) -> Document:
    try:
        match select:
            case None:
                return Document(data=load_dataset(path)[split].to_list(), field=field)
            case int():
                return Document(
                    data=load_dataset(path)[split].select(range(select)).to_list(),
                    field=field,
                )
            case tuple():
                return (
                    Document(
                        data=load_dataset(path, split=split)
                        .select(range(select[0], select[1]))
                        .to_list(),
                        field=field,
                    )
                    if len(select) == 2
                    else Document(
                        data=load_dataset(path, split=split)
                        .select(range(select[0], select[1], select[2]))
                        .to_list(),
                        field=field,
                    )
                )
    except Exception as e:
        raise e


def load_document(
    path: str, filetype: str = None, field: List[str] = None
) -> Union[Document, Any, None]:
    try:
        field = DOC_FIELD if field is None else field
        match filetype:
            case "json":
                with open(
                    file=get_extension(filename=path, filetype="json"),
                    mode="r",
                    encoding="utf-8",
                ) as file:
                    return Document(data=json.load(fp=file), field=field)
            case "pickle":
                with open(
                    file=get_extension(filename=path, filetype="pickle"),
                    mode="rb",
                ) as file:
                    return pickle.load(file=file)
    except Exception as e:
        raise e


def load_qa_hf(
    path: str,
    split: str = "train",
    field: List[str] = None,
    select: Union[int, Tuple[int, int], Tuple[int, int, int]] = None,
) -> QADataset:
    try:
        match select:
            case None:
                return QADataset(data=load_dataset(path)[split].to_list(), field=field)
            case int():
                return QADataset(
                    data=load_dataset(path)[split].select(range(select)).to_list(),
                    field=field,
                )
            case tuple():
                return (
                    QADataset(
                        data=load_dataset(path, split=split)
                        .select(range(select[0], select[1]))
                        .to_list(),
                        field=field,
                    )
                    if len(select) == 2
                    else QADataset(
                        data=load_dataset(path, split=split)
                        .select(range(select[0], select[1], select[2]))
                        .to_list(),
                        field=field,
                    )
                )
    except Exception as e:
        raise e


def load_qa(
    path: str, filetype: str = None, field: List[str] = None
) -> Union[QADataset, Any, None]:
    try:
        field = QA_FIELD if field is None else field
        match filetype:
            case "json":
                with open(
                    file=get_extension(filename=path, filetype="json"),
                    mode="r",
                    encoding="utf-8",
                ) as file:
                    return QADataset(data=json.load(fp=file), field=field)
            case "pickle":
                with open(
                    file=get_extension(filename=path, filetype="pickle"),
                    mode="rb",
                ) as file:
                    return pickle.load(file=file)
    except Exception as e:
        raise e
