import streamlit as st
import copy

import experiments.visualizations as visualizations
import new_economic as new_adoption
from experiments.run import run

### Main Window

st.markdown(
    "- **No Rewards Policy** : Validators receive only the chain fees and the 2% emissions as rewards. The token economy operates without additional incentives, allowing for natural market movements with no fixed guarantee on APY."
)

simulation_1 = copy.deepcopy(new_adoption.experiment.simulations[0])

# st.write(simulation_1.model.params)

simulation_1.model.params.update(
    {"PRIVATE_CHAINS_CNT": [0], "PUBLIC_CHAINS_CNT": [0], "slashing_fraction": [0]}
)

df_1, _exceptions = run(simulation_1)

# plot the no of public chains per subset
fig1 = visualizations.plot_number_of_public_chains_per_subset(
    df_1, scenario_names={0: "Low Adoption", 1: "Medium Adoption", 2: "High Adoption"}
)

st.plotly_chart(fig1)

# plot yields per subset subplots
fig2 = visualizations.plot_yields_per_subset_subplots(
    df_1, scenario_names={0: "Low Adoption", 1: "Medium Adoption", 2: "High Adoption"}
)

st.plotly_chart(fig2)

# plot the treasury balance barplot
fig3 = visualizations.plot_treasury_balance_barplot(
    df_1,
)

st.plotly_chart(fig3)
