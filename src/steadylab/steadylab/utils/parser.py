import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='SteadyLab')
    
    # Add the 'mode' argument
    parser.add_argument('--mode', default='auto', metavar='--m', choices=['test', 'auto'], help='Select mode: test or auto')

    args = parser.parse_args()
    return args