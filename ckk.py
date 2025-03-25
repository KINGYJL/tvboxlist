import re
import requests

# 尝试用多种编码方式读取文件
def read_file_with_fallback_encodings(file_path):
    encodings = ['utf-8', 'gbk', 'utf-16', 'latin-1']  # 常见的编码方式
    for encoding in encodings:
        try:
            with open(file_path, "r", encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"无法使用 {encodings} 中的任何编码读取文件: {file_path}")

# 从文件中提取所有URL链接
def extract_urls_from_file(file_path):
    content = read_file_with_fallback_encodings(file_path)
    # 使用正则表达式提取URL
    urls = re.findall(r'https?://[^\s"\']+', content)
    return urls

# 测试联通性并保存可用接口
def check_urls_connectivity(urls):
    available_urls = []
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                available_urls.append(url)
                print(f"可用: {url}")
            else:
                print(f"不可用: {url} (状态码: {response.status_code})")
        except requests.RequestException as e:
            print(f"不可用: {url} (错误: {e})")
    return available_urls

# 将可用接口保存到新文件
def save_available_urls(available_urls, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        for url in available_urls:
            file.write(url + "\n")
    print(f"可用接口已保存到 '{output_file}'")

# 主函数
def main(input_file, output_file):
    # 从文件中提取URL
    urls = extract_urls_from_file(input_file)
    print(f"共提取到 {len(urls)} 个URL链接")

    # 测试联通性
    available_urls = check_urls_connectivity(urls)
    print(f"共找到 {len(available_urls)} 个可用接口")

    # 保存可用接口
    save_available_urls(available_urls, output_file)

# 运行脚本
if __name__ == "__main__":
    input_file = "new.txt"  # 替换为您的文件路径
    output_file = "可用接口.txt"  # 输出文件路径
    main(input_file, output_file)
