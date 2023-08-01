# -*- coding：utf-8-*-
# 方案1：通过django修改html文件
# 方案2：通过直接修改html文件, 可行但不够优雅

def read_html_file(html_file_path:str, to_replace_dict:dict):
    # 读入
    f = open(html_file_path, "r", encoding="utf-8")
    # 获取内容
    str1 = f.read()

    line_html = dict()
    for id, line in enumerate(str1.split("\n")):
        line_html[id] = line
    print(line_html)
    # 替换内容
    # 票据代码
    line_html[16] = line_html[16].replace('      <p class="invoice-body-up-center-title l-s2">湖北省医疗门诊收费票据（电子）</p>',
                                          f'      <p class="invoice-body-up-center-title l-s2">{to_replace_dict["shengfen"]}医疗门诊收费票据（电子）</p>')
    line_html[21] = line_html[21].replace('        <dd class="black"><span class="l-s1 orange">票据代码：</span>42060123</dd>',
                                          f'<dd class="black"><span class="l-s1 orange">票据代码：</span>{to_replace_dict["piaojudaima"]}</dd>')
    line_html[24] = line_html[24].replace('        <dd class="black"><span class="l-s1 orange">交款人统一社会信用代码：</span>420982********0059</dd>',
                                          f'        <dd class="black"><span class="l-s1 orange">交款人统一社会信用代码：</span>{to_replace_dict["xinyongdaima"]}</dd>')

    str2 = "\n".join(line_html.values())
    return str2


if __name__ == "__main__":
    html_file = "../medical-invoice/index.html"

    shengfen = "广东省"
    shengfenpinyin = ""
    fapiaoleixing = "门诊"
    replace_dict = {
        "shengfen": shengfen,
        "qrCode": "../images/1561108150.png",
        "piaojudaima":"12344321",
        "xinyongdaima": "233821****223400",
        "jiaokuanren": "卧龙凤雏",
        "piaojuhaoma": "09876543",
        "jiaoyanma": "56789",
        "开票日期": "2023-08-01",
        "fee":[
            {
            "pro": "西药费",
            "num": "1 项",
            "money": "123.00",
            },
            {
                "pro": "中药费",
                "num": "1 项",
                "money": "123.00",
            },
            {
                "pro": "手术费",
                "num": "1 项",
                "money": "123.00",
            }
        ],
        "other info": {
            "yewuliushuihao": "062021111111111",
            "yiyuanjigouleixing": "综合医院",
            "yibaotongchoujijinzhifu": "0.00",
            "gerenzifu": "0.00",
            "menzhenhao": "X00120012",
            "yibaoleixing": "普通患者",
            "qitazhifu": "0.00",
            "gerenzifei": "0.00",
            "yibaobianhao": "",
            "gerenzhanghu":"0.00",
            "jiuzhenriqi": "20230403",
            "xingbie": "男",
            "gerenxianjinzhifu": "237.69",
            "shoukuandanwei": "深圳市大韭菜人民医院",
            "fuheren": "",
            "shoukuanren": "abc",
            "zhenweichayan": f"真伪查验、报销入账反馈，请登录{shengfen}财政电子票据公共服务平台（http:crpj）"
        }
    }
    str2 = read_html_file(html_file, to_replace_dict=replace_dict)
    print(f"str2: {str2}")

    f = open('../medical-invoice/index_gen.html', 'w', encoding='utf-8')  # f.seek(0)
    # f.truncate()
    f.write(str2)
    f.close()
