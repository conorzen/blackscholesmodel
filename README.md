# Financial Growth Plotting Project

A Python project to visualize year-over-year growth of values with a plot. This project uses `polar` and `matplotlib` for data manipulation and plotting.

It has to apps to run each one do the following:

```bash 
uv run black_scholes_model.py 

uv run compounding_interest_calculator.py

```

---

## Features

- Calculates Yearly Gain and YoY Growth
- Plots `Value` over `Year` for easy visualization
- Simple, clean, reusable code

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/conorzen/blackscholesmodel.git


uv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

uv pip install -r requirements.txt
```
## Author 

 name: conorzen
 email: conoreid@me.com


## Example output


example output for compound_interest_calculator

(compound_interest.png)


┌──────┬──────────────┬──────────────┬─────────────┐
│ Year ┆ Value        ┆ Gain         ┆ YoY_Growth  │
│ ---  ┆ ---          ┆ ---          ┆ ---         │
│ i64  ┆ f64          ┆ f64          ┆ f64         │
╞══════╪══════════════╪══════════════╪═════════════╡
│ 0    ┆ 1000.0       ┆ 0.0          ┆ 0.0         │
│ 1    ┆ 1200.0       ┆ 200.0        ┆ 200.0       │
│ 2    ┆ 1440.0       ┆ 440.0        ┆ 240.0       │
│ 3    ┆ 1728.0       ┆ 728.0        ┆ 288.0       │
│ 4    ┆ 2073.6       ┆ 1073.6       ┆ 345.6       │
│ …    ┆ …            ┆ …            ┆ …           │
│ 16   ┆ 18488.42589  ┆ 17488.42589  ┆ 3081.404315 │
│ 17   ┆ 22186.111067 ┆ 21186.111067 ┆ 3697.685178 │
│ 18   ┆ 26623.333281 ┆ 25623.333281 ┆ 4437.222213 │
│ 19   ┆ 31947.999937 ┆ 30947.999937 ┆ 5324.666656 │
│ 20   ┆ 38337.599924 ┆ 37337.599924 ┆ 6389.599987 │
└──────┴──────────────┴──────────────┴─────────────┘

Thanks