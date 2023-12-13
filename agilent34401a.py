import pyvisa
import threading
import time
 
class Agilent34401A:
 
 
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.rm = pyvisa.ResourceManager()
        self.dmm = self.rm.open_resource(self.resource_name)
        self.dmm.timeout = 50000  # Set a long timeout for the DMM
        self.dmm.write('*RST; *CLS')  # Reset the DMM and registers
 
    def _measure(self, command):
        """Internal helper to setup and fetch a measurement."""
        self.dmm.write(command)
        return self._trigger_and_fetch()  # Make sure to return the result
 
    def _stream_measurements(self, measure_command, stream_interval, callback):
        """Internal thread target for streaming measurements."""
        try:
            while self._streaming:
                measurement = self._measure(measure_command)
                if callback:
                    callback(measurement)
                time.sleep(stream_interval)
        except pyvisa.errors.VisaIOError as e:
            print(f"VISA Error: {e}")
 
    def start_streaming(self, measure_command, stream_interval=0.1, callback=None):
        """Starts streaming measurements of the specified type."""
        self._streaming = True
        self._stream_thread = threading.Thread(
            target=self._stream_measurements,
            args=(measure_command, stream_interval, callback)
        )
        self._stream_thread.start()
 
    def stop_streaming(self):
        """Stops the streaming of measurements."""
        self._streaming = False
        if self._stream_thread:
            self._stream_thread.join()
 
 
    def measure_voltage_dc(self, voltage_range='DEF', resolution='MAX'):
        """Measure DC voltage with the specified range and resolution."""
        try:
            # Configure the DMM for DC voltage measurement
            self.dmm.write(f'CONF:VOLT:DC {voltage_range}, {resolution}')
            # Use the _trigger_and_fetch method to execute the measurement and retrieve the result
            return self._trigger_and_fetch()
        except pyvisa.errors.VisaIOError as e:
            print(f"VISA Error: {e}")
            return None
        except Exception as e:
            print(f"Error in measure_voltage_dc: {e}")
            return None
 
def measure_voltage_ac(self, voltage_range='DEF', resolution='MAX'):
    """Measure AC voltage with the specified range and resolution."""
    try:
        # Configure the DMM for AC voltage measurement
        self.dmm.write(f'CONF:VOLT:AC {voltage_range}, {resolution}')
        # Use the _trigger_and_fetch method to execute the measurement and retrieve the result
        return self._trigger_and_fetch()
    except pyvisa.errors.VisaIOError as e:
        print(f"VISA Error: {e}")
        return None
    except Exception as e:
        print(f"Error in measure_voltage_ac: {e}")
        return None

 
def measure_current_dc(self, current_range='DEF', resolution='MAX'):
    """Measure DC current with the specified range and resolution."""
    try:
        # Configure the DMM for DC current measurement
        self.dmm.write(f'CONF:CURR:DC {current_range}, {resolution}')
        # Use the _trigger_and_fetch method to execute the measurement and retrieve the result
        return self._trigger_and_fetch()
    except pyvisa.errors.VisaIOError as e:
        print(f"VISA Error: {e}")
        return None
    except Exception as e:
        print(f"Error in measure_current_dc: {e}")
        return None

 
def measure_current_ac(self, current_range='DEF', resolution='MAX'):
    """Measure AC current with the specified range and resolution."""
    try:
        # Configure the DMM for AC current measurement
        self.dmm.write(f'CONF:CURR:AC {current_range}, {resolution}')
        # Use the _trigger_and_fetch method to execute the measurement and retrieve the result
        return self._trigger_and_fetch()
    except pyvisa.errors.VisaIOError as e:
        print(f"VISA Error: {e}")
        return None
    except Exception as e:
        print(f"Error in measure_current_ac: {e}")
        return None

 
    def _trigger_and_fetch(self):
        """Trigger the DMM and fetch the measurement result."""
        self.dmm.write('TRIG:SOUR BUS')
        self.dmm.write('SAMP:COUN 1')
        self.dmm.write('INIT')
        self.dmm.write('*TRG')
        self.dmm.query('*OPC?')  # Wait for the DMM to complete the measurement
        measurement_str = self.dmm.query('FETCh?')
        return float(measurement_str)
 
    def close(self):
        """Close the connection to the DMM and clean up."""
        self.dmm.close()
        self.rm.close()
