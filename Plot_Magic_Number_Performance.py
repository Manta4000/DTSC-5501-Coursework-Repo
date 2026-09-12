import matplotlib.pyplot as plt

# Performance data from the table above.
search_ranges = ["1–99", "1–10,000", "1–10,000,000"]
efficient_attempts = [5, 5, 18]
inefficient_attempts = [4, None, None]
efficient_times = [0.0004247, 0.0001509, 0.0005048]
inefficient_times = [0.0003628, 0.0005469, 0.0004713]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Use None for failed attempts so they are not plotted as valid values.
axes[0].plot(search_ranges, efficient_attempts, marker="o", label="Efficient")
axes[0].plot(search_ranges, inefficient_attempts, marker="o", label="Inefficient")
axes[0].set_title("Magic Number Attempts")
axes[0].set_xlabel("Search range")
axes[0].set_ylabel("Attempts")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(search_ranges, efficient_times, marker="o", label="Efficient")
axes[1].plot(search_ranges, inefficient_times, marker="o", label="Inefficient")
axes[1].set_title("Algorithm Performance")
axes[1].set_xlabel("Search range")
axes[1].set_ylabel("Execution time (seconds)")
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()