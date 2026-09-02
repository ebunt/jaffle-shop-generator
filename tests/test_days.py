import datetime as dt

from jafgen.simulation import Simulation
from jafgen.time import total_minutes_elapsed


def test_year_length():
    sim = Simulation(2, 0, "raw")
    assert sim.sim_days == 730


def test_total_minutes_elapsed_from_time_uses_hours_and_minutes():
    assert total_minutes_elapsed(dt.time(hour=13, minute=42, second=59)) == 822
