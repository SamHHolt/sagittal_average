from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

import numpy as np
from pathlib import Path


def run_averages(file_input='brain_sample.csv', file_output='brain_average.csv'):
    """
    Calculates the average through the coronal planes
    The input file should has as many columns as coronal planes
    The rows are intersections of the sagittal/horizontal planes

    The result is the average for each sagittal/horizontal plane (rows)
    """
    script_dir = Path(__file__).resolve().parent       # src/sagittal_average
    project_root = script_dir.parents[1]               # adjust number to reach repo root
    input_file = project_root / "docs" / file_input
    output_file = project_root / "docs" / file_output
    # Open the file to analyse
    planes = np.loadtxt(input_file, dtype=int,  delimiter=',')

    # Calculates the averages through the sagittal/horizontal planes
    # and makes it as a row vector
    averages = planes.mean(axis=1)[np.newaxis, :]

    # write it out on my file
    np.savetxt(output_file, averages, fmt='%.1f', delimiter=',')

