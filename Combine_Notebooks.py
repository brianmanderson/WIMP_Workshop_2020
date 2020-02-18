__author__ = 'Brian M Anderson'
# Created on 2/17/2020
from Workshop_Modules.Merge_Notebooks import merge_notebooks_function, os

path_to_notebooks = os.path.join('.','Workshop_Modules')
notebook_paths = [os.path.join('.','Download_Data.ipynb')] + [os.path.join('.\\Workshop_Modules',i) for i in ['DeepBox.ipynb','Data_Curation.ipynb','Liver_Model.ipynb']]
out_path_name = os.path.join('.','Click_Me.ipynb')
merge_notebooks_function(notebook_paths=notebook_paths,notebook_output_path=out_path_name)