import streamlit as st
import time
import copy
import importlib

import model.constants as constants
import new_economic as new_adoption
from experiments.run import run
from experiments.default_experiment import experiment
import experiments.visualizations as visualizations


start_time = time.time()

### Main Window
st.write("#### No Rewards Policy")
st.markdown(
    "- **No Rewards Policy** : Validators receive only the chain fees and the 2% emissions as rewards. The token economy operates without additional incentives, allowing for natural market movements with no fixed guarantee on APY."
)

with st.spinner(text="In progress..."):

    DELTA_TIME = constants.epochs_per_week  # epochs per timestep
    SIMULATION_TIME_DAYS = 5 * 365  # number of months
    TIMESTEPS = constants.epochs_per_day * SIMULATION_TIME_DAYS // DELTA_TIME

    # generate stochastic processes
    (
        polygn_price_samples,
        adoption_rates_slow,
        adoption_rates_med,
        adoption_rates_fast,
        adoption_rates_public_slow,
        adoption_rates_public_med,
        adoption_rates_public_fast,
        hardware_cost_moores_law,
    ) = new_adoption.generate_stochastic_processes(TIMESTEPS, DELTA_TIME)

    # get parameter overrides
    parameter_overrides = new_adoption.get_parameter_overrides(
        polygn_price_samples,
        adoption_rates_slow,
        adoption_rates_med,
        adoption_rates_fast,
        adoption_rates_public_slow,
        adoption_rates_public_med,
        adoption_rates_public_fast,
        hardware_cost_moores_law,
    )

    # Make a copy of the default experiment to avoid mutation
    no_reward_experiment = copy.deepcopy(experiment)

    # store this experiemnt simulation as no_rewards_simulation
    no_rewards_simulation = no_reward_experiment.simulations[0]
    print("no_rewards_simulation : ", no_rewards_simulation)

    # override default experiment Simulation and System Parameters related to timing
    no_rewards_simulation.timesteps = TIMESTEPS
    print("TIMESTEPS : ", TIMESTEPS)
    no_rewards_simulation.model.params.update({"dt": [DELTA_TIME]})

    # override default experiment System Parameters
    no_rewards_simulation.model.params.update(parameter_overrides)

    no_rewards_simulation.model.params.update(
        {"PRIVATE_CHAINS_CNT": [0], "PUBLIC_CHAINS_CNT": [0], "slashing_fraction": [0]}
    )

    df_1, _exceptions = run(no_rewards_simulation)

    # plot the no of public chains per subset
    fig1 = visualizations.plot_number_of_public_chains_per_subset(
        df_1,
        scenario_names={0: "Low Adoption", 1: "Medium Adoption", 2: "High Adoption"},
    )

    st.plotly_chart(fig1)

    # plot yields per subset subplots
    fig2 = visualizations.plot_yields_per_subset_subplots(
        df_1,
        scenario_names={0: "Low Adoption", 1: "Medium Adoption", 2: "High Adoption"},
    )

    st.plotly_chart(fig2)

    # plot the treasury balance barplot
    fig3 = visualizations.plot_treasury_balance_barplot(
        df_1,
    )

    st.plotly_chart(fig3)

if st.button("Back Home"):
    st.switch_page("Babylon_Growth_Analysis.py")

elapsed_time = time.time() - start_time
st.success(f"Process completed in {elapsed_time:.2f} seconds")
