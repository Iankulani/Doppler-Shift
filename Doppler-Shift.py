# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:39:25 2025

@author: IAN CARTER KULANI

"""

SPEED_OF_LIGHT = 299792458  # Speed of light in meters per second (m/s)

def calculate_doppler_shift(velocity, transmitted_frequency):
    # Calculate Doppler shift using the Doppler formula
    doppler_shift = (2 * velocity / SPEED_OF_LIGHT) * transmitted_frequency
    
    # Print the result
    print(f"Doppler Shift (frequency change) is: {doppler_shift:.6f} Hz")

def main():
    # Prompt the user for the transmitted frequency of the radar signal
    transmitted_frequency = float(input("Enter the transmitted frequency (Hz) of the Radar system: "))

    # Prompt the user for the relative velocity of the target
    velocity = float(input("Enter the relative velocity (m/s) of the target (positive if moving towards, negative if moving away):"))
    
    # Calculate and display the Doppler shift
    calculate_doppler_shift(velocity, transmitted_frequency)

if __name__ == "__main__":
    main()
