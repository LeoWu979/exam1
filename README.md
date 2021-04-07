# exam1

### 1. Setup of 3 buttons : <br>
- D13 for "confirm" frequency<br>
- D12 for "select down"<br>
- D11 for "select up"<br>
### 2. Setup of DAC and ADC pin name: <br>
- D7 for DAC pin<br>
- A0 for ADC pin<br>
### 3. Some other electronic component : <br>
- uLCD : tx <-> D1, rx <-> D0, reset <-> D2.<br>
### 4. Compile "main.cpp" with mbed command.<br>
### 5. Frequency selection : <br>
- I design a menu form of frequency selection. Please focus on uLCD screen.<br>
- Four choice : 1/8, 1/4, 1/2 and 1.<br>
- "select up" will move down the selection rectangle, "select down" will move up the selection rectangle.<br>
- Push "confirm" to input frequency to system.<br>
### 6. You can use picoscope to observe waveform.<br>
### 7. Python analysis : <br>
- Compile "FFT.py" with python command : sudo python3 FFT.py<br>
- You will see two figure, the first is the waveform after RC filter, second is the frequency response of FFT.<br>
