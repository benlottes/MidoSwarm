"""

"""

import argparse

from modes.mode import Mode
from core.simulation import Simulation
from core.visitors import Simulator, Renderer, Logger


class Game(Mode):

    @staticmethod
    def define_subparser(subparser: argparse.ArgumentParser) -> None:
        pass

    @staticmethod
    def run(args: argparse.Namespace) -> None:
        print('gaming...')

        simulation = Simulation(visitors=[Simulator(), Renderer(), Logger()])
        for _ in range(1):
            simulation.step()
