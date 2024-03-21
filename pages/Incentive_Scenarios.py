import streamlit as st
import copy
import plotly.graph_objects as go

import experiments.visualizations as visualizations
import new_economic as new_adoption
from experiments.run import run

### Main Window

st.markdown("### Incentivization Scenarios")
# The potential incentivization scenarios for BBN's validator rewards:
# 1. **No Rewards Policy**: Validators receive only the chain fees and the 2% emissions as rewards. The token economy operates without additional incentives, allowing for natural market movements with no fixed guarantee on APY.
# 2. **Maintain APY Policy**: To keep the Annual Percentage Yield (APY) for stakers around 4%. The incentives are adjusted to maintain the current stakers' APY at approximately 4%. There is no provision to attract new stakers unless the APY is increased above this threshold.
# 3. **Maintain APY and Price Policy**: To preserve a ~4% APY for stakers while keeping the token price stable. The BBN treasury manages the reward distribution to balance the APY at its initial value, assuming the sales of tokens are onset by an influx of new stakers. Assumes that rewards are distributed entirely in stablecoins.
# 4. **Maintain APY and Price Policy with Tokens**: Ensuring a ~4% APY for stakers with a stable token price, but compensating in BBN tokens. This introduces a selling pressure, as tokens are transferred from the treasury to the open market.

no_rewards_tab, maintain_apy_policy_tab, maintain_apy_price_policy_tab, maintain_apy_price_policy_tokens_tab = st.tabs(["No Rewards Policy", "Maintain APY Policy", "Maintain APY and Price Policy", "Maintain APY and Price Policy with Tokens"])

with no_rewards_tab:
   st.markdown("- **No Rewards Policy** : Validators receive only the chain fees and the 2% emissions as rewards. The token economy operates without additional incentives, allowing for natural market movements with no fixed guarantee on APY.")
   
   simulation_1 = copy.deepcopy(new_adoption.experiment.simulations[0])

   # st.write(simulation_1.model.params)

   simulation_1.model.params.update({"PRIVATE_CHAINS_CNT": [0], "PUBLIC_CHAINS_CNT": [0], 'slashing_fraction': [0]})

   df_1, _exceptions = run(simulation_1)

   # plot the no of public chains per subset
   fig1 = visualizations.plot_number_of_public_chains_per_subset(df_1, scenario_names={
    0: "Low Adoption",
    1: "Medium Adoption",
    2: "High Adoption"})
   
   st.plotly_chart(fig1)
   
   # plot yields per subset subplots
   fig2 = visualizations.plot_yields_per_subset_subplots(df_1, scenario_names={
    0: "Low Adoption",
    1: "Medium Adoption",
    2: "High Adoption"})
   
   st.plotly_chart(fig2)
   
   # plot the treasury balance barplot
   fig3 = visualizations.plot_treasury_balance_barplot(
       df_1,
   )
   
   st.plotly_chart(fig3)



# with maintain_apy_policy_tab:
#    st.markdown("- **Maintain APY Policy** : To keep the Annual Percentage Yield (APY) for stakers around 4%. The incentives are adjusted to maintain the current stakers' APY at approximately 4%. There is no provision to attract new stakers unless the APY is increased above this threshold.")

# with maintain_apy_price_policy_tab:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# with maintain_apy_price_policy_tokens_tab:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)