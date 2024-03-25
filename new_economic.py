"""
# Cumulative Yield Analysis
"""

from model.stochastic_processes import create_stochastic_process_realizations
import time


def generate_stochastic_processes(TIMESTEPS, DELTA_TIME):

    print("Starting of generate_stochastic_processes...")
    start_time = time.time()

    # Generate stochastic process realizations
    ## Linear
    polygn_price_samples = create_stochastic_process_realizations(
        "convex_polygn_price_samples", timesteps=TIMESTEPS, dt=DELTA_TIME
    )
    adoption_rates_slow = create_stochastic_process_realizations(
        "adoption_rates", timesteps=TIMESTEPS, dt=DELTA_TIME, final_chains_num=500
    )
    adoption_rates_med = create_stochastic_process_realizations(
        "adoption_rates", timesteps=TIMESTEPS, dt=DELTA_TIME, final_chains_num=2000
    )
    adoption_rates_fast = create_stochastic_process_realizations(
        "adoption_rates", timesteps=TIMESTEPS, dt=DELTA_TIME, final_chains_num=3500
    )
    adoption_rates_public_slow = create_stochastic_process_realizations(
        "adoption_rates", timesteps=TIMESTEPS, dt=DELTA_TIME, final_chains_num=5
    )
    adoption_rates_public_med = create_stochastic_process_realizations(
        "adoption_rates", timesteps=TIMESTEPS, dt=DELTA_TIME, final_chains_num=15
    )
    adoption_rates_public_fast = create_stochastic_process_realizations(
        "adoption_rates", timesteps=TIMESTEPS, dt=DELTA_TIME, final_chains_num=25
    )
    hardware_cost_moores_law = create_stochastic_process_realizations(
        "hardware_costs", timesteps=TIMESTEPS, dt=DELTA_TIME, init_hardware_cost=500
    )

    print("End of generate_stochastic_processes...")
    elapsed_time = time.time() - start_time
    print(f"Process completed in {elapsed_time:.2f} seconds")

    return (
        polygn_price_samples,
        adoption_rates_slow,
        adoption_rates_med,
        adoption_rates_fast,
        adoption_rates_public_slow,
        adoption_rates_public_med,
        adoption_rates_public_fast,
        hardware_cost_moores_law,
    )


def get_parameter_overrides(
    polygn_price_samples,
    adoption_rates_slow,
    adoption_rates_med,
    adoption_rates_fast,
    adoption_rates_public_slow,
    adoption_rates_public_med,
    adoption_rates_public_fast,
    hardware_cost_moores_law,
):
    parameter_overrides = {
        "polygn_price_process": [
            lambda run, timestep: polygn_price_samples[run - 1][timestep],
        ],
        "Adoption_speed_process": [
            lambda run, timestep: adoption_rates_slow[run - 1][timestep],
            lambda run, timestep: adoption_rates_med[run - 1][timestep],
            lambda run, timestep: adoption_rates_fast[run - 1][timestep],
        ],
        "Adoption_speed_public_process": [
            lambda run, timestep: adoption_rates_public_slow[run - 1][timestep],
            lambda run, timestep: adoption_rates_public_med[run - 1][timestep],
            lambda run, timestep: adoption_rates_public_fast[run - 1][timestep],
        ],
        "validator_hardware_costs_per_month_process": [
            lambda run, timestep: hardware_cost_moores_law[run - 1][timestep],
        ],
    }
    return parameter_overrides
