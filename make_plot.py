# This script was produced by glue and can be used to further customize a
# particular plot.

### Package imports

from glue.core.state import load
from matplotlib.patches import Patch
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('Agg')
# matplotlib.use('qt5Agg')

### Set up data

data_collection = load('make_plot.py.data')

### Set up viewer

# Initialize figure
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, aspect='auto', projection=None)

# for the legend
legend_handles = []
legend_labels = []
legend_handler_dict = dict()

### Set up layers

## Layer 1: Customer_ID

layer_data = data_collection[1]

# Get main data values
x = layer_data['Income (USD/Month)']

# Set up histogram bins
hist_n_bin = 15
hist_x_min = np.nanmin(x)
hist_x_max = np.nanmax(x)

x = x[(x >= hist_x_min) & (x <= hist_x_max)]

ax.hist(x, alpha=0.8, color='#595959', zorder=2, edgecolor='none', range=[hist_x_min, hist_x_max], bins=hist_n_bin)

handle = Patch(facecolor='#595959', edgecolor='none', alpha=0.8)  # for legend
legend_handles.append(handle)
legend_labels.append(layer_data.label)
## Layer 2: Subset 4

layer_data = data_collection[1].subsets[0]

# Get main data values
x = layer_data['Income (USD/Month)']

# Set up histogram bins
hist_n_bin = 15
hist_x_min = np.nanmin(x)
hist_x_max = np.nanmax(x)

x = x[(x >= hist_x_min) & (x <= hist_x_max)]

ax.hist(x, alpha=0.5, color='#8c510a', zorder=3, edgecolor='none', range=[hist_x_min, hist_x_max], bins=hist_n_bin)

handle = Patch(facecolor='#8c510a', edgecolor='none', alpha=0.5)  # for legend
legend_handles.append(handle)
legend_labels.append(layer_data.label)
## Layer 3: Subset 5

layer_data = data_collection[1].subsets[1]

# Get main data values
x = layer_data['Income (USD/Month)']

# Set up histogram bins
hist_n_bin = 15
hist_x_min = np.nanmin(x)
hist_x_max = np.nanmax(x)

x = x[(x >= hist_x_min) & (x <= hist_x_max)]

ax.hist(x, alpha=0.5, color='#ff7f00', zorder=4, edgecolor='none', range=[hist_x_min, hist_x_max], bins=hist_n_bin)

handle = Patch(facecolor='#ff7f00', edgecolor='none', alpha=0.5)  # for legend
legend_handles.append(handle)
legend_labels.append(layer_data.label)

### Legend

ax.legend(legend_handles, legend_labels,
    handler_map=legend_handler_dict,
    loc='best',            # location
    framealpha=0.59,      # opacity of the frame
    title='',             # title of the legend
    title_fontsize=10,   # fontsize of the title
    fontsize=10,          # fontsize of the labels
    facecolor='#FFFFFF',
    edgecolor=(0.0, 0.0, 0.0, 0.5858585858585859)
)

### Finalize viewer

# Set limits
ax.set_xlim(left=2007, right=34996)
ax.set_ylim(bottom=0.0, top=5244.0)


# Set scale (log or linear)
ax.set_xscale('linear')
ax.set_yscale('linear')


# Set axis label properties
ax.set_xlabel('Income (USD/Month)', weight='normal', size=10)
ax.set_ylabel('Profit', weight='normal', size=10)

# Set tick label properties
ax.tick_params('x', labelsize=8)
ax.tick_params('y', labelsize=8)

# For manual edition of the plot
#  - Uncomment the next code line (plt.show)
#  - Also change the matplotlib backend to qt5Agg
#  - And comment the "plt.close" line
# plt.show()

# Save figure
fig.savefig('glue_plot.png')
plt.close(fig)