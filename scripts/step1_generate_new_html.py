# -*- coding：utf-8-*-
# 方案1：通过django修改html文件
# 方案2：通过直接修改html文件, 可行但不够优雅

def change_html_template(html_file_path:str, to_replace_dict:dict):
    # 读入
    f = open(html_file_path, "r", encoding="utf-8")
    # 获取内容
    str1 = f.read()

    line_html = list()
    for id, line in enumerate(str1.split("\n")):
        line_html.append(line)
    print(line_html)
    # 替换内容
    # basic info
    line_html[16] = f'      <p class="invoice-body-up-center-title l-s2">{to_replace_dict["shengfen"]}医疗门诊收费票据（电子）</p>'
    line_html[21] = f'        <dd class="black"><span class="l-s1 orange">票据代码：</span>{to_replace_dict["piaojudaima"]}</dd>'
    line_html[24] = f'        <dd class="black"><span class="l-s1 orange">交款人统一社会信用代码：</span>{to_replace_dict["xinyongdaima"]}</dd>'
    line_html[27] = f'        <dd class="black"><span class="l-s1 orange">交款人：</span>{to_replace_dict["jiaokuanren"]}</dd>'
    line_html[35] = f'        <dd class="black"><span class="l-s1 orange">校验码：</span>{to_replace_dict["jiaoyanma"]}</dd>'
    line_html[38] = f'        <dd class="black"><span class="l-s1 orange">开票日期：</span>{to_replace_dict["kaipiaoriqi"]}</dd>'
    line_html[44] = f'          <img width="70" height="70" src="{to_replace_dict["qrCode"]}" alt="二维码">'
    # fee info
    left, line_idx = True, 0
    for fee_item in to_replace_dict["fee_info"]:
        if left:
            line_html[64+10*line_idx] = f'          <div class="fl w160 ta-l">{fee_item["pro"]}</div>'
            line_html[65+10*line_idx] = f'          <div class="fl w97 ta-l">{fee_item["num"]}</div>'
            line_html[66+10*line_idx] = f'          <div class="fl w46 ta-l">{fee_item["money"]}</div>'
            left = False
        else:
            line_html[68 + 10 * line_idx] = f'          <div class="fl w95 ta-l">{fee_item["pro"]}</div>'
            line_html[69 + 10 * line_idx] = f'          <div class="fl w88 ta-l">{fee_item["num"]}</div>'
            line_html[70 + 10 * line_idx] = f'          <div class="fl w81 ta-l">{fee_item["money"]}</div>'
            left = True
            line_idx += 1
    # other info



    str2 = "\n".join(line_html)
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
        "kaipiaoriqi": "2023-08-01",
        "shoukuandanwei": "深圳市大韭菜人民医院",
        "fuheren": "",
        "shoukuanren": "wechat001",
        "fee_info":[
            {
            "pro": "注射费",
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
            },
            {
                "pro": "床位费",
                "num": "1 项",
                "money": "123.00",
            }
        ],
        "other info": {
            "业务流水号": "062021111111111",
            "医疗机构类型": "综合医院",
            "医保统筹基金支付": "0.00",
            "个人自负": "0.00",
            f"{fapiaoleixing}号": "X00120012",
            "医保类型": "普通患者",
            "其他支付": "0.00",
            "个人自费": "0.00",
            "医保编号": "",
            "个人账户支付":"0.00",
            "就诊日期": "20230403",
            "性别": "男",
            "个人现金支付": "237.69",
            # "zhenweichayan": f"真伪查验、报销入账反馈，请登录{shengfen}财政电子票据公共服务平台（http:crpj）"
        }
    }
    str2 = change_html_template(html_file, to_replace_dict=replace_dict)

    total_money = sum([float(fee_item["money"]) for fee_item in replace_dict["fee_info"]])
    total_money = '%.2f'%total_money
    replace_dict["total_money"] = total_money
    replace_dict["total_money_daxie"] = "数字小写转大写代码待实现"
    print(f"str2: {str2}")

    f = open('../medical-invoice/index_gen.html', 'w', encoding='utf-8')  # f.seek(0)
    # f.truncate()
    f.write(str2)
    f.close()
