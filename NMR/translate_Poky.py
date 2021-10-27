
class Translate_Poky:
    """Use this class to translate Poky string data to volume (.vol()), chemical shift (.chem_shift()), line width
    (.line_width()) and root mean square (.rms()) arrays."""

    def __init__(self, raw_string):
        self.raw_data = raw_string
        self.vol_array = []
        self.w1_array = []
        self.w2_array = []
        self.lw1_array = []
        self.lw2_array = []
        self.rms_array = []

    def clean_data(self):  # Filter function
        raw_str = self.raw_data
        clean_str = raw_str.replace("Fit group of 2 peaks.", '')
        clean_str = clean_str.replace("Fit group of 3 peaks.", '')
        clean_str = clean_str.replace("Fit group of 4 peaks.", '')
        return clean_str

    @staticmethod
    def interpret_vol(peak_data):  # Volume getter function
        index1 = peak_data.find('vol')
        index2 = peak_data.find('rms')
        vol_data = float(peak_data[index1 + 3:index2])
        return vol_data

    @staticmethod
    def interpret_peaks(peak_data):  # Peak location getter function
        index1a = peak_data.find('@') + 2
        index1b = peak_data.find(' ', 7, 17)
        peak1_data = float(peak_data[index1a: index1b])
        index2a = index1b + 1
        index2b = index2a + 6
        peak2_data = float(peak_data[index2a:index2b])
        return peak1_data, peak2_data

    @staticmethod
    def interpret_line_width(peak_data):  # Line width getter function
        index1a = peak_data.find('lw') + 2
        index1b = peak_data.find('vol') - 7
        line_width1_data = float(peak_data[index1a: index1b])
        index2a = index1b
        index2b = peak_data.find('vol') - 1
        line_width2_data = float(peak_data[index2a:index2b])
        return line_width1_data, line_width2_data

    @staticmethod
    def interpret_rms(peak_data):  # Percentage getter function
        index1 = peak_data.find('%') - 4
        index2 = peak_data.find('%')
        rms_data = float(peak_data[index1:index2])
        return rms_data

    @staticmethod
    def separate(my_str):  # Single string to array function
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

    def interpret_all_data(self):  # Make an array for each data type

        clean_data = self.clean_data()
        separated_data_str = self.separate(clean_data)

        for element in separated_data_str:
            vol = self.interpret_vol(element)
            self.vol_array.append(vol)

            line_width1, line_width2 = self.interpret_peaks(element)
            self.w1_array.append(line_width1)
            self.w2_array.append(line_width2)

            lw1, lw2 = self.interpret_line_width(element)
            self.lw1_array.append(lw1)
            self.lw2_array.append(lw2)

            rms_data = self.interpret_rms(element)
            self.rms_array.append(rms_data)

    def vol(self):
        self.interpret_all_data()
        return self.vol_array

    def chem_shift(self):
        self.interpret_all_data()
        return self.w1_array, self.w2_array

    def line_width(self):
        self.interpret_all_data()
        return self.lw1_array, self.lw2_array

    def rms(self):
        self.interpret_all_data()
        return self.rms_array

