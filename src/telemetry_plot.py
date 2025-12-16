import matplotlib.pyplot as plt
from extractor import extract_f1_data

def plot_lap_telemetry(year, gp, driver):
    # 1. Fetch the data
    session = extract_f1_data(year, gp, 'R')
    
    # 2. Pick the fastest lap for that driver
    fastest_lap = session.laps.pick_driver(driver).pick_fastest()
    
    # 3. Get the high-speed telemetry (Speed, Throttle, Brake)
    telemetry = fastest_lap.get_telemetry()
    
    # 4. Create the "F1 TV" style multi-plot
    fig, ax = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
    
    # Speed Trace
    ax[0].plot(telemetry['Distance'], telemetry['Speed'], color='cyan')
    ax[0].set_ylabel('Speed (km/h)')
    ax[0].set_title(f'Telemetry: {driver} Fastest Lap - {gp} {year}')

    # Throttle Trace
    ax[1].plot(telemetry['Distance'], telemetry['Throttle'], color='green')
    ax[1].set_ylabel('Throttle %')

    # Brake Trace
    ax[2].plot(telemetry['Distance'], telemetry['Brake'], color='red')
    ax[2].set_ylabel('Brake %')
    ax[2].set_xlabel('Distance (meters)')

    plt.tight_layout()
    plt.savefig(f'{driver}_telemetry.png')
    print(f"Telemetry trace saved for {driver}!")
    plt.show()

if __name__ == "__main__":
    plot_lap_telemetry(2024, 'Monaco', 'LEC') # Looking at Leclerc's winning lap