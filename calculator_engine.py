import polars as pl
from scipy.stats import norm
from math import log, sqrt, exp


class CompoundingFun:
       
    def __init__(self, principal, rate, years):
        self.principal = principal
        self.rate = rate 
        self.years = years

    def generate_report(self):
        results = []
        for year in range(self.years + 1):
            value = self.principal * (1 + self.rate) ** year
            results.append({
                'Year': year,
                'Value': value,
                'Gain': value - self.principal,
                'YoY_Growth': 0 if year == 0 else 
                    (value - self.principal * (1 + self.rate) ** (year-1))
            })

        return pl.DataFrame(results)


def options_calculator(S, K, T, r, sigma, in_days=False):

    if in_days:
        T = T / 360  
    
    # d1 and d2
    d1 = (log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    
    # Call & put prices
    call_price = S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
    put_price  = K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    return call_price, put_price, d1, d2, T

    



