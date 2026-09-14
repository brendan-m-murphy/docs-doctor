class Measurement:
    def convert(self, value: float, factor: float) -> float:
        """Scale a measurement.

        Args:
            value: Measurement value.

        Returns:
            The converted value.
        """
        return value * factor

    def reset(self) -> None:
        pass


def measurement_name() -> str:
    return "measurement"
