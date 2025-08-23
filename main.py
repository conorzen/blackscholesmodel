from black_scholes_model import black
from compound_interest_calculator import compound


def main():
    print("Hello from black-scholes-calculator!")
    print("please select what you would like to do")
    selectModel = input(
        "press 1 for black-scholes-calculator or 2 for compound-interest-calculator: "
    )

    if selectModel == "1":
        black()
    else:
        compound()


if __name__ == "__main__":
    main()
