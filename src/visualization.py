import pandas as pd
import plotly.graph_objects as go
import os

# Load the dataset
data_path = os.path.join("data", "supply_chain_dataset.csv")
df = pd.read_csv(data_path)

# Create node labels
suppliers = df['supplier'].unique().tolist()
manufacturers = df['manufacturer'].unique().tolist()
transports = df['transport'].unique().tolist()

labels = suppliers + manufacturers + transports

# Map each label to an index
label_index = {label: i for i, label in enumerate(labels)}

# Create Sankey node sources and targets
source = []
target = []
value = []

# From supplier to manufacturer
for _, row in df.iterrows():
    source.append(label_index[row['supplier']])
    target.append(label_index[row['manufacturer']])
    value.append(row['inventory_level'])

# From manufacturer to transport
for _, row in df.iterrows():
    source.append(label_index[row['manufacturer']])
    target.append(label_index[row['transport']])
    value.append(row['inventory_level'])

# Create Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color="blue"
    ),
    link=dict(
        source=source,
        target=target,
        value=value
    ))])

fig.update_layout(title_text="Supply Chain Flow Visualization", font_size=12)

# Save the dashboard
output_path = os.path.join("outputs", "interactive_dashboard.html")
fig.write_html(output_path)
print(f"Dashboard saved to {output_path}")
