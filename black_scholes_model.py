from calculator_engine import options_calculator


def black():
    print("Welcome to the Black Scholes price calculator")
    print("=" * 100)
    print(
        """
        When you run your function, you’re calculating the fair value of a European option (call or put) under the Black–Scholes assumptions.
	•	Call price → how much the option should cost today to have the right to buy the stock at strike price K at expiry.
	•	Put price → how much the option should cost today to have the right to sell the stock at strike price K at expiry.
    """
    )
    print("=" * 100)
    print("please enter the values below")
    share_price = float(input("share price: "))
    exercise_price = float(input("exercise price: "))
    risk_free_rate = float(input("risk free rate: "))
    time_to_expiration = float(input("expiration in days(days/360 or years): "))
    standard_deviation_of_anualised_returns = float(
        input("standard deviation of anualised returns: ")
    )
    isTrue = input("time in days? y/n: ")

    call_price, put_price, d1, d2, T = options_calculator(
        share_price,
        exercise_price,
        time_to_expiration,
        risk_free_rate,
        standard_deviation_of_anualised_returns,
        in_days=isTrue,
    )
    print(f"Call price: {call_price:.4f}")
    print(f"Put price:  {put_price:.4f}")
    print(f"d1: {d1:.4f}, d2: {d2:.4f}, T (years): {T:.4f}")


if __name__ == "__main__":
    back()
