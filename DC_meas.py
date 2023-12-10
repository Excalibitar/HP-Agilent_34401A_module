from Agilent_DMM_module import Agilent34401A  # Make sure this matches the new name of your module file

def main():
    # Replace 'GPIB0::25::INSTR' with your DMM's GPIB address
    dmm_address = 'GPIB0::25::INSTR'
    
    # Create an instance of the Agilent34401A class
    dmm = Agilent34401A(dmm_address)

    try:
        # Take a DC voltage measurement
        voltage_dc = dmm.measure_voltage_dc()
        print(f"Measured DC Voltage: {voltage_dc} V")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Always close the connection to the DMM
        dmm.close()

if __name__ == "__main__":
    main()
