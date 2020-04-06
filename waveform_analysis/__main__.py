import waveform_analysis._common as common
from waveform_analysis.thd import THD
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    common.analyze_channels(args.filename, THD)

