## Analysis of relational calls to python modules

### Various tests
- main.py works, when called from ``path/to/relational_calls_python``
- main.py does not work when called from anywhere else. The idea is that ``module.pythonfile`` is ``folder_from_place_of_execution.file_in_that_folder``
- clearly main1.py will not work, when called from folder1 then, however it also does not work when called from ``relational_calls_python``
- It does however work with ``python -m folder1.main1.py`` from the root (``relational_calls_python``) instead of using ``python folder1/main1.py``, since ``relational_calls_python`` is appended to sys implicitely. See also:
- ``folder3/main3.py``, where this is done explicitely. This file can be called from anywhere! This seems to be the cleanest solution.

### Jupyter and changing wd
- main1_test is attempting to change the wd before import, but that does not work
- It does however work in a Jupyter Notebook. Here, changing the working directory to "git/relational_python_calls", results in a runnable file

