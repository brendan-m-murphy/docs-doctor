"""Provide a valid Google-style docstring fixture."""


class Measurement:
    """Represent a measurement in a stated unit."""

    def convert(self, factor: float) -> float:
        """Scale the measurement by a conversion factor.

        Args:
            factor: Multiplicative conversion factor.

        Returns:
            The converted value.
        """
        return factor
