import agilent34401a

def main():
    dmm_address = 'GPIB0::25::INSTR'
    dmm = agilent34401a.Agilent34401A(dmm_address)

    try:
        voltage_dc = dmm.measure_voltage_dc(voltage_range='DEF', resolution='MIN')
        print(f"Measured DC Voltage: {voltage_dc} V")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        dmm.close()

if __name__ == "__main__":
    main()
