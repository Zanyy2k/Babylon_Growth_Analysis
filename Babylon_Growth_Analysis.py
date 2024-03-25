import streamlit as st
import json

st.write("# Welcome to Babyon Tokenomics ! 👋")

# initial supply of bbn
st.write("#### Initial Supply")
initial_supply_bbn = st.number_input(
    "Please Enter the Initial Supply of BBN (B) : ", value=21
)
st.write("Initial Supply of BBN : ", f"{initial_supply_bbn} B")

# input yearly emissions
st.write("#### Yearly Emissions")
with st.expander("Yearly Emissions"):
    # yearly emissions cap for validator incentives
    pct_yearly_emission_validator_incentives_cap = float(
        st.text_input(
            "Please Enter the yearly emission cap for Validator Incentives (%) : ",
            value=2.0,
        )
    )
    # st.sidebar.write("Pct of Validator Incentives Cap : ", f'{pct_yearly_emission_validator_incentives_cap}%')

    # yearly emissions cap for community treasury
    pct_yearly_emission_community_treasury_cap = float(
        st.text_input(
            "Please Enter the yearly emission cap for Community Treasury (%) : ",
            value=2.0,
        )
    )
    # st.sidebar.write("Pct of Community Treasury Cap : ", f'{pct_yearly_emission_community_treasury_cap}%')

    # total yearly emissions cap
    pct_yearly_emission_cap = (
        pct_yearly_emission_validator_incentives_cap
        + pct_yearly_emission_community_treasury_cap
    )
    st.markdown(
        f"Total Pct of yearly emission cap for the first decade : **{pct_yearly_emission_cap} %**"
    )

# number of validators
st.write("#### Validators")
num_validators = st.number_input(
    "Please Enter the Number of Validators : ", min_value=1, value=100, step=1
)
st.write("Number of Validators : ", num_validators)

# operational cost per year per validator
st.write("#### Operation Cost")
operational_cost = st.number_input(
    "Please Enter the operational cost per Year per Validator ($) : ",
    min_value=0.0,
    value=100000.0,
    step=1000.0,
)
st.write("Operational Cost : $", operational_cost)

# minimum percentage of supply staked
st.write("#### Staking Parameters")
pct_min_supply_staked = float(
    st.text_input(
        "Please Enter the Minimum Percentage of Supply Staked (%) : ", value=35.0
    )
)
st.write("Pct of min Supply Staked : ", f"{pct_min_supply_staked}%")

# ### pass the user input value into state_variables file
user_input_dict = {
    "initial_supply_bbn": initial_supply_bbn,
    "pct_yearly_emission_cap": pct_yearly_emission_cap,
    "num_validators": num_validators,
    "operational_cost": operational_cost,
    "pct_min_supply_staked": pct_min_supply_staked,
}

# write user_input_dict to JSON file
with open("config.json", "w") as json_file:
    json.dump(user_input_dict, json_file)

st.write("#### Incentive Policy (Mandatory)")
incentive_policy_option = st.selectbox(
    "Which Incentive Policy Scenario would you like to Simulate?",
    (
        "No Rewards",
        "Maintain APY",
        "Maintain APY & Price",
        "Maintain APY & Price with Tokens",
    ),
    index=None,
    placeholder="Select Incentive Policy...",
)

st.write("You selected:", incentive_policy_option)


st.markdown("***")
if st.button("RUN SIMULATION"):
    if incentive_policy_option == "No Rewards":
        st.switch_page("pages/No_Rewards_Policy.py")
    elif incentive_policy_option == "Maintain APY":
        st.switch_page("pages/Maintain_APY_Policy.py")
