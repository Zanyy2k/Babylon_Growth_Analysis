import streamlit as st
import time

# import copy
# import plotly.graph_objects as go

# import experiments.visualizations as visualizations
# import new_economic as new_adoption
# from experiments.run import run

start_time = time.time()
### Main Window
st.write("#### Maintain APY Policy")
st.markdown(
    "- **Maintain APY Policy**: To keep the Annual Percentage Yield (APY) for stakers around 4%. The incentives are adjusted to maintain the current stakers' APY at approximately 4%. There is no provision to attract new stakers unless the APY is increased above this threshold."
)


if st.button("Back Home"):
    st.switch_page("Babylon_Growth_Analysis.py")

elapsed_time = time.time() - start_time  # Calculate the elapsed time
st.success(f"Process completed in {elapsed_time:.2f} seconds")
