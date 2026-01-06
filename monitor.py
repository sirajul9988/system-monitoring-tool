import psutil
import time

def show_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")
    print("-" * 30)

def main():
    print("System Monitoring Tool (Press Ctrl+C to stop)")
    try:
        while True:
            show_stats()
            time.sleep(2)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    main()
