# Markdown表格转Excel表格

如标题所示，可以把 Markdown 表格转换为 Excel 表格。

## 介绍

带有图形化界面，根据提示操作即可完成转换。

使用 pyinstaller 打包脚本为独立的 exe 文件发行。

输入：

```
### 表1.1 数据项列表

| 数据项编号 | 数据项名 | 数据项含义 | 类型 | 长度 | 别名 | 取值范围 |
| --- | --- | --- | --- | --- | --- | --- |
| DI-1 | ReaderNo | 卡号 | 字符型 | 10 | 借阅证号 |   |
| DI-2 | ReaderName | 姓名 | 字符型 | 20 | 读者姓名 |   |
| DI-3 | Rsex | 性别 | 字符 | 2 | 性别 | （男，女） |
| DI-4 | Rbirth | 出生年月日 | 日期型 | 10 |   | YYYY-MM-DD |
| DI-5 | Rdepartment | 所在部门 | 字符型 | 50 |   | 学院/部门名 |
| DI-6 | Rtype | 读者类型 | 字符型 | 10 |   | 学生/教师 |
```

程序输出（制表符分隔）：

````
### 表1.1 数据项列表

```
数据项编号	数据项名	数据项含义	类型	长度	别名	取值范围
DI-1	ReaderNo	卡号	字符型	10	借阅证号	
DI-2	ReaderName	姓名	字符型	20	读者姓名	
DI-3	Rsex	性别	字符	2	性别	（男，女）
DI-4	Rbirth	出生年月日	日期型	10		YYYY-MM-DD
DI-5	Rdepartment	所在部门	字符型	50		学院/部门名
DI-6	Rtype	读者类型	字符型	10		学生/教师	
```
````

## 使用

1. 下载 Realses 中的 exe 文件
2. 双击运行
3. 根据界面提示粘贴 Markdown 文档文本
4. 点击转换按钮
5. 转换结果会显示，同时自动复制到剪切板

## 开发

### 配置依赖

（推荐在.venv 环境或 conda 环境下进行开发，避免污染你的主环境）

安装 Pyperclip 库

```sh
pip install pyperclip
```

安装 pyinstaller 库用于打包

```sh
pip install pyinstaller
```

### 打包

```sh
pyinstaller -w -F -i icon.ico main.pyw
```

`-w`：使打包成品运行后无终端窗口

`-F`：一份可执行文件

`-i`：图标

打包后的产物会在 dist 文件夹下。

## 协议

GNU General Public License v3.0