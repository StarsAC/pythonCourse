import argparse
import chardet
import codecs

# 创建ArgumentParser对象
parser = argparse.ArgumentParser(description='Convert file to UTF-8 encoding')
parser.add_argument('filename', help='Input file name')
parser.add_argument('--encoding', help='Input file encoding (optional)')

# 解析命令行参数
args = parser.parse_args()

# 获取文件名和编码格式
filename = args.filename
file_encoding = args.encoding

# 如果没有指定编码格式，则使用chardet来猜测
if not file_encoding:
    with open(filename, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        file_encoding = result['encoding']

# 读取文件并转存成UTF-8格式
with codecs.open(filename, 'r', encoding=file_encoding) as f:
    content = f.read()

with codecs.open(filename + '_utf8', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"文件 {filename} 已成功转存成UTF-8格式为 {filename}_utf8")
