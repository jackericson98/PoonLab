"""The point of this code is to allow you to copy and paste the integration data from POKY into the data file and then
receive the data it contains (chemical shifts (w1, w2), line widths(lw1, lw2), volume, % error?)"""

from POKY_string_data import *


#Filter function
def clean_data(raw_str):
    clean_str = raw_str.replace("Fit group of 2 peaks.", '')
    clean_str = clean_str.replace("Fit group of 4 peaks.", '')
    return clean_str


# Volume getter function
def interpret_vol(peak_data):
    index1 = peak_data.find('vol')
    index2 = peak_data.find('rms')
    vol_data = float(peak_data[index1 + 3:index2])
    return vol_data


# Peak location getter function
def interpret_peaks(peak_data):
    index1a = peak_data.find('@') + 2
    index1b = peak_data.find(' ', 7, 17)
    peak1_data = float(peak_data[index1a: index1b])
    index2a = index1b + 1
    index2b = index2a + 6
    peak2_data = float(peak_data[index2a:index2b])
    return peak1_data, peak2_data


# Line width getter function
def interpret_line_width(peak_data):
    index1a = peak_data.find('lw') + 2
    index1b = peak_data.find('vol') - 7
    line_width1_data = float(peak_data[index1a: index1b])
    index2a = index1b
    index2b = peak_data.find('vol') - 1
    line_width2_data = float(peak_data[index2a:index2b])
    return line_width1_data, line_width2_data


# Percentage getter function
def interpret_percentage(peak_data):
    index1 = peak_data.find('%') - 4
    index2 = peak_data.find('%')
    percentage_data = float(peak_data[index1:index2])
    return percentage_data


# Single string to array function
def separate(my_str):
    data_array = []
    len_between_ps = 0
    str_num = 0
    for char in my_str:
        if char == 'p':
            data_array.append(my_str[str_num - len_between_ps - 1:str_num])
            len_between_ps = 0
        else:
            len_between_ps = len_between_ps + 1
        str_num = str_num + 1
    del data_array[0]
    return data_array


# Make an array for each data type
def interpret_all_data(data_str):

    vol_array = []
    chemShift1_array = []
    chemShift2_array = []
    line_width1_array = []
    line_width2_array = []
    percent_array = []

    clean_data_str = clean_data(data_str)
    separated_data_str = separate(clean_data_str)

    for element in separated_data_str:

        vol_array.append(interpret_vol(element))

        line_width1, line_width2 = interpret_peaks(element)
        chemShift1_array.append(line_width1)
        chemShift2_array.append(line_width2)

        line_width1_data, line_width2_data = interpret_line_width(element)
        line_width1_array.append(line_width1_data)
        line_width2_array.append(line_width2_data)

        percent_data = interpret_percentage(element)
        percent_array.append(percent_data)

    return vol_array, chemShift1_array, chemShift2_array, line_width1_array, line_width2_array, percent_array


w1 = interpret_all_data(data)[1]
w2 = interpret_all_data(data)[2]
vol = interpret_all_data(data)[0]
lw1 = interpret_all_data(data)[3]
lw2 = interpret_all_data(data)[4]
per = interpret_all_data(data)[5]
