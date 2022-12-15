# Mat2Py
Tired of using Matlab but have a lot of Matlab code? Started using python but don't want to 
rewrite all your Matlab code? This might be the package for you!

Mat2Py converts Matlab code to Python code. It's not perfect, but it's a good starting point to work off of. It uses 
OpenAI's [Codex](https://beta.openai.com/docs/models/codex) (`code-cushman-001`) model to generate the code.

### Installation
**Note: All testing was done using Python 3.8.** Ignore any step if you already have any of these installed.
0. ```cd Mat2Py```
1. Run ```pip install -r requirements.txt``` to install dependencies.
This will install the ```openai``` library. Please note in order to use OpenAI **you will need to create an account 
and get an API key. You can do this [here](https://beta.openai.com/).**
### Testing
1. Run ```python mat2py.py -h``` to view the help menu.

### Usage
Run ```python mat2py.py -i <iterations> <input_file>``` to convert a MATLAB file to Python.
- ```-i``` is the number of iterations to run the Codex model. The default is 3. 
- ```<input_file>``` is the MATLAB file to convert.

### Example (using test.m in the tests folder)
```python mat2py.py -i 3 tests/test.m```

Please note that the output file will be named ```<input_file>.py``` and be placed in the same directory 
as the input file.

### Known Issues
None at the moment. Please report any issues you find.

Thanks and enjoy!