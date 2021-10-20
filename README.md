**Content of the source code documentation**  

1. QCQC-python is a open source quantum chemistry package for education
1. It generates basic integrals for HF, CIS or MP2.
1. Main requirements
    1. basis-set-exchange
1. Further information:

# QCQC-python

This is a template for quantum chemistry projects in <quantum chemistry> course at Shandong University by Yang Guo. 

For installation, run  
`source setup.sh`

This will pip-install basis-set-exchange on your system.

If you want to run the test module manually, execute  
`python -m unittest`  
in the `src/` directory.

## github actions

This repository contains a github action in `./github/workflows/`. This will run linting, unit tests and update the documentation upon push to the master branch and upon pull request. The action can also be run manually in the "Actions" tab on the github website.

### Linting
The linter (in this case, `flake8` will point out potential bugs, errors, styling issues, and suspicious code.

### Testing
You should always test your code against a reference. In this template, we used `unittest` which is a python core module, but `pytest` is also a popular option (it needs to be pip installed though).

So far, only *unit tests* are included in the code template (that is, tests of a specific component of the software), but as you develop your software, you should also add `integration tests` that check the overall behaviour of your code.

In the github action, the tests are performed under ubuntu, windows and mac operating systems to ensure that the code runs in different environments. Also, two different python versions are tested right now, 3.7 and 3.8.

