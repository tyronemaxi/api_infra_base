python Cookbook


本文档旨在说明 python 语言特点，梳理后端项目 MVC 开发规范，目标是编写






可维护性（maintainability）








可读性（readability）








可扩展性（extensibility）








简洁性（simplicity）








可复用性（reusability）








可测试性（testability）的高质量代码。
优先级逐渐递减








说明


python 是一门面向对象编程语言, OOPL（Obeject Oriented Programming Language）
具备以下几个特点：




解释性


可塑性


不被谈及的高级特性


兼容性，可移植，可扩展性，可嵌入好


胶水语言……




每个人的审美价值不同，对代码质量的认知会有不同。在实际的代码开发中，任务时间是紧迫的，我们追求而不强求所有代码按照此种方式进行编写，
当然，项目代码规范非一日之功，希望大家能够建立共同的代码质量规范，这也是此文档的由来。
对于本项目来说，标准不应成为开发工程师进步的牢笼，也非常欢迎各位优秀的开发工程师能加入讨论和 commit 共同改进此文档。


应遵守的一些原则




可读性应是代码质量的第一标准，对于此文档和 PEP8 的风格要求，如果违背更能提升代码的可读性，那么就违背它 ———代码风格应该是为人服务的，不应本末倒置


可维护性应该是代码质量的第二要求，从长期来看，一个项目代码的维护时间远远大于编写代码的时间，工程师大部分时间可能都是花在修改 BUG、改老的逻辑，所以代码的可维护性就显得格外重要


对于一个业务功能而言，若是不能清晰通过文字表述出来，这往往是业务存在问题，先进行确认


若在实现某个需求时，从设计上就非常困难，这可能也是业务员的问题，也有可能是架构的问题。——好的技术架构往往不存在难做的业务




PEP 8 规范


PEP8 规范


补充说明


我们使用 PEP8 作为基础编码规范，并基于改规范进行进一步扩展：


函数类型标注


参数标注`必须使用，可加强代码工程师对于参数的类型问题的检查。
Return 标注不做强制要求。


from typing import List, Union, Any
def method(a: str, b: int, c:List, d: Any):
    # do something
    return a, b, c, d



模块引用（Imports）




模块引用应该分行写，且按照三种类型进行划分：


标准库


第三方库


本地库
顺序不做要求








import re
import os
import collections

from langchain import prompts

from app.common.log import logger
from app.controller.pdf_backtrack.pdf_backtrack import PDF_TRACKBALL_DIR



相对导入还是绝对导入


原则上无脑使用绝对导入，在主文件中，不允许使用相对导入，在子包中允许使用对同级别文件的相对导入（逻辑更好）
关于使用绝对导入还是相对导入的讨论


字符串单引号还是双引号


不做规定，个人推荐使用双引号，2个好处：




Dict 风格更 json 化，复制粘贴也比较方便


贴近其他编程语言风格




风格约定


面向对象值传递


和主流 OOP 思路相反，不推荐业务中进行自定义对象传递（User）当有类似需求时，使用 namedtuple 或 dict 传递。面向对象在服务中的问题有以下三点：


​
