import json

# 读取可用接口文件
def read_available_urls(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        urls = file.readlines()
        # 去除每行的换行符
        urls = [url.strip() for url in urls if url.strip()]
        return urls

# 将可用接口保存为多仓配置文件
def save_as_multistore_config(available_urls, output_file):
    stores = []
    for i, url in enumerate(available_urls):
        stores.append({
            "name": f"仓库{i + 1}",  # 仓库名称
            "url": url  # 仓库URL
        })
    config = {
        "stores": stores
    }
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(config, file, ensure_ascii=False, indent=2)
    print(f"多仓配置文件已保存到 '{output_file}'")

# 主函数
def main(input_file, output_file):
    # 读取可用接口
    available_urls = read_available_urls(input_file)
    print(f"共找到 {len(available_urls)} 个可用接口")

    # 保存为多仓配置文件
    save_as_multistore_config(available_urls, output_file)

# 运行脚本
if __name__ == "__main__":
    input_file = "ky.txt"  # 替换为您的可用接口文件路径
    output_file = "多仓配置.json"  # 输出文件路径
    main(input_file, output_file)
