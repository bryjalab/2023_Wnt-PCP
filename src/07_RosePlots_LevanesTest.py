import pandas as pd
from scipy.stats import levene

# Load the dataset
file_path = '/mnt/data/PrimII_FishID_0_180.xlsx'
data = pd.read_excel(file_path)

# Calculate the variance of angles for each FishID within each condition
fish_variances = data.groupby(['FishID', 'Condition'])['angles'].var().reset_index()

# Extract variances for the control condition
control_variances = fish_variances[fish_variances['Condition'] == 'Control']['angles']

# List of conditions to compare with control
conditions = ['Epha2', 'Phactr4', 'Rai14']

# Initialize a dictionary to store the results
levene_results_by_fish = {}

# Perform Levene's test for each condition vs control using the fish-level variances
for condition in conditions:
    condition_variances = fish_variances[fish_variances['Condition'] == condition]['angles']
    stat, p_value = levene(control_variances, condition_variances)
    levene_results_by_fish[condition] = {'statistic': stat, 'p-value': p_value}

# Display the results
levene_results_df = pd.DataFrame(levene_results_by_fish).T
print("Levene's Test Results by Fish Variance:")
print(levene_results_df)

# Calculate the number of fish (n) for each group in the Control vs Epha2 comparison using the fish-level variances
n_control_fish = fish_variances[fish_variances['Condition'] == 'Control'].shape[0]
n_epha2_fish = fish_variances[fish_variances['Condition'] == 'Epha2'].shape[0]

print(f"Number of fish in Control group: {n_control_fish}")
print(f"Number of fish in Epha2 group: {n_epha2_fish}")


# Define a function to create a rose plot for a specified column
def create_rose_plot(column_name, num_bins=36):
    angles = data[column_name].dropna()
    bin_edges = np.linspace(0, 360, num_bins + 1)
    
    # Convert angles from degrees to radians
    angles_rad = np.deg2rad(angles)
    
    # Create histogram
    counts, _ = np.histogram(angles_rad, bins=np.deg2rad(bin_edges))
    
    # Plot
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, polar=True)
    bars = ax.bar(np.deg2rad(bin_edges[:-1]), counts, width=np.deg2rad(np.diff(bin_edges)), align='edge')
    
    plt.title(f'Rose Plot for {column_name}')
    plt.show()

# Example usage: create a rose plot for the first column
create_rose_plot(data.columns[0])

