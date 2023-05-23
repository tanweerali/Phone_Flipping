# IQR outlier detection

from scipy.stats import iqr
from scipy import percentile
import numpy as np



def iqrcleaner(data):
        global iqr
        #Calculate iqr
        q25, q75 = percentile(data,25), percentile(data, 75)
        iqr_ = iqr(data)
        cut_off = iqr_ * 1.5
        lower, upper = q25 - cut_off, q75 + cut_off 
        outliers = [x for x in data if x < lower or x > upper]
        outliers_removed = [x for x in data if x >= lower and x <= upper]
        
        ar = np.array(outliers_removed)
        
        return ar