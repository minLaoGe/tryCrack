import scrapy
import json

class QQMusicSpider(scrapy.Spider):
    name = "qqmusic"
    allowed_domains = ["y.qq.com", "u6.y.qq.com"]
    start_urls = ["https://u6.y.qq.com/cgi-bin/musics.fcg"]

    def start_requests(self):
        # 请求的参数
        params = {
            '_': '1732174503887',
            'sign': 'zzccd7a34aomna4utxcad3gfhj0ft6vh011a397ca139',
        }

        # Cookies
        cookies = {
            'pgv_pvid': '8281634143',
            'fqm_pvqid': '6e4cd7b0-6324-4635-a675-8a1a4110c9e5',
            'fqm_sessionid': '49215737-12e1-4037-9127-e468c6620bf8',
            'pgv_info': 'ssid=s1831168672',
            'ts_refer': 'cn.bing.com/',
            'ts_uid': '4546005376',
            '_qpsvr_localtk': '0.9922212454494288',
            'RK': 'qHf1JeYGky',
            'ptcz': '4d70c81c9f2028da22d182807f0eb5be891b420270e3a1cd856a752bc6a91919',
            'login_type': '1',
            'wxunionid': '',
            'tmeLoginType': '2',
            'wxrefresh_token': '',
            'wxopenid': '',
            'psrf_musickey_createtime': '1732174479',
            'psrf_access_token_expiresAt': '1732779279',
            'euin': 'owEkoe4q7wSzov**',
            'psrf_qqopenid': '83FBEDC825188B7053D4D5D5BF1BEEDD',
            'psrf_qqaccess_token': '8AF42F5149EE4DDD68CA4C11132DA7DC',
            'uin': '2950596701',
            'psrf_qqrefresh_token': '9AC32133B026A96939B68F27694B0251',
            'psrf_qqunionid': '539BFB2E8961DC499EE089F9F7D655B9',
            'qm_keyst': 'Q_H_L_63k3NephSPkv3eqoIqnIhF7krWjtcjnOme5iEVNE86EZ9gaiPcoxT-RtnC3EqTWSh1tO7YhwSYfZLeE2A9RPWNn9m1s8',
            'music_ignore_pskey': '202306271436Hn@vBj',
            'qqmusic_key': 'Q_H_L_63k3NephSPkv3eqoIqnIhF7krWjtcjnOme5iEVNE86EZ9gaiPcoxT-RtnC3EqTWSh1tO7YhwSYfZLeE2A9RPWNn9m1s8',
            'ts_last': 'y.qq.com/n/ryqq/player',
        }

        # Headers
        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://y.qq.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://y.qq.com/',
            'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        }

        # 数据
        data = json.dumps({
            "comm": {
                "cv": 4747474,
                "ct": 24,
                "format": "json",
                "inCharset": "utf-8",
                "outCharset": "utf-8",
                "notice": 0,
                "platform": "yqq.json",
                "needNewCode": 1,
                "uin": 2950596701,
                "g_tk_new_20200303": 1971603813,
                "g_tk": 1971603813
            },
            "req_1": {
                "module": "userInfo.VipQueryServer",
                "method": "SRFVipQuery_V2",
                "param": {
                    "uin_list": ["2950596701"]
                }
            },
            "req_2": {
                "module": "userInfo.BaseUserInfoServer",
                "method": "get_user_baseinfo_v2",
                "param": {
                    "vec_uin": ["2950596701"]
                }
            },
            "req_3": {
                "module": "music.lvz.VipIconUiShowSvr",
                "method": "GetVipIconUiV2",
                "param": {"PID": 3}
            },
            "req_4": {
                "module": "music.musicasset.SongFavRead",
                "method": "IsSongFanByMid",
                "param": {"v_songMid": ["003w13L71JbNMK"]}
            },
            "req_5": {
                "module": "music.musichallSong.PlayLyricInfo",
                "method": "GetPlayLyricInfo",
                "param": {
                    "songMID": "003w13L71JbNMK",
                    "songID": 545216417
                }
            },
            "req_6": {
                "method": "GetCommentCount",
                "module": "music.globalComment.GlobalCommentRead",
                "param": {
                    "request_list": [{"biz_type": 1, "biz_id": "545216417", "biz_sub_type": 0}]
                }
            },
            "req_7": {
                "module": "music.musichallAlbum.AlbumInfoServer",
                "method": "GetAlbumDetail",
                "param": {"albumMid": "003mWs7r1YklxT"}
            },
            "req_8": {
                "module": "music.vkey.GetVkey",
                "method": "GetUrl",
                "param": {
                    "guid": "3226243125",
                    "songmid": ["003w13L71JbNMK"],
                    "songtype": [0],
                    "uin": "2950596701",
                    "loginflag": 1,
                    "platform": "20"
                }
            }
        })

        # 发起 POST 请求
        yield scrapy.Request(
            url=self.start_urls[0],
            method="POST",
            headers=headers,
            cookies=cookies,
            body=data,
            callback=self.parse_response,
            cb_kwargs={'params': params}
        )

    def parse_response(self, response, params):
        # 解析响应
        json_data = response.json()
        self.logger.info("Response data:")
        self.logger.info(json_data)

        # 将数据保存或进一步处理
        yield {"data": json_data}
    def requestmusicsfcg(self):
        # 请求的参数
        params = {
            '_': '1732175606676',
            'sign': 'zzc7988ebfjtd8hrdybm1yc6xmpzuorrc86cef93f5cf',
        }

        # Cookies
        cookies = {
            'pgv_pvid': '8281634143',
            'fqm_pvqid': '6e4cd7b0-6324-4635-a675-8a1a4110c9e5',
            'fqm_sessionid': '49215737-12e1-4037-9127-e468c6620bf8',
            'pgv_info': 'ssid=s1831168672',
            'ts_refer': 'cn.bing.com/',
            'ts_uid': '4546005376',
            '_qpsvr_localtk': '0.9922212454494288',
            'RK': 'qHf1JeYGky',
            'ptcz': '4d70c81c9f2028da22d182807f0eb5be891b420270e3a1cd856a752bc6a91919',
            'login_type': '1',
            'wxunionid': '',
            'tmeLoginType': '2',
            'wxrefresh_token': '',
            'wxopenid': '',
            'psrf_musickey_createtime': '1732174479',
            'psrf_access_token_expiresAt': '1732779279',
            'euin': 'owEkoe4q7wSzov**',
            'psrf_qqopenid': '83FBEDC825188B7053D4D5D5BF1BEEDD',
            'psrf_qqaccess_token': '8AF42F5149EE4DDD68CA4C11132DA7DC',
            'uin': '2950596701',
            'psrf_qqrefresh_token': '9AC32133B026A96939B68F27694B0251',
            'psrf_qqunionid': '539BFB2E8961DC499EE089F9F7D655B9',
            'qm_keyst': 'Q_H_L_63k3NephSPkv3eqoIqnIhF7krWjtcjnOme5iEVNE86EZ9gaiPcoxT-RtnC3EqTWSh1tO7YhwSYfZLeE2A9RPWNn9m1s8',
            'music_ignore_pskey': '202306271436Hn@vBj',
            'qqmusic_key': 'Q_H_L_63k3NephSPkv3eqoIqnIhF7krWjtcjnOme5iEVNE86EZ9gaiPcoxT-RtnC3EqTWSh1tO7YhwSYfZLeE2A9RPWNn9m1s8',
            'ts_last': 'y.qq.com/n/ryqq/player',
        }

        # Headers
        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://y.qq.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://y.qq.com/',
            'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        }

        # 数据
        data = json.dumps({
            "comm": {
                "cv": 4747474,
                "ct": 24,
                "format": "json",
                "inCharset": "utf-8",
                "outCharset": "utf-8",
                "notice": 0,
                "platform": "yqq.json",
                "needNewCode": 1,
                "uin": 2950596701,
                "g_tk_new_20200303": 1971603813,
                "g_tk": 1971603813,
            },
            "req_1": {
                "module": "userInfo.VipQueryServer",
                "method": "SRFVipQuery_V2",
                "param": {"uin_list": ["2950596701"]},
            },
            "req_2": {
                "module": "userInfo.BaseUserInfoServer",
                "method": "get_user_baseinfo_v2",
                "param": {"vec_uin": ["2950596701"]},
            },
            "req_3": {
                "module": "music.lvz.VipIconUiShowSvr",
                "method": "GetVipIconUiV2",
                "param": {"PID": 3},
            },
            "req_4": {
                "module": "music.musicasset.SongFavRead",
                "method": "IsSongFanByMid",
                "param": {"v_songMid": ["003w13L71JbNMK"]},
            },
            "req_5": {
                "module": "music.musichallSong.PlayLyricInfo",
                "method": "GetPlayLyricInfo",
                "param": {"songMID": "003w13L71JbNMK", "songID": 545216417},
            },
            "req_6": {
                "method": "GetCommentCount",
                "module": "music.globalComment.GlobalCommentRead",
                "param": {
                    "request_list": [
                        {"biz_type": 1, "biz_id": "545216417", "biz_sub_type": 0}
                    ]
                },
            },
            "req_7": {
                "module": "music.musichallAlbum.AlbumInfoServer",
                "method": "GetAlbumDetail",
                "param": {"albumMid": "003mWs7r1YklxT"},
            },
            "req_8": {
                "module": "music.vkey.GetVkey",
                "method": "GetUrl",
                "param": {
                    "guid": "3786771100",
                    "songmid": ["003w13L71JbNMK"],
                    "songtype": [0],
                    "uin": "2950596701",
                    "loginflag": 1,
                    "platform": "20",
                },
            },
        })

        # 发起 POST 请求
        yield scrapy.Request(
            url=self.start_urls[0],
            method="POST",
            headers=headers,
            cookies=cookies,
            body=data,
            callback=self.parse_response,
        )

    def parse_response(self, response):
        # 解析响应
        json_data = response.json()
        self.logger.info("Response data:")
        self.logger.info(json_data)

        # 将数据保存或进一步处理
        yield {"data": json_data}
