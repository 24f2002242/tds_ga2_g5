
import matplotlib.pyplot as plt

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
retention_rates = [68.92, 70.82, 74.73, 77.49]
average_retention = sum(retention_rates) / len(retention_rates)
industry_target = 85

# Plot 1: Quarterly Retention Rate Trend
plt.figure(figsize=(10, 6))
plt.plot(quarters, retention_rates, marker='o', linestyle='-', color='b')
plt.title('2024 Quarterly Customer Retention Rate')
plt.xlabel('Quarter')
plt.ylabel('Retention Rate (%)')
plt.grid(True)
plt.ylim(60, 90)
plt.savefig('retention_trend.png')
plt.close()

# Plot 2: Average Retention Rate vs. Industry Target
plt.figure(figsize=(8, 6))
plt.bar(['Average Retention', 'Industry Target'], [average_retention, industry_target], color=['skyblue', 'lightgreen'])
plt.title('Average Retention Rate vs. Industry Target')
plt.ylabel('Retention Rate (%)')
plt.ylim(0, 100)
for i, v in enumerate([average_retention, industry_target]):
    plt.text(i, v + 1, f"{v}%", ha='center')
plt.savefig('retention_comparison.png')
plt.close()

print("Plots generated successfully: 'retention_trend.png' and 'retention_comparison.png'")
