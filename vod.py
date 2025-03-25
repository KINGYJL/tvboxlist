```python                                                            import requests
import json                                                          
def fetch_vod_data(url):                                                 response = requests.get(url)
                                                                         if response.status_code == 200:
        data = {                                                                 "vod_sites": [
                {                                                                        "name": "影视采集网站",
                    "url": url,                                                          "description": "描述该网站的内容或功能"
                }                                                                ]
        }                                                            
        with open("vods.json", 'w') as f:                                        json.dump(data, f)
                                                                             print(f"JSON文件已成功保存到 {f.name}")
    else:                                                                    raise Exception(f"请求失败，状态码: {response.status_code}")
                                                                     if __name__ == "__main__":
    url = "https://json02.heimuer.xyz/api.php/provide/vod/?ac=list"  
    try:                                                                     fetch_vod_data(url)
    except Exception as e:                                                   print(e)
```
