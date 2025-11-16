# generate_pi_50mb.py
import mpmath as mp

# how many digits you want after "3."
DIGITS = 50 * 1024 * 1024   # ~52,428,800

mp.mp.dps = DIGITS + 20

print("Computing π… this may take a bit…")
pi_str = str(mp.pi)

int_part, frac = pi_str.split(".")

with open("pi_50mb.txt", "w") as f:
    f.write(int_part + ".")  # "3."
    chunk = 1_000_000
    for i in range(0, DIGITS, chunk):
        f.write(frac[i:i+chunk])

print("Done")