"""Operations on sampled signals."""

from collections.abc import Sequence


def scale_signal(values: Sequence[float], factor: float = 1.0) -> list[float]:
    """Scale each sample without changing the input sequence.

    Parameters
    ----------
    values
        Samples to scale.
    factor
        Multiplicative scale factor.

    Returns
    -------
    list[float]
        A new list containing the scaled samples.
    """
    return [value * factor for value in values]
