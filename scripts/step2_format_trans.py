# -*- coding:utf-8 -*-
# https://pypi.org/project/html2image/

from html2image import Html2Image
hti = Html2Image()
def html2jpg(html_file:str):
    pass


if __name__ == "__main__":

    hti.screenshot(
        html_file='../medical-invoice/index_gen.html', css_file='../medical-invoice/index.css',
        save_as='medical_invoice.jpg',
        size=(900, 600)
    )