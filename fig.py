import numpy as np
import matplotlib.pyplot as plt


iterations = np.arange(19).astype(int)
metric_value = np.array([-0.055, -0.12, -0.125, -0.275, -0.295, -0.405, -0.365, -0.457, -0.41, -0.46, -0.425, -0.457, -0.45, -0.457, -0.453, -0.454, -0.455, -0.456, -0.457])
print(metric_value.shape, iterations)

n=19
plt.plot(iterations[:n], metric_value[:n], "r")
plt.ylim((-0.5, 0))
plt.xticks(iterations)
plt.xlabel("Iterations")
plt.ylabel("Metric value")
plt.savefig("metric4.pdf", bbox_inches = 'tight',
    pad_inches = 0)
plt.show()
