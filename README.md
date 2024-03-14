# Python Wrapper for Sphere Engine API

_This Python package provides a convenient wrapper for accessing the Sphere Engine API. [Sphere Engine](https://sphere-engine.com/) is a powerful cloud-based platform that offers a variety of programming assessment and execution tools. This wrapper simplifies the process of integrating Sphere Engine's functionality into your Python projects._

Example of use:

```python
from code_executor import CodeExecutor

python_executor = CodeExecutor(
    '<TOKEN:str>',
    '<WIDGET_ID:str>',
    '<language_id:int>'
)

source_code_example = "print(input(), input())"
input_data_example = "The best web pentest course is:\nhttps://punkration.ru/"

python_executor.execute(source_code_example, input_data_example)

print('source_code: ', python_executor.source_code)
print('output: ', python_executor.output)
print('errors: ', python_executor.errors)
print('server_response: ', python_executor.response)
```