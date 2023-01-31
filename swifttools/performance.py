"""Tools for measuring code performance."""

from glob import glob
import numpy as np

unit_time_Gyr = 977.8131

def extract_runtime(sim_dir):
    """Extract the run time of a simulation."""

    timesteps_glob = glob(f"{sim_dir}/timesteps_*.txt")
    timesteps_filename = timesteps_glob[0]

    # Read the relevant columns from the timesteps file
    data = np.genfromtxt(
        timesteps_filename,
        skip_footer=5,
        loose=True,
        invalid_raise=False,
        usecols=(1, 12),
        dtype=[("time", "f4"), ("wallclock", "f4")],
    )

    sim_time = data["time"] * unit_time_Gyr
    wallclock_time = np.cumsum(data["wallclock"]) / 1000 / 3600

    return wallclock_time, sim_time


                                
