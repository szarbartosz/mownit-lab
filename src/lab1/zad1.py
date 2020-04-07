import numpy as np
from texttable import Texttable

floats = ["type: ", "float16", "float32", "float64"]
precision = ["precision: "]
rangeMin = ["min: "]
rangeMax = ["max: "]
precision.append(np.finfo(np.float16).precision)
rangeMax.append(np.finfo(np.float16).max)
rangeMin.append(np.finfo(np.float16).min)
precision.append(np.finfo(np.float32).precision)
rangeMax.append(np.finfo(np.float32).max)
rangeMin.append(np.finfo(np.float32).min)
precision.append(np.finfo(np.float64).precision)
rangeMax.append(np.finfo(np.float64).max)
rangeMin.append(np.finfo(np.float64).min)

t = Texttable()
t.add_rows([floats,precision,rangeMax,rangeMin])
print(t.draw())