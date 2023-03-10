import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="test for args")
    parser.add_argument("--seed", type=int, default=2022, help="random seed.")
    parser.add_argument('--dropout', type=float, default=0.3, help='dropout ratio')

    parser.add_argument("--i", type=int, default=2022, help="int test.")

    return parser.parse_args()