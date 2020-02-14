# get_unit_tests
with this util you can make simple unittests

***

 h3 Getting start

to start you should execute this command in the cmd
`pip install -r requirenments.txt`

***

h3 how to use

to use tis util you should make special mark file with syntax like this:
```
func_you_want_to_test: 
 (func_params), func_result 
 (another_func_params), another_func_result 
 ```
after you do this file you can make unittests with this file, to do this, you should run this command on the cmd:
`python main.py --func_path <path_to_your_function>`
***
also you can change name of file with test with flag `--save_test` and name file with your markdown (by default you should get name of file with markdown `markup.txt`) by flag `--mark_path` 
