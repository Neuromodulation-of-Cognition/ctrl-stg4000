[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://en.wikipedia.org/wiki/MIT_License) [![pytest-status](https://github.com/pyreiz/ctrl-stg4000/workflows/pytest/badge.svg)](https://github.com/pyreiz/ctrl-stg4000/actions) [![Coverage Status](https://coveralls.io/repos/github/pyreiz/ctrl-stg4000/badge.svg?branch=develop)](https://coveralls.io/github/pyreiz/ctrl-stg4000?branch=develop) [![Documentation Status](https://readthedocs.org/projects/ctrl-stg4000/badge/?version=latest)](https://ctrl-stg4000.readthedocs.io/en/latest/?badge=latest)

### STG4000

This package wraps the C# dll ```McsUsbNet.dll``` for remote control of the multichannelsystem STG4002/4/8 in Python 3. The dll can be acquired from multichannelsystems directly at https://www.multichannelsystems.com/software/mcsusbnetdll or installed by script, i.e. by running ```python post_setup.py```.

The dll allows to set stimulation settings in stream or download mode. Currently, this package only supports download mode.

#### Installation

```bash
git clone https://github.com/pyreiz/app-stg4000
cd app-stg4000
pip install -e .
python -m stg.install
```
The last command downloads and unzips the most recent 64-bit dll from multichannelsystems into ```./bin```

#### Downloading a stimulation setting

```python
from stg.api import STG4000
stim = STG4000()
# download a biphasic single pulse with an amplitude of +- 1mA, a pulsewidth of 1ms and a
# interstimulusinterval of 48ms to the first channel. Channel indexing starts at 0.

stim.download(channel_index=0,
              amplitude=[1, -1, 0],
              duration=[1, 1, 48000])

# start the stimulation
stim.start_stimulation([0]) #trigger the first channel
# abort an ongoing stimulation
stim.start_stimulation()
```
#### Creating and downloading repetitive pulses
```python
# for convenience, there is also a PulseFile class implemented
from stg.api import PulseFile
p = PulseFile(intensity_in_mA=1000, #in microamps, i.e. 1000 -> 1 mA
            mode='biphasic', # can alternatively be monophasic
            pulsewidth_in_ms=1, #in milliseconds, i.e. 1 -> 1ms
            burstcount=3, # number of repetitions
            isi_in_ms=48, #in milliseconds, i.e. 48 -> 48ms
            )
amplitude, duration = p.compile()
stim.download(1, amplitude, duration)
stim.start_stimulation([1])
```
#### Triggering multiple channels

By default, the stg4002/4/8 uses a map to define which channels are to be triggered by which triggerinput. In that regard, ```stim.start_stimulation``` does actually not trigger a channel directly, but a trigger input, which is mapped to the respective channels. The triggermap is initialized during class instantiation to the identity diagonal, i.e. trigin 0 triggers channel 0, trigin 1 triggers channel 1. If you want to trigger multiple channels with a single trigin, you can use ```stim.start_stimulation([0,1])```.
