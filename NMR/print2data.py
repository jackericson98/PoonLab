"""The point of this code is to allow you to copy and paste the integration data from POKY into the data file and then
receive the data it contains (chemical shifts (w1, w2), line widths(lw1, lw2), volume, % error?)"""

"""peak @ 120.228 8.200 lw 12.116 16.139 vol 6.313e+09 rms 10.2%
Isolated"""

from POKY_string_data import *

"""This function filters out the string Fit group of _ peaks."""


def clean_data(raw_str):
    clean_str = raw_str.replace("Fit group of 2 peaks.", '')
    clean_str = clean_str.replace("Fit group of 4 peaks.", '')
    return clean_str


"This function takes each peak and returns a volume value for each data point"


def interpret_vol(peak_data):
    index1 = peak_data.find('vol')
    index2 = peak_data.find('rms')
    vol_data = float(peak_data[index1 + 3:index2])
    return vol_data


"This function takes each peak and returns a peak value for each data point"


def interpret_peaks(peak_data):
    index1a = peak_data.find('@') + 2
    index1b = peak_data.find(' ', 7, 17)
    peak1_data = float(peak_data[index1a: index1b])
    index2a = index1b + 1
    index2b = index2a + 6
    peak2_data = float(peak_data[index2a:index2b])
    return peak1_data, peak2_data


"""This function takes each peak data set and returns its line widths"""


def interpret_line_width(peak_data):
    index1a = peak_data.find('lw') + 2
    index1b = peak_data.find('vol') - 7
    line_width1_data = float(peak_data[index1a: index1b])
    index2a = index1b
    index2b = peak_data.find('vol') - 1
    line_width2_data = float(peak_data[index2a:index2b])
    return line_width1_data, line_width2_data


"""This function takes individual peak data and returns percentage"""


def interpret_percentage(peak_data):
    index1 = peak_data.find('%') - 4
    index2 = peak_data.find('%')
    percentage_data = float(peak_data[index1:index2])
    return percentage_data


"""This function takes all of the data and separates it into an array of strings. You need to copy and paste the 
first set twice bug """


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


"""This function takes the entire data set and returns an array of volume data points"""


def interpret_all_vol(data_str):
    vol_array = []
    clean_data_str = clean_data(data_str)
    separated_data_str = separate(clean_data_str)
    for element in separated_data_str:
        vol_array.append(interpret_vol(element))
    return vol_array


"""This function takes the entire data set and returns 2 arrays of w1 and w2 chemical shift data points"""


def interpret_all_peaks(dataset):
    peak1_array = []
    peak2_array = []
    clean_data_str = clean_data(dataset)
    sep_clean_data = separate(clean_data_str)
    for element in sep_clean_data:
        line_width1, line_width2 = interpret_peaks(element)
        peak1_array.append(line_width1)
        peak2_array.append(line_width2)

    return peak1_array, peak2_array


"""This function takes the entire data set and returns 2 arrays of lw1 and lw2 chemical shift data points"""


def interpret_all_line_widths(dataset):
    line_width1_array = []
    line_width2_array = []
    clean_data_str = clean_data(dataset)
    sep_clean_data = separate(clean_data_str)
    for element in sep_clean_data:
        line_width1_data, line_width2_data = interpret_line_width(element)
        line_width1_array.append(line_width1_data)
        line_width2_array.append(line_width2_data)

    return line_width1_array, line_width2_array


def interpret_all_percent(dataset):
    percent_array = []
    clean_data_str = clean_data(dataset)
    sep_clean_data = separate(clean_data_str)
    for element in sep_clean_data:
        percent_data = interpret_percentage(element)
        percent_array.append(percent_data)
    return percent_array


w1 = interpret_all_peaks(data)[0]
w2 = interpret_all_peaks(data)[1]
vol = interpret_all_vol(data)
lw1 = interpret_all_line_widths(data)[0]
lw2 = interpret_all_line_widths(data)[1]
per = interpret_all_percent(data)
