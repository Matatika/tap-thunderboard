# tap-thunderboard

`tap-thunderboard` is a Singer tap for environmental measurements collected by Silicon Labs Thunderboards.

Inspired by [this example](https://github.com/siliconlabs/thundercloud) from [Silicon Labs](https://www.silabs.com/community/projects.entry.html/2017/03/08/thunderboard_sensew-Scqr)

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.


## Installation

To install this tap locally you can install directly from GitHub.

```bash
pip install git+https://github.com/Matatika/tap-thunderboard
```

## Prerequisites and Collecting data

Before using this tap to collect your measurements you will need a [Thunderboard](https://www.silabs.com/development-tools/thunderboard/thunderboard-bg22-kit)
or another way to collect a json file of measurements.

This tap would normally be used to output continuously to a file
```bash
tap-thunderboard -s >> data/capture.out
```

To run non root you need to give additional device permissions
```bash
sudo setcap cap_net_raw+e [path to your executable]/tap-thunderboard
sudo setcap cap_net_admin+eip [path to your executable]/tap-thunderboard
```

Then periodically run the tap (meltano add loader target-postgres)
```bash
meltano elt tap-thunderboard target-postgres
```


## Configuration

### Accepted Config Options

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-thunderboard --about
```

## Usage

You can easily run `tap-thunderboard` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-thunderboard --version
tap-thunderboard --help
tap-thunderboard --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_thunderboard/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-thunderboard` CLI interface directly using `poetry run`:

```bash
poetry run tap-thunderboard --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file.

To run with Meltano:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-thunderboard
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-thunderboard --version
# OR run a test `elt` pipeline:
meltano elt tap-thunderboard target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.
