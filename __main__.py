"""
TODO
- map tile system
- classes (agents, map, tile map)
- Neural Network research
- Pygame reseach for rendering
- simulation loop
"""

import os.path as osp, os
import argparse


ROOT_PATH = osp.dirname(osp.realpath(__file__))


def make_argparser() -> argparse.ArgumentParser:
    argparser = argparse.ArgumentParser()
    return argparser


def main() -> None:
    argparser = make_argparser()
    args = argparser.parse_args()


if __name__ == '__main__':
    main()