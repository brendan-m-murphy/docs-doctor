"""Model runner implementations."""

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class FixedOuRun:
    """Result of the fixed-OU cached-amplitude runner.

    Attributes:
        tau_hours: Fixed correlation timescale in hours.
        site_amplitudes: Inferred site amplitudes.
        sampler_steps: Ordered sampler step names.
        cached_state_updates: Whether state updates reuse cached values.
        state_draws: Values produced by the state step.
    """

    tau_hours: float
    site_amplitudes: tuple[float, ...]
    sampler_steps: tuple[str, str]
    cached_state_updates: bool
    state_draws: tuple[float, ...]


def run_fixed_ou_cached(tau_hours: float) -> FixedOuRun:
    """Run the production fixed-OU cached-amplitude recipe.

    Args:
        tau_hours: Fixed positive correlation timescale in hours.

    Returns:
        Run details for inferred site amplitudes and cached updates.

    Raises:
        ValueError: If ``tau_hours`` is not finite and positive.
    """
    if not math.isfinite(tau_hours) or tau_hours <= 0:
        raise ValueError("tau_hours must be finite and positive")
    site_amplitude = math.sqrt(tau_hours)
    accepted_state_cache = {"site_amplitude": site_amplitude}
    state_draws = tuple(
        accepted_state_cache["site_amplitude"] * math.exp(-step / tau_hours) for step in range(3)
    )
    return FixedOuRun(
        tau_hours=tau_hours,
        site_amplitudes=(site_amplitude,),
        sampler_steps=("site_amplitude", "state"),
        cached_state_updates=True,
        state_draws=state_draws,
    )
