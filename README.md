# Python Wrapper for Sphere Engine Compiler API

_This Python package provides a convenient wrapper for accessing the Sphere Engine API. [Sphere Engine](https://sphere-engine.com/) is a powerful cloud-based platform that offers a variety of programming assessment and execution tools. This wrapper simplifies the process of integrating Sphere Engine's functionality into your Python projects._

Example of use:

```python
from code_executor import CodeExecutor

python_executor1 = CodeExecutor(
    '<token:str>',
    '<widget_id:str>',
    '<lang_id:int>(https://sphere-engine.com/supported-languages)'
)

source_code_example = "print(input(), input(), end='')"
input_data_example = "The best web pentest course is:\nhttps://punkration.ru/"

python_executor1.execute(source_code_example, input_data_example)

print(python_executor1.source_code)
print(python_executor1.output)
print(python_executor1.errors)
print(python_executor1.cmpinfo)
print(python_executor1.response)
```
