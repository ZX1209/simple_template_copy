## 使用类重构

## 配置文件问题?
简单先测试下功能

可以直接指定文件啊,,简单的复制也是可以的

## 依赖
fuzzywuzzy
python-Levenshtein

## todo
- [ ] 基本流程构建
  - [x] docopt 构建
  - [x] template str 解析
  - [x] target str 解析
  - [x] template path,target path
  - [x] valid template path,valid template path
  - [x] 复制操作
- [ ] 使用流程文件
  - [ ] 安装
  - [ ] 位置
  - [ ] 使用
- [ ] 配置项(模板位置)
  - [x] 环境变量
    - [ ] tempy_templates_dir
  - [x] 默认位置
    - [ ] ~/tempy_templates_dir
  - [x] 链接解析
  - [x] 配置文件??,no
  - [x] 链接?,no
  - [x] 多模板文件夹?,no
- [x] debug 模式
  - [ ] debug 标志
  - [ ] log 级别
- [ ] 模板库
- [ ] 发布?
  - [ ] 预设模板
  - [x] pyproject ,先不用管
  - [x] setup.py ,主要
    - [ ] 编写安装配置文件
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
* fire_cli


## 开发流程
文件结构
setup.py
pip install,upgrade



