import matplotlib.pyplot as plt
import polars as pl
import seaborn as sns

from calculator_engine import CompoundingFun


def compound():

    print("Welcome to the compound interest calculator")
    print("=" * 100)
    print(
        """
        When you run your function, you’re calculating the compounding interest based on a certain time period.
    """
    )
    print("=" * 100)
    print("please enter the values below")
    principle_ammount = float(input("Inital ammout (principle): "))
    compound = float(input("interest_rate (decimal): "))
    time_period = int(input("time period: "))

    print("=" * 100)

    analyser = CompoundingFun(principle_ammount, compound, time_period)
    report = analyser.generate_report()
    print(report)

    isVisualise = input("do you want to visualise this? (y/n):").lower().startswith("y")

    if isVisualise:
        plt.figure(figsize=(10, 6))

        sns.lineplot(data=report, x="Year", y="Value", marker="o", label="Value")
        #  sns.lineplot(data=report, x='Year', y='Gain', marker='o', label='Gain')

        plt.title(f"Value and Gain over {time_period} Years")
        plt.xlabel("Year")
        plt.ylabel("value")
        plt.grid(True)
        plt.legend()
        plt.show()
    else:
        print("No visualisation.")


if __name__ == "__main__":
    compound()
