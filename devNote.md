
## 安装配置

### pypi
pip install templatepy

#### testpypi?


### 本地安装
cd simple_template_copy
pip install ./


### dev 模式? ⭐
> https://setuptools.pypa.io/en/latest/userguide/quickstart.html
pip install --editable .

pip install -e ./
### 模板位置指定

- [x] 环境变量
  - [x] tempy_templates_dir
- [x] 默认位置
  - [x] ~/tempy_templates_dir


## 使用 
tempy




## doing



## todo
* 覆盖提示?
* 发布?



使用类重构?

配置文件问题?

依赖?
  fuzzywuzzy
  python-Levenshtein

filecmp
定制复制操作?覆盖问题
覆盖提醒,these file will change

发布
使用例子

注意git存档
文档更新


## done
* 帮助文本显示?

./ 支持 (copy tree,dirs_exist_ok=True)
多文件创建
匹配算法改进(改进了下simple match的提示)
* 执行总结
* 执行提示
  * match
  * copy info

- [ ] 基本流程构建
  - [x] docopt 构建
  - [x] template str 解析
  - [x] target str 解析
  - [x] template path,target path
  - [x] valid template path,valid template path
  - [ ] 确认 ?
  - [x] 复制操作
  - [ ] 成功不显示信息?
- [ ] 使用流程文件
  - [ ] 安装
  - [ ] 位置
  - [ ] 使用
- [ ] 配置项(模板位置)
  - [x] 环境变量
    - [x] tempy_templates_dir
  - [x] 默认位置
    - [x] ~/tempy_templates_dir
  - [x] 链接解析
  - [x] 配置文件??,no
  - [x] 链接?,no
  - [x] 多模板文件夹?,no
- [x] debug 模式
  - [x] debug 标志
  - [x] log 级别
- [ ] 模板库
  - [ ] 只说明位置
- [ ] 发布?
  - [ ] 预设模板
  - [ ] 调整模板文件夹位置
  - [x] pyproject ,先不用管
  - [x] setup.py ,主要
    - [x] 编写安装配置文件
  - [ ] 上传
- [ ] 开发流程 
  - [ ] 在src 中运行是导入本地的包的,可以顺利调试开发
- [ ] 优化
- [ ] 解耦
  - [ ] 让方法更通用

### 基本用例
- [ ] cmd 
  - [ ] 帮助信息
- [ ] cmd template_str
  - [ ] only show possible template path
- [ ] cmd template_str target_str
- [ ] --log_level=debug
- [ ] --test
  - [ ] 不执行具体操作,

## 文件说明
* core.py
  * 程序主要运行代码
* docopt_wrapper.py 
  * 使用 docopt 解析,传递参数
* fire_cli,弃用


## 开发流程
文件结构
setup.py
pip install,upgrade



## 文件结构
引用脚本放在包外面,
进入点用scripts