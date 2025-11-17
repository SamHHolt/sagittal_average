import numpy as np

data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

"""Using git bisect the first bad commit was found to be:
baef87988e0e44ac753987206ae80b65fa3a906e is the first bad commit
commit baef87988e0e44ac753987206ae80b65fa3a906e
Author: Charlene Bultoc <c.bultoc@neurolab.ac.uk>
Date:   Sun Sep 29 05:35:31 2019 +0100

    Uses numpy to calculate the average

 sagittal_brain.py | 8 ++++----
 1 file changed, 4 insertions(+), 4 deletions(-).
 
Recommended change:
averages = planes.mean(axis=0)[np.newaxis, :] -> averages = planes.mean(axis=1)[np.newaxis, :]
 """