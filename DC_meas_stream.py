from Agilent_DMM_module import Agilent34401A
import time

def main():
    dmm_address = 'GPIB0::25::INSTR'  # Replace with your DMM's GPIB address
    dmm = Agilent34401A(dmm_address)

    try:
        # Define a callback function for processing streamed measurements
        def process_measurement(measurement):
            nonlocal start_time
            elapsed_time = time.time() - start_time
            print(f"Time: {elapsed_time:.2f} s, Measured DC Voltage: {measurement} V")

            # Stop streaming if voltage exceeds 8 VDC or 10 seconds have elapsed
            if measurement > 8 or elapsed_time >= 10:
                dmm.stop_streaming()

        # Start streaming DC voltage measurements
        start_time = time.time()  # Record the start time
        dmm.start_streaming("CONF:VOLT:DC DEF, MAX", stream_interval=0.5, callback=process_measurement)

        # Wait for the streaming to stop
        while dmm._streaming:
            time.sleep(0.1)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Always close the connection to the DMM
        dmm.close()

if __name__ == "__main__":
    main()
