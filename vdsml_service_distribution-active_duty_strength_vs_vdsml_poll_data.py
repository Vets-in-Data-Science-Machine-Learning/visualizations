# -*- coding: utf-8 -*-
"""
Plot 2021 Active Duty End Strengths vs. VDSML Poll Data
Author: Ted Hallum
Date: 13 OCT 2021
"""

# Import packages
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns

# Set current working directory to this script's own directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Create data
# Source for 2021 Active Duty End Strengths: https://sgp.fas.org/crs/natsec/R46810.pdf
# Source for VDSML Poll Data: https://www.linkedin.com/feed/update/urn:li:activity:6848227969299697664
# The cutoff for the poll data was 22:45 on 13 OCT 2021
columns = ['source', 'service', 'number']
army = [['2021 Active Duty End Strength', 'Army', 485900], ['VDSML Poll Data', 'Army', 38]]
navy = [['2021 Active Duty End Strength', 'Navy', 347800], ['VDSML Poll Data', 'Navy', 25]]
air_force = [['2021 Active Duty End Strength', 'Air Force', 327041], ['VDSML Poll Data', 'Air Force', 17]]
marine_corps = [['2021 Active Duty End Strength', 'Marine Corps', 181200], ['VDSML Poll Data', 'Marine Corps', 21]]
coast_guard = [['2021 Active Duty End Strength', 'Coast Guard', 44500], ['VDSML Poll Data', 'Coast Guard', 2]]
space_force = [['2021 Active Duty End Strength', 'Space Force', 6434], ['VDSML Poll Data', 'Space Force', 1]]

# Build DataFrame for 2021 Active duty data
active_duty_2021 = [army[0], navy[0], air_force[0], marine_corps[0], coast_guard[0], space_force[0]]
active_duty_2021_df = pd.DataFrame(data = active_duty_2021, columns = columns)

# Build DataFrame for VDSML poll data
vdsml_poll = [army[1], navy[1], air_force[1], marine_corps[1], coast_guard[1], space_force[1]]
vdsml_poll_df = pd.DataFrame(data = vdsml_poll, columns = columns)

# Find the total active duty personnel
active_duty_sum = active_duty_2021_df['number'].sum()

# Calculate active duty personnel percentages
active_duty_2021_df['percent'] = round(active_duty_2021_df['number'] / active_duty_sum, 2)

# Find the total VDSML members who voted
vdsml_sum = vdsml_poll_df['number'].sum()

# Calculate VDSML percentages
vdsml_poll_df['percent'] = round(vdsml_poll_df['number'] / vdsml_sum, 2)

# Create merged dataframe
dataframes = [active_duty_2021_df, vdsml_poll_df]
merged_df = pd.concat(dataframes).reset_index()

# Create plot
sns.set(style="darkgrid")
fig, ax = plt.subplots(figsize=(15,12))
ax = sns.barplot(x = "service", y = 'percent', hue = "source", orient = 'v', data = merged_df)

# Set individual bar annotations
for i, patch in enumerate(ax.patches):
    # get_width pulls left or right; get_y pushes up or down
    ax.text(x = patch.get_x() + .08,
            y = patch.get_height() + .002,
            s = f"{merged_df['number'][i]:,}",
            fontsize = 15,
            rotation = 45,
            color = 'dimgrey')

# Set various other plot attributes
ax.set_xlabel("Service Branch", fontsize = 28)
ax.set_ylabel('Percent %', fontsize = 28)
ax.set_xticklabels(ax.get_xticklabels(), size = 18)
ax.set_yticks(ax.get_yticks().round(2))
ax.set_yticklabels(ax.get_yticks().round(2), size = 18)
ax.set_title("2021 Active Duty End Strengths vs. VDSML Poll Data", fontsize = 32)
ax.legend(loc = 'best', fontsize = 15)

plt.savefig('active_duty_strength_vs_vdsml_poll_data.png')

plt.show()