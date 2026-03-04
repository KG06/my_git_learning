import numpy as np

data = np.array([[22.5, 19.0, 31.2, 28.7, 25.1],
                 [17.3, 22.8, 30.5, 26.4, 21.9],
                 [33.1, 29.6, 18.4, 24.0, 27.8],
                 [20.2, 23.5, 31.9, 28.1, 22.6]])


# Task 1 Print the shape of data
print(np.shape(data))

print(np.mean(data, axis=1)) # mean temperature per station

# Task 2 Using a boolean mask, extract all temperature readings above 28.0°C and print them as a 1D array.

temperatures = data > 28.0

print(data[temperatures])

# Task 3 Normalize the entire data array to the range [0, 1] using the formula below and print the result rounded to 2 decimal places:

normalized = (data - data.min()) / (data.max() - data.min())

print(np.round(normalized, 2))