import numpy as np
import subprocess


def test_sagittal_brain_average():
    input_array= np.arange(1, 401).reshape(20, 20)
    expected_array= np.arange(10.5, 401, 20).reshape(20,) 
    np.savetxt("brain_sample.csv", input_array, fmt='%d', delimiter=',')
    
    subprocess.run(["python3", "sagittal_brain.py"])
    output_array= np.loadtxt("brain_average.csv",  delimiter=',')

    np.testing.assert_array_equal(output_array, expected_array)

if __name__ == "__main__":
    test_sagittal_brain_average()
