
import sys
sys.path.append("project/src")

from data_generator import generate_data
from stream_simulator import stream_data

if __name__ == "__main__":
    print("Starting system...")

    generate_data()
    stream_data()

    print("System finished ✅")
