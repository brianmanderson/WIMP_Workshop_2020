__author__ = 'Brian M Anderson'
# Created on 2/17/2020
from Workshop_Modules.Merge_Notebooks import merge_notebooks_function, os

path_to_notebooks = os.path.join('.','Workshop_Modules')
out_path_name = os.path.join('.','Click_Me.ipynb')
merge_notebooks_function(path_to_notebooks=path_to_notebooks,combined_notebook_path=out_path_name)