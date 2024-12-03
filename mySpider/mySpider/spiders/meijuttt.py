import os
import scrapy

class MeijutttSpider(scrapy.Spider):
    name = "meijuttt"
    allowed_domains = ["hn.bfvvs.com"]
    start_urls = ["https://hn.bfvvs.com/play/mbkqgO6e/index.m3u8"]
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
        'cache-control': 'no-cache',
        'origin': 'https://jiexi.tanju.vip',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    def __init__(self, folder_path="downloads", *args, **kwargs):
        super(MeijutttSpider, self).__init__(*args, **kwargs)
        # 创建保存 TS 文件的文件夹
        self.folder_path = folder_path
        os.makedirs(self.folder_path, exist_ok=True)

    def start_requests(self):
        yield scrapy.Request(
            # 该地址为登录青年大学习之后的地址
            url="https://hn.bfvvs.com/play/mbkqgO6e/index.m3u8",
            callback=self.parse,
            method='GET',
            headers=self.headers,
        )

    def parse(self, response):
        """
        解析 m3u8 文件，提取 .ts 文件 URL，并调度下载任务
        """
        # 设置响应编码为 UTF-8
        response = response.replace(headers={"Content-Type": "application/json"})

        # 打印响应内容
        self.logger.info(f"Response Text: {response.text[:500]}...")  # 打印前500个字符以避免日志过长

        # 提取 m3u8 文件中的 TS 文件 URL
        ts_urls = [
            line.strip()
            for line in response.text.splitlines()
            if line.startswith("http")
        ]
        self.logger.info(f"Found {len(ts_urls)} TS files to download.")

        # 为每个 TS 文件创建下载请求
        for ts_url in ts_urls:
            yield scrapy.Request(
                url=ts_url,
                callback=self.save_ts_file2,
                method='GET',
                headers=self.headers,
                meta={"filename": os.path.basename(ts_url)},
            )

    def save_ts_file2(self, response):
        """
        保存下载的 .ts 文件到本地
        """
        print(response.text)
        filename = response.meta["filename"]
        file_path = os.path.join(self.folder_path, filename)

        # 将 .ts 文件内容写入本地文件
        try:
            with open(file_path, "wb") as f:
                f.write(response.body)
            self.logger.info(f"Downloaded: {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to save {file_path}: {e}")
