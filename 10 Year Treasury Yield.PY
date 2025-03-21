import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Data Collection
def get_treasury_data():
    """
    Fetches historical 10-Year Treasury Yield data from Yahoo Finance.
    """
    treasury_data = yf.download("^TNX", start="2020-01-01", end="2025-03-12", interval="1d")
    treasury_data = treasury_data[['Close']].dropna()
    treasury_data.rename(columns={'Close': 'Yield'}, inplace=True)
    return treasury_data

# Step 2: Basic Analysis
def analyze_data(data):
    """
    Performs basic analysis by calculating daily changes, rolling averages, and rolling standard deviations.
    """
    data['Daily Change'] = data['Yield'].diff()
    data['Rolling Average'] = data['Yield'].rolling(window=30).mean()
    data['Rolling Std Dev'] = data['Yield'].rolling(window=30).std()
    return data

# Step 3: Summary Statistics
def calculate_statistics(data):
    """
    Calculates summary statistics for the 10-Year Treasury Yield data.
    """
    stats = {
        "Mean Yield": float(data['Yield'].mean()),
        "Median Yield": float(data['Yield'].median()),
        "Standard Deviation of Yield": float(data['Yield'].std()),
        "Max Yield": float(data['Yield'].max()),
        "Min Yield": float(data['Yield'].min()),
        "Mean Daily Change": float(data['Daily Change'].mean()),
        "Standard Deviation of Daily Change": float(data['Daily Change'].std())
    }
    return stats

# Step 4: Visualization
def plot_yield(data):
    """
    Plots the 10-Year Treasury Yield along with its 30-day rolling average.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Yield'], label='10-Year Treasury Yield (%)', color='blue')  # No *100
    plt.plot(data.index, data['Rolling Average'], label='30-Day Rolling Average (%)', color='orange', linestyle='--')  # No *100
    plt.title("10-Year Treasury Yield Analysis")
    plt.xlabel("Date")
    plt.ylabel("Yield (%)")
    plt.legend()
    plt.grid()
    plt.show()

def plot_daily_change(data):
    """
    Plots the daily changes in the 10-Year Treasury Yield.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Daily Change'], label='Daily Change (%)', color='green')  # No *100
    plt.title("Daily Changes in 10-Year Treasury Yield")
    plt.xlabel("Date")
    plt.ylabel("Change (%)")
    plt.axhline(0, color='red', linestyle='--', linewidth=1)
    plt.legend()
    plt.grid()
    plt.show()

def plot_rolling_std(data):
    """
    Plots the rolling standard deviation of the 10-Year Treasury Yield.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Rolling Std Dev'], label='30-Day Rolling Std Dev (%)', color='purple')  # No *100
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
        if "Yield" in key or "Change" in key:  
            print(f"{key}: {value:.2f}%")  # Display as-is without multiplying by 100
        else:
            print(f"{key}: {value:.2f}")
    
    # Plot results
    plot_yield(treasury_data)
    plot_daily_change(treasury_data)
    plot_rolling_std(treasury_data)
