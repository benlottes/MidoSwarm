"""

"""

import argparse

from modes.mode import Mode
from core.simulation import Simulation
from core.visitors import Simulator, Logger


class Train(Mode):

    @staticmethod
    def define_subparser(subparser: argparse.ArgumentParser) -> None:
        pass

    @staticmethod
    def run(args: argparse.Namespace) -> None:
        print('training...')

        simulation = Simulation(visitors=[Simulator(), Logger()])
        for _ in range(1):
            simulation.step()
