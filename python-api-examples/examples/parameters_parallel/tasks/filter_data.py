# # Clean Data
#
# Use linear regression and reject outliers from the data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
# + tags=["parameters"]
# parameters
upstream = ["make-data"]

# +
# The code below handles the case where the task is called either as a stand alone task in a serial DAG, or as part of a parallel DAG.
# When called in parallel, the upstream variable is overwritten and is replaced by a nested dictionary 
# with keys corresponding to the name of the upstream task.
upstream_file = upstream['make-data']

if type(upstream_file) is str:
    file = upstream_file
else:
    file = list(upstream_file.values())[0]
output_file = product['file']
max_variance = 2 # filter data more than 2 standard deviations from model


# -

# ## Load Data

# +
# Load file to a pandas dataframe
df = pd.read_csv(file)

df.head()
# -

# ## Fit Model to Data and remove outliers

# +
# Fit the data with a linear model
model = linregress(df['t'],df['f'])

x_fit = df['t']
f_fit = model.slope*x_fit + model.intercept

residual_f = df['f'] - f_fit

residual_mean = np.mean(residual_f)
residual_sd = np.std(residual_f)

residual_distance = (residual_f-residual_mean)/residual_sd



# +
filter = residual_distance < max_variance

df_filtered = df[filter]

# +
# Plot the data

fig, ax = plt.subplots(2,1)

df.plot.scatter('t','f', ax=ax[0], color=(.4,.4,.4,.3))
df_filtered.plot.scatter('t','f', ax=ax[0])
ax[0].plot(x_fit, f_fit)
ax[0].set_title('Data')
ax[0].set_xlabel('x')

ax[1].plot(x_fit[filter], residual_f[filter],'b.')
ax[1].plot(x_fit[np.invert(filter)], residual_f[np.invert(filter)],'r.')
ax[1].set_title('Residual')
ax[1].set_xlabel('x')
ax[1].set_ylabel('Residual')

plt.tight_layout()
# -

# ## Save data to file

df_filtered.to_csv(output_file)
