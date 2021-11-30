from common.utility import *

def test_download_and_extract_zip():
    res = download_zipfile("https://ganguoroshi.jp/client_info/KAWADAONLINE/view/userweb/images/KOLList.zip?timestamp=1625216694000", "test.zip")
    assert res

    assert extract_zipfile("test.zip","temp_zip")


def test_download_img():
    download_img("https://placehold.jp/150x150.png","temp_img")


def test_re_search():
    res = re_search(r"/category/(.*)", "https://www.mercari.com/jp/category/1")
    assert res == "1"
    

def test_delete_old_files():
    delete_old_files("screen_shot", day_limit=0)