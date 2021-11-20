import numpy as np

from samplics.sampling import power_for_one_proportion


def test_power_for_one_prop_two_sides_number():
    power1 = power_for_one_proportion(
        samp_size=107, prop_0=0.2, prop_1=0.1, arcsin=True, testing_type="two-side", alpha=0.05
    )
    power2 = power_for_one_proportion(
        samp_size=25, prop_0=0.3, prop_1=0.7, arcsin=True, testing_type="two-side", alpha=0.10
    )
    power3 = power_for_one_proportion(
        samp_size=500, prop_0=0.95, prop_1=0.99, arcsin=True, testing_type="two-side", alpha=0.07
    )
    power4 = power_for_one_proportion(
        samp_size=50,
        prop_0=0.0950,
        prop_1=0.1990,
        arcsin=True,
        testing_type="two-side",
        alpha=0.01,
    )
    assert np.isclose(power1, 0.8359, atol=0.001)
    assert np.isclose(power2, 0.9932, atol=0.001)
    assert np.isclose(power3, 0.9999, atol=0.001)
    assert np.isclose(power4, 0.3200, atol=0.001)


def test_power_for_one_prop_two_sides_array():
    samp_size = np.array([107, 25, 500, 50])
    prop_0 = (0.2, 0.3, 0.95, 0.0950)
    prop_1 = [0.1, 0.7, 0.99, 0.1990]
    alpha = [0.05, 0.10, 0.07, 0.01]
    power = power_for_one_proportion(
        samp_size=samp_size,
        prop_0=prop_0,
        prop_1=prop_1,
        arcsin=True,
        testing_type="two-side",
        alpha=alpha,
    )

    assert np.isclose(power[0], 0.8359, atol=0.001)
    assert np.isclose(power[1], 0.9932, atol=0.001)
    assert np.isclose(power[2], 0.9999, atol=0.001)
    assert np.isclose(power[3], 0.3200, atol=0.001)


def test_power_for_one_prop_two_sides_dict():
    samp_size = {"one": 107, "two": 25, "three": 500, "four": 50}
    prop_0 = {"one": 0.2, "two": 0.3, "three": 0.95, "four": 0.095}
    prop_1 = {"one": 0.1, "two": 0.7, "three": 0.99, "four": 0.199}
    alpha = {"one": 0.05, "two": 0.10, "three": 0.07, "four": 0.01}
    power = power_for_one_proportion(
        samp_size=samp_size,
        prop_0=prop_0,
        prop_1=prop_1,
        arcsin=True,
        testing_type="two-side",
        alpha=alpha,
    )

    assert np.isclose(power["one"], 0.8359, atol=0.001)
    assert np.isclose(power["two"], 0.9932, atol=0.001)
    assert np.isclose(power["three"], 0.9999, atol=0.001)
    assert np.isclose(power["four"], 0.3200, atol=0.001)


def test_power_for_one_prop_one_sides_number():

    samp_size = np.array([75, 55, 37, 5])
    prop_0 = (0.2, 0.37, 0.95, 0.85)
    prop_1 = [0.1, 0.47, 0.99, 0.90]
    power_less = power_for_one_proportion(
        samp_size=samp_size,
        prop_0=prop_0,
        prop_1=prop_1,
        arcsin=True,
        testing_type="less",
        alpha=0.05,
    )

    assert np.isclose(power_less[0], 0.7924, atol=0.001)
    assert np.isclose(power_less[1], 0.0008, atol=0.001)
    assert np.isclose(power_less[2], 0.0008, atol=0.001)
    assert np.isclose(power_less[3], 0.0236, atol=0.001)


def test_power_for_one_prop_one_sides_number():

    samp_size = {1: 75, 2: 55, 3: 37, 4: 5}
    prop_0 = {1: 0.2, 2: 0.37, 3: 0.95, 4: 0.85}
    prop_1 = {1: 0.1, 2: 0.47, 3: 0.99, 4: 0.90}
    power_less = power_for_one_proportion(
        samp_size=samp_size,
        prop_0=prop_0,
        prop_1=prop_1,
        arcsin=True,
        testing_type="greater",
        alpha=0.05,
    )

    assert np.isclose(power_less[1], 2.027e-5, atol=0.001)
    assert np.isclose(power_less[2], 0.4446, atol=0.001)
    assert np.isclose(power_less[3], 0.4530, atol=0.001)
    assert np.isclose(power_less[4], 0.0960, atol=0.001)