# bmi

A single-file command-line script that calculates body mass index. It asks
for height in feet and inches and weight in pounds, converts them to meters
and kilograms, prints the BMI to two decimal places, and prints one of five
weight categories (under 18.5, 18.5 to 25, 25 to 30, 30 to 35, 35 and up).

## Run

Requires Python 3 only, no third-party packages.

```sh
python3 bmiIndex.py
```

Example session:

```
Want to calculate your Body Mass Index (BMI)?
Enter your height (feet): 5
Enter your height (inches): 10
Enter your weight in pounds (lbs): 160
Your BMI is: 22.96
You are normal weight.
```

Non-numeric input raises a `ValueError`; there is no input validation.

## Layout

- `bmiIndex.py` - the whole program
