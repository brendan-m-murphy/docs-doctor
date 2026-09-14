"""Tests for the built-in fixed-OU runner."""

import math
import unittest

from example_model import run_fixed_ou_cached


class RunnerTests(unittest.TestCase):
    """Check the public runner record and input constraint."""

    def test_run_record(self) -> None:
        """Describe the fixed-OU sampler and cache behavior."""
        result = run_fixed_ou_cached(24.0)

        self.assertEqual(result.tau_hours, 24.0)
        self.assertEqual(result.site_amplitudes, (math.sqrt(24.0),))
        self.assertEqual(result.sampler_steps, ("site_amplitude", "state"))
        self.assertIs(result.cached_state_updates, True)
        self.assertEqual(len(result.state_draws), 3)

    def test_invalid_timescale(self) -> None:
        """Reject non-positive and non-finite timescales."""
        for value in (0.0, -1.0, math.nan, math.inf):
            with self.subTest(value=value), self.assertRaises(ValueError):
                run_fixed_ou_cached(value)
