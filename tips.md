## 常见错误解决

### SyntaxError: Non-ASCII character '\xe5'
* 这个问题是：python的默认编码文件是用的ASCII码，你将文件存成了UTF-8 （一般情况是在文件中有中文的情况）
* 解决方案：在文件开头加入：

```python
# -*- coding: UTF-8 -*-    或者  #coding=utf-8
```




本文档是有特殊意义，未经许可，请勿转载。