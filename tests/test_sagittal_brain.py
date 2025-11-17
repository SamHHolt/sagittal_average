import numpy as np
import subprocess
from pathlib import Path


script_dir = Path(__file__).resolve().parent       # src/sagittal_average
project_root = script_dir.parents[0]               # adjust number to reach repo root

def test_sagittal_brain_average():
    input_array= np.arange(1, 401).reshape(20, 20)
    expected_array= np.arange(10.5, 401, 20).reshape(20,) 
    np.savetxt(project_root / "tests" / "test_brain_sample.csv", input_array, fmt='%d', delimiter=',')
    subprocess.run(["python3", project_root / "src" / "sagittal_average" / "sagittal_brain.py", project_root / "tests" / "test_brain_sample.csv", "--file_output", project_root / "tests" / "test_brain_average.csv"], check=True)
    output_array= np.loadtxt(project_root / "tests" / "test_brain_average.csv",  delimiter=',')

    np.testing.assert_array_equal(output_array, expected_array)

if __name__ == "__main__":
    test_sagittal_brain_average()
