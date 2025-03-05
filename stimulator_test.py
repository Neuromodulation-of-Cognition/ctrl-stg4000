from stg.pulsefile import PulseFileAlternative

asymm_biphasic = {
    "pulse_width": 250,
    "stimulation_duration": 5.0,
    "frequency": 50,
    "intensity": 1.0,
    "phase_ratio": (1, 2),
    "first_intensity_negative": True,
    "waveform": "rectangular_assym_biphasic",
}

monoph = {
    "pulse_width": 100,
    "stimulation_duration": 5.0,
    "frequency": 20,
    "intensity": 1.0,
    "phase_ratio": (1, 2),
    "first_intensity_negative": True,
    "waveform": "monophasic",
}

symm_biphasic_error = {
    "pulse_width": 250,
    "stimulation_duration": 5.0,
    "frequency": 3,
    "intensity": 1.0,
    "phase_ratio": (1, 2),
    "first_intensity_negative": True,
    "waveform": "symm_biphasic",
}

symm_biphasic = {
    "pulsewidth": 250,
    "stimulation_duration": 5.0,
    "frequency": 3,
    "intensity": 1.0,
    "phase_ratio": None,
    "first_intensity_negative": True,
    "waveform": "symm_biphasic",
}

test_list = [asymm_biphasic, monoph, symm_biphasic_error, symm_biphasic]

for test in test_list:
    pulsefile = PulseFileAlternative(**test)

print("done")
