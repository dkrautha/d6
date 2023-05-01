import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from scipy import stats

data = pd.read_csv("rpidata1.csv")

times = pd.to_datetime(data["Date / Time"], format="%Y-%m-%d %H:%M:%S.%f")
x = data["CPU Usage %"]
y = data["Temperature C"]

EARLY_TIME_CUTOFF = 209
MY_DATE_FORMATTER = mdates.DateFormatter("%H:%M")

# Time series for earlier times
plt.plot_date(
    times[:EARLY_TIME_CUTOFF],
    y[:EARLY_TIME_CUTOFF],
    "r",
    lw=2,
    label="Temperature C",
)
plt.plot_date(
    times[:EARLY_TIME_CUTOFF],
    x[:EARLY_TIME_CUTOFF],
    "b",
    lw=2,
    label="CPU Usage %",
)
plt.xlabel("Time")
plt.legend(loc="lower center")
plt.gca().xaxis.set_major_formatter(MY_DATE_FORMATTER)
plt.setp(
    plt.gca().xaxis.get_majorticklabels(),
    "rotation",
    90,
)
plt.title("Timeseries of CPU Usage and Temperature 2023-03-28 (2pm ish)")
plt.savefig("timeseries_early.png")


# Time series for later times
plt.figure()
plt.plot_date(
    times[EARLY_TIME_CUTOFF:],
    y[EARLY_TIME_CUTOFF:],
    "r",
    lw=2,
    label="Temperature C",
)
plt.plot_date(
    times[EARLY_TIME_CUTOFF:],
    x[EARLY_TIME_CUTOFF:],
    "b",
    lw=2,
    label="CPU Usage %",
)
plt.xlabel("Time")
plt.legend(loc="lower center")
plt.title("Iotu 2017-04-28")
plt.gca().xaxis.set_major_formatter(MY_DATE_FORMATTER)
plt.setp(
    plt.gca().xaxis.get_majorticklabels(),
    "rotation",
    90,
)
plt.title("Timeseries of CPU Usage and Temperature 2023-03-28 (6pm ish)")
plt.savefig("timeseries_late.png")

# Histogram of CPU usage
plt.figure()
num_bins = 35
n, bins, patches = plt.hist(x, num_bins, density=1, facecolor="blue", alpha=0.5)
plt.xlabel("CPU Usage %")
plt.ylabel("Probability")
plt.title("Histogram of CPU Usage")
plt.savefig("histogram_of_cpu_usage.png")

# Histogram of temperature
plt.figure()
num_bins = 30
n, bins, patches = plt.hist(y, num_bins, density=1, facecolor="red", alpha=0.5)
plt.xlabel("Temperature C")
plt.ylabel("Probability")
plt.title("Histogram of Temperature")
plt.savefig("histogram_of_temperature.png")

# Horizontal box plot of CPU usage
plt.figure()
plt.boxplot(x, 0, "+", 0)
plt.xlabel("CPU Usage %")
plt.title("Horizontal Box Plot of CPU Usage")
plt.savefig("boxplot_of_cpu_usage.png")

# Vertical box plot of temperature
plt.figure()
plt.boxplot(y, 0, "+")
plt.ylabel("Temperature C")
plt.title("Vertical Box Plot of Temperature")
plt.savefig("boxplot_of_temperature.png")

# Scatter diagram with a linear regression line
plt.figure()
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
plt.xlabel("CPU Usage %")
plt.ylabel("Temperature C")
plt.plot(x, y, "bo")
l = [slope * i + intercept for i in x]
plt.plot(x, l, "r", lw=2)
plt.title("Scatter Plot of CPU Usage and Temperature")
plt.savefig("scatter_of_cpu_usage_and_temperature.png")

plt.show()
