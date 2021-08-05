import argparse
from .wolf_goat_cabbage import Graph


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path of the text file with information about the riddle. ", type=str)
    parser.add_argument("boat_size", help="Size of the boat used in the given riddle. ", type=int)
    args = parser.parse_args()
    g = Graph()
    g.add_start_state(args.path)
    g.get_path(args.boat_size)
    g.visualise()
