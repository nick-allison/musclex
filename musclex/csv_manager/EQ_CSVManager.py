"""
Copyright 1999 Illinois Institute of Technology

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL ILLINOIS INSTITUTE OF TECHNOLOGY BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Except as contained in this notice, the name of Illinois Institute
of Technology shall not be used in advertising or otherwise to promote
the sale, use or other dealings in this Software without prior written
authorization from Illinois Institute of Technology.
"""

from os.path import exists
from os import makedirs
import pandas as pd
try:
    from ..utils.file_manager import fullPath
except: # for coverage
    from utils.file_manager import fullPath

class EQ_CSVManager:
    """
    A class taking care of writing results including csv file and failedcases file.
    It creates 2 files, summary and summary2, with a different way to display the results for each.
    """
    def __init__(self, dir_path):
        """
        init with directory path
        :param dir_path:
        """
        result_path = fullPath(dir_path, "eq_results")
        self.dataframe = None
        self.dataframe2 = None
        if not exists(result_path):
            makedirs(result_path)
        self.filename = fullPath(result_path, 'summary.csv')
        self.colnames = ["Filename","Side","Distance From Center","Area","Sigma D","Sigma S","Sigma C",
                        "gamma","Z line","Sigma Z","Iz","gamma Z", "Extra peak","Sigma Z EP","Iz EP","gamma Z EP",
                        "Model", "CenterX", "S10", "d10",
                        "I11/I10", "Average I11/I10 per fiber", "Fitting error","comment"]
        self.filename2 = fullPath(result_path, 'summary2.csv')
        self.colnames2 = ['Filename', 'left peak 0', 'right peak 0', 'left peak 1', 'right peak 1',
                         'left Sigma D', 'right Sigma D', 'left Sigma S', 'right Sigma S', 'left Sigma C',
                         'right Sigma C', 'left gamma', 'right gamma', 'left Z line', 'right Z line',
                         'left Sigma Z', 'right Sigma Z', 'left Iz', 'right Iz', 'left gamma Z',
                         'right gamma Z', 'left Extra peak', 'right Extra peak',
                         'left Sigma Z EP', 'right Sigma Z EP', 'left Iz EP', 'right Iz EP', 'left gamma Z EP',
                         'right gamma Z EP', 'Model', 'CenterX', 'S10', 'd10', 'left I11/I10', 'right I11/I10',
                         'Average I11/I10 per fiber', 'Fitting error', 'comment']
        self.loadFailedCases(dir_path)
        self.loadSummary()
        self.loadSummary2()

    def loadFailedCases(self, direc):
        """
        Load failed cases file from the directory and keep them in self.failedcases
        :param direc: input directory (str)
        :return: -
        """
        self.failedcasesfile = fullPath(direc, "failedcases.txt")
        self.failedcases = set()
        if exists(self.failedcasesfile):
            for line in open(self.failedcasesfile, 'r'):
                name = line.rstrip('\n')
                self.failedcases.add(name)

    def loadSummary(self):
        """
        Load summary.csv file and keep data in self.dataframe
        :return:
        """
        if not exists(self.filename):
            self.dataframe = pd.DataFrame(columns = self.colnames)
        else:
            self.dataframe = pd.read_csv(self.filename)

    def loadSummary2(self):
        """
        Load summary.csv file and keep data in self.dataframe2
        :return:
        """
        if not exists(self.filename2):
            self.dataframe2 = pd.DataFrame(columns = self.colnames2)
        else:
            self.dataframe2 = pd.read_csv(self.filename2)

    def writeNewData(self, bioImg):
        """
        Add new data to dataframe, then re-write summary.csv and failed cases file
        :param bioImg: EquatorImage object with results in its info dict
        :return: -
        """
        file_name = bioImg.filename
        info = bioImg.info
        self.removeData(file_name)
        new_datas = []

        # If image is rejected
        if "reject" in info and info["reject"]:
            data = {}
            for k in self.dataframe.columns:
                data[k] = '-'
            data['Filename'] = file_name
            data['comment'] = "REJECTED"
            new_datas = [data]
        else:
            failed = False
            # Get all needed infos
            if 'peaks' not in info:
                data = {}
                for k in self.dataframe.columns:
                    data[k] = '-'
                data['Filename'] = file_name
                data['comment'] = "No effective peaks detected"
                new_datas = [data]
                failed = True
            else:
                if 'fit_results' in info:
                    fit_results = info['fit_results']
                    all_S = fit_results['all_S']
                    for side in ['left', 'right']:
                        areas = fit_results[side+'_areas']

                        for i in range(len(areas)):
                            data = {
                                "Filename": file_name,
                                "Side": side,
                                "Distance From Center": all_S[i],
                                "Area" : areas[i]
                            }
                            if i == 0:
                                first_row = data
                            new_datas.append(data)

                        # Write data to the first row of each side
                        first_row.update({
                            "Sigma C": abs(fit_results[side+'_sigmac']),
                            "Sigma D": abs(fit_results[side+'_sigmad']),
                            "Sigma S": abs(fit_results[side+'_sigmas']),
                            "I11/I10": fit_results[side+'_ratio'],
                        })
                        if fit_results["model"] == 'Voigt':
                            first_row["gamma"] = fit_results[side+'_gamma']
                        if fit_results["isSkeletal"]:
                            first_row["Z line"] = fit_results[side+'_zline']
                            first_row["Sigma Z"] = fit_results[side+'_sigmaz']
                            first_row["Iz"] = fit_results[side+'_intz']
                            if fit_results["model"] == 'Voigt':
                                first_row["gamma Z"] = fit_results[side+'_gammaz']
                            if fit_results["isExtraPeak"]:
                                first_row["Extra peak"] = fit_results[side+'_zline_EP']
                                first_row["Sigma Z EP"] = fit_results[side+'_sigmaz_EP']
                                first_row["Iz EP"] = fit_results[side+'_intz_EP']
                                if fit_results["model"] == 'Voigt':
                                    first_row["gamma Z EP"] = fit_results[side+'_gammaz_EP']


                    # Write general information to the first row of image
                    first_row = new_datas[0]

                    if fit_results["fiterror"] > 0.2:
                        first_row['comment'] = 'High Fitting Error'
                        failed = True

                    first_row['S10'] = fit_results['S10']
                    first_row['Model'] = fit_results['model']
                    first_row['Average I11/I10 per fiber'] = fit_results['avg_ratio']
                    first_row['Model'] = fit_results['model']
                    first_row['Fitting error'] = fit_results['fiterror']
                    first_row['CenterX'] = round(fit_results['centerX'], 2)

                    if 'd10' in fit_results.keys():
                        first_row['d10'] = fit_results['d10']
                    else:
                        first_row['d10'] = '-'
                else:
                    data = {}
                    for k in self.dataframe.columns:
                        data[k] = '-'
                    data['Filename'] = file_name
                    data['comment'] = "Model cannot be fit"
                    new_datas = [data]
                    failed = True

            if failed:
                self.failedcases.add(file_name)
            elif file_name in self.failedcases:
                self.failedcases.remove(file_name)

        self.dataframe = pd.concat([self.dataframe, pd.DataFrame.from_records(new_datas)])
        # self.dataframe = self.dataframe.append(new_datas, ignore_index=True) # Future warning deprecated
        self.dataframe.reset_index()
        self.dataframe.to_csv(self.filename, index=False, columns=self.colnames) # Write to csv file

        # Write all failed cases to failed cases file
        f = open(self.failedcasesfile, 'w')
        f.write("\n".join(list(self.failedcases)))
        f.close()

    def writeNewData2(self, bioImg):
        """
        Add new data to dataframe2, then re-write summary.csv and failed cases file
        :param bioImg: EquatorImage object with results in its info dict
        :return: -
        """
        file_name = bioImg.filename
        info = bioImg.info
        self.removeData2(file_name)
        data = {}

        # If image is rejected
        if "reject" in info and info["reject"]:
            for k in self.dataframe2.columns:
                data[k] = '-'
            data['Filename'] = file_name
            data['comment'] = "REJECTED"
        else:
            failed = False
            # Get all needed infos
            if 'peaks' not in info:
                for k in self.dataframe2.columns:
                    data[k] = '-'
                data['Filename'] = file_name
                data['comment'] = "No effective peaks detected"
                failed = True
            else:
                if 'fit_results' in info:
                    fit_results = info['fit_results']
                    all_S = fit_results['all_S']
                    data['Filename'] = file_name
                    for side in ['left', 'right']:
                        areas = fit_results[side+'_areas']
                        for i in range(len(areas)):
                            data[f'{side} peak {i}'] = all_S[i]

                        data.update({
                            side+" Sigma C": abs(fit_results[side+'_sigmac']),
                            side+" Sigma D": abs(fit_results[side+'_sigmad']),
                            side+" Sigma S": abs(fit_results[side+'_sigmas']),
                            side+" I11/I10": fit_results[side+'_ratio'],
                        })
                        if fit_results["model"] == 'Voigt':
                            data[side+" gamma"] = fit_results[side+'_gamma']
                        if fit_results["isSkeletal"]:
                            data[side+" Z line"] = fit_results[side+'_zline']
                            data[side+" Sigma Z"] = fit_results[side+'_sigmaz']
                            data[side+" Iz"] = fit_results[side+'_intz']
                            if fit_results["model"] == 'Voigt':
                                data[side+" gamma Z"] = fit_results[side+'_gammaz']
                            if fit_results["isExtraPeak"]:
                                data[side+" Extra peak"] = fit_results[side+'_zline_EP']
                                data[side+" Sigma Z EP"] = fit_results[side+'_sigmaz_EP']
                                data[side+" Iz EP"] = fit_results[side+'_intz_EP']
                                if fit_results["model"] == 'Voigt':
                                    data[side+" gamma Z EP"] = fit_results[side+'_gammaz_EP']

                    if fit_results["fiterror"] > 0.2:
                        data['comment'] = 'High Fitting Error'
                        failed = True

                    data['S10'] = fit_results['S10']
                    data['Model'] = fit_results['model']
                    data['Average I11/I10 per fiber'] = fit_results['avg_ratio']
                    data['Model'] = fit_results['model']
                    data['Fitting error'] = fit_results['fiterror']
                    data['CenterX'] = round(fit_results['centerX'], 2)

                    if 'd10' in fit_results.keys():
                        data['d10'] = fit_results['d10']
                    else:
                        data['d10'] = '-'
                else:
                    for k in self.dataframe2.columns:
                        data[k] = '-'
                    data['Filename'] = file_name
                    data['comment'] = "Model cannot be fit"
                    failed = True

            if failed:
                self.failedcases.add(file_name)
            elif file_name in self.failedcases:
                self.failedcases.remove(file_name)

        self.dataframe2 = pd.concat([self.dataframe2, pd.DataFrame.from_records([data])])
        # self.dataframe2 = self.dataframe2.append(data, ignore_index=True) # Future warning deprecated
        self.dataframe2.reset_index()
        self.dataframe2.to_csv(self.filename2, index=False, columns=self.colnames2) # Write to csv file

    def removeData(self, file_name):
        """
        Remove data from dataframe
        :param file_name: (str)
        :return:
        """
        self.dataframe = self.dataframe[self.dataframe["Filename"] != file_name]

    def removeData2(self, file_name):
        """
        Remove data from dataframe2
        :param file_name: (str)
        :return:
        """
        self.dataframe2 = self.dataframe2[self.dataframe2["Filename"] != file_name]
