import requests

cookies = {
    'index_location_city': '^%^E5^%^85^%^A8^%^E5^%^9B^%^BD',
    'sensorsdata2015jssdkcross': '^%^7B^%^22distinct_id^%^22^%^3A^%^2219310f41da246a-092b3b4bd8b61d8-e525627-2663424-19310f41da312c4^%^22^%^2C^%^22first_id^%^22^%^3A^%^22^%^22^%^2C^%^22props^%^22^%^3A^%^7B^%^22^%^24latest_traffic_source_type^%^22^%^3A^%^22^%^E8^%^87^%^AA^%^E7^%^84^%^B6^%^E6^%^90^%^9C^%^E7^%^B4^%^A2^%^E6^%^B5^%^81^%^E9^%^87^%^8F^%^22^%^2C^%^22^%^24latest_search_keyword^%^22^%^3A^%^22^%^E6^%^9C^%^AA^%^E5^%^8F^%^96^%^E5^%^88^%^B0^%^E5^%^80^%^BC^%^22^%^2C^%^22^%^24latest_referrer^%^22^%^3A^%^22https^%^3A^%^2F^%^2Fwww.baidu.com^%^2Flink^%^22^%^2C^%^22^%^24os^%^22^%^3A^%^22Windows^%^22^%^2C^%^22^%^24browser^%^22^%^3A^%^22Firefox^%^22^%^2C^%^22^%^24browser_version^%^22^%^3A^%^22132.0^%^22^%^7D^%^2C^%^22^%^24device_id^%^22^%^3A^%^2219310f41da246a-092b3b4bd8b61d8-e525627-2663424-19310f41da312c4^%^22^%^7D',
    'showExpriedIndex': '1',
    'showExpriedCompanyHome': '1',
    'showExpriedMyPublish': '1',
    'hasDeliver': '0',
    'privacyPolicyPopup': 'false',
    'gate_login_token': 'v1^#^#^#^#bbdb3b8ae0c66ef3b8d4289ba9cdd38c0a632bfd444c1ce1ff22a978c7220f1f',
    '__lg_stoken__': '27a48e540d3604f433788e37c0f562123222765871cad73118a00a5cad400079931ce380e7b899bdca1e692102a6b6097a9f2303db18ffea69bdf399592590db3b51be6e009b',
    'JSESSIONID': 'ABAABJAABBDABGG55433DB18CA4B20F48B117E346B09DBD',
    'X_HTTP_TOKEN': '42daf4b72327b2819589611371bf5e71415983ed09',
    'WEBTJ-ID': '20241110003100-19311c3ba6562-0d596a435638c78-f575722-2663424-19311c3ba66b97',
    '_ga': 'GA1.2.1244049279.1731169860',
    '_gat': '1',
    'user_trace_token': '20241110003100-06fdf7a8-5e92-4346-91d6-11a082ff9ca0',
    'LGSID': '20241110003100-e881e5a1-4cbd-45e5-a84c-708c17754309',
    'PRE_UTM': '',
    'PRE_HOST': '',
    'PRE_SITE': 'https^%^3A^%^2F^%^2Fm.lagou.com^%^2F',
    'PRE_LAND': 'https^%^3A^%^2F^%^2Fwww.lagou.com^%^2Fs^%^2Flist^%^5F4aed9153ed4157ece51a6ef1f82ac88f46fcc8ff7fa16711',
    'LGUID': '20241110003100-b66ad1df-aadd-4169-8d7e-017bf1515fab',
    'LGRID': '20241110003101-a12021e6-0390-4a67-af18-301cafb0c8c2',
    '_putrc': '81BADF4A4BA946B4123F89F2B170EADC',
    'login': 'true',
    'unick': '^%^E7^%^94^%^A8^%^E6^%^88^%^B73221',
    'index_location_city': '^%^E5^%^85^%^A8^%^E5^%^9B^%^BD',
    'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1731169862',
    'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1731169862',
    'HMACCOUNT': '88C9B466800437DF',
    '_gid': 'GA1.2.1357274859.1731169863',
    '_ga_DDLTLJDLHH': 'GS1.2.1731169863.1.0.1731169863.60.0.0',
    'sensorsdata2015session': '^%^7B^%^7D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    # 'Referer': 'https://www.lagou.com/wn/zhaopin?kd=Java&pn=2',
    # 'Cookie': 'index_location_city=^%^E5^%^85^%^A8^%^E5^%^9B^%^BD; sensorsdata2015jssdkcross=^%^7B^%^22distinct_id^%^22^%^3A^%^2219310f41da246a-092b3b4bd8b61d8-e525627-2663424-19310f41da312c4^%^22^%^2C^%^22first_id^%^22^%^3A^%^22^%^22^%^2C^%^22props^%^22^%^3A^%^7B^%^22^%^24latest_traffic_source_type^%^22^%^3A^%^22^%^E8^%^87^%^AA^%^E7^%^84^%^B6^%^E6^%^90^%^9C^%^E7^%^B4^%^A2^%^E6^%^B5^%^81^%^E9^%^87^%^8F^%^22^%^2C^%^22^%^24latest_search_keyword^%^22^%^3A^%^22^%^E6^%^9C^%^AA^%^E5^%^8F^%^96^%^E5^%^88^%^B0^%^E5^%^80^%^BC^%^22^%^2C^%^22^%^24latest_referrer^%^22^%^3A^%^22https^%^3A^%^2F^%^2Fwww.baidu.com^%^2Flink^%^22^%^2C^%^22^%^24os^%^22^%^3A^%^22Windows^%^22^%^2C^%^22^%^24browser^%^22^%^3A^%^22Firefox^%^22^%^2C^%^22^%^24browser_version^%^22^%^3A^%^22132.0^%^22^%^7D^%^2C^%^22^%^24device_id^%^22^%^3A^%^2219310f41da246a-092b3b4bd8b61d8-e525627-2663424-19310f41da312c4^%^22^%^7D; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; privacyPolicyPopup=false; gate_login_token=v1^#^#^#^#bbdb3b8ae0c66ef3b8d4289ba9cdd38c0a632bfd444c1ce1ff22a978c7220f1f; __lg_stoken__=27a48e540d3604f433788e37c0f562123222765871cad73118a00a5cad400079931ce380e7b899bdca1e692102a6b6097a9f2303db18ffea69bdf399592590db3b51be6e009b; JSESSIONID=ABAABJAABBDABGG55433DB18CA4B20F48B117E346B09DBD; X_HTTP_TOKEN=42daf4b72327b2819589611371bf5e71415983ed09; WEBTJ-ID=20241110003100-19311c3ba6562-0d596a435638c78-f575722-2663424-19311c3ba66b97; _ga=GA1.2.1244049279.1731169860; _gat=1; user_trace_token=20241110003100-06fdf7a8-5e92-4346-91d6-11a082ff9ca0; LGSID=20241110003100-e881e5a1-4cbd-45e5-a84c-708c17754309; PRE_UTM=; PRE_HOST=; PRE_SITE=https^%^3A^%^2F^%^2Fm.lagou.com^%^2F; PRE_LAND=https^%^3A^%^2F^%^2Fwww.lagou.com^%^2Fs^%^2Flist^%^5F4aed9153ed4157ece51a6ef1f82ac88f46fcc8ff7fa16711; LGUID=20241110003100-b66ad1df-aadd-4169-8d7e-017bf1515fab; LGRID=20241110003101-a12021e6-0390-4a67-af18-301cafb0c8c2; _putrc=81BADF4A4BA946B4123F89F2B170EADC; login=true; unick=^%^E7^%^94^%^A8^%^E6^%^88^%^B73221; index_location_city=^%^E5^%^85^%^A8^%^E5^%^9B^%^BD; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1731169862; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1731169862; HMACCOUNT=88C9B466800437DF; _gid=GA1.2.1357274859.1731169863; _ga_DDLTLJDLHH=GS1.2.1731169863.1.0.1731169863.60.0.0; sensorsdata2015session=^%^7B^%^7D',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
}

params = {
    'kd': 'Java',
    'pn': '3',
}

response = requests.get('https://www.lagou.com/wn/zhaopin', params=params, cookies=cookies, headers=headers)


with open('./recure.html', 'w',encoding='utf-8') as f:
    f.write(response.text)
