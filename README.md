# HP-Agilent_34401A_module
A python module to handle communication with an Agilent/HP 34401A with pyvisa. The purpose of this module is to encapsulate the lower-level details of interacting with the DMM, allowing the user's main script to focus on the higher-level logic of their testing process.

Measurement types:
DC Voltage
AC Voltage
DC Current
AC Current
  paramaters include:
    resolution, range, stream
  

Resistance (2w)
Resistance (4w)
  paramaters include:
    resolution, range, stream
      RESistance:RANGe {<range>|MINimum|MAXimum}
      FRESistance:RANGe {<range>|MINimum|MAXimum}
      
Continuity
  parameters include:
    beep threshold
    
Diode
  parameters include:
    resolution
    
Null
  parameters include:
    null value

dBm
  parameters include:
    load resistance

Frequency
Period
  parameters include:
    gate time, range (voltage)
      FREQuency:VOLTage:RANGe {<range>|MINimum|MAXimum}
      PERiod:VOLTage:RANGe {<range>|MINimum|MAXimum}
      
Min/Max
  parameters include:
    "CALC:FUNC AVER;STAT ON" ! Select min-max and enable math
    "CALC:AVER:AVER?;MIN?;MAX?" ! Read the average, min, and max
