# abcd
Repo to demo GenAI

## Installation

Clone the repository and install in editable mode:

```bash
git clone <repo-url>
cd abcd
pip install -e .
```

Or install directly from the repository URL:

```bash
pip install git+<repo-url>
```

## Usage

```python
from abcd.dataquery import read_sgi2023_glaciers
from abcd.plot import plot_glaciers

gdf = read_sgi2023_glaciers(name_filter="Birch")
plot_glaciers(gdf)
```
