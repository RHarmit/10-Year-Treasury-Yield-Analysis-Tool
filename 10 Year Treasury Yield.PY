import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Data Collection
def get_treasury_data():
    # Download 10-Year Treasury Yield data
    treasury_data = yf.download("^TNX", start="2000-01-01", end="2024-01-01", interval="1d")
    treasury_data = treasury_data[['Close']].dropna()
    treasury_data.rename(columns={'Close': 'Yield'}, inplace=True)
    return treasury_data

# Step 2: Basic Analysis
def analyze_data(data):
    data['Daily Change'] = data['Yield'].diff()
    data['Rolling Average'] = data['Yield'].rolling(window=30).mean()
    data['Rolling Std Dev'] = data['Yield'].rolling(window=30).std()
    return data

# Step 3: Summary Statistics
def calculate_statistics(data):
    stats = {
        "Mean Yield": data['Yield'].mean(),
        "Median Yield": data['Yield'].median(),
        "Standard Deviation of Yield": data['Yield'].std(),
        "Max Yield": data['Yield'].max(),
        "Min Yield": data['Yield'].min(),
        "Mean Daily Change": data['Daily Change'].mean(),
        "Standard Deviation of Daily Change": data['Daily Change'].std()
    }
    return stats

# Step 4: Visualization
def plot_yield(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Yield'], label='10-Year Treasury Yield', color='blue')
    plt.plot(data['Rolling Average'], label='30-Day Rolling Average', color='orange', linestyle='--')
    plt.title("10-Year Treasury Yield Analysis")
    plt.xlabel("Date")
    plt.ylabel("Yield (%)")
    plt.legend()
    plt.grid()
    plt.show()

def plot_daily_change(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Daily Change'], label='Daily Change', color='green')
    plt.title("Daily Changes in 10-Year Treasury Yield")
    plt.xlabel("Date")
    plt.ylabel("Change (%)")
    plt.axhline(0, color='red', linestyle='--', linewidth=1)
    plt.legend()
    plt.grid()
    plt.show()

def plot_rolling_std(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Rolling Std Dev'], label='30-Day Rolling Std Dev', color='purple')
    plt.title("Rolling Standard Deviation of 10-Year Treasury Yield")
    plt.xlabel("Date")
    plt.ylabel("Std Dev (%)")
    plt.legend()
    plt.grid()
    plt.show()

# Main Execution
if __name__ == "__main__":
    # Load data
    treasury_data = get_treasury_data()
    
    # Perform analysis
    treasury_data = analyze_data(treasury_data)
    
    # Calculate and display statistics
    stats = calculate_statistics(treasury_data)
    print("Summary Statistics for 10-Year Treasury Yield:")
    for key, value in stats.items():
        print(f"{key}: {value:.2f}")
    
    # Plot results
    plot_yield(treasury_data)
    plot_daily_change(treasury_data)
    plot_rolling_std(treasury_data)
