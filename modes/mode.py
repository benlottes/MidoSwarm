"""

"""
from __future__ import annotations

import argparse
from abc import ABCMeta, abstractmethod
from typing import Type


class Mode(metaclass = ABCMeta):
    """
    Need to import any derived modes in __init__.py
    """
    _registry: dict[str, Type[Mode]] = {}

    def __init_subclass__(cls) -> None:
        key = cls.__name__.lower()
        if key in Mode._registry:
            raise TypeError(f'"{key}" already mapped to {Mode._registry[key]}')
        Mode._registry[key] = cls

    @staticmethod
    @abstractmethod
    def define_subparser(self) -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def run(args: argparse.Namespace) -> None:
        raise NotImplementedError

    @staticmethod
    def select_and_run() -> None:
        argparser = Mode._make_argparser()
        args = argparser.parse_args()
        return args.func(args)

    @staticmethod
    def _make_argparser() -> argparse.ArgumentParser:
        argparser = argparse.ArgumentParser(description='Interact with MidoSwarm.')
        subparsers = argparser.add_subparsers(help='Select mode', dest='mode', required=True)

        for name, mode in Mode._registry.items():
            subparser = subparsers.add_parser(name.lower())
            mode.define_subparser(subparser)
            subparser.set_defaults(func = mode.run)

        return argparser
