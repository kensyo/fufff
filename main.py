# -*- coding: UTF-8 -*-

import os
import urllib.request
import tarfile
import version_search
import shutil

def install_fp(home_dir, version):
    DL_URL = 'https://fpdownload.macromedia.com/get/flashplayer/pdc/' + version + '/install_flash_player_11_linux.x86_64.tar.gz'
    PLUGIN_PATH = home_dir + "/.mozilla/plugins"

    os.mkdir(PLUGIN_PATH + "/tmp") # if tmp exists, the script stops here with error
    urllib.request.urlretrieve(DL_URL, PLUGIN_PATH + '/tmp/ifp11x86_64.tar.gz')
    tf = tarfile.open(PLUGIN_PATH + '/tmp/ifp11x86_64.tar.gz', 'r')
    tf.extractall(PLUGIN_PATH + '/tmp')
    if os.path.exists(PLUGIN_PATH + '/libflashplayer.so'):
        os.remove(PLUGIN_PATH + '/libflashplayer.so')
    shutil.move(PLUGIN_PATH + '/tmp/libflashplayer.so', PLUGIN_PATH)
    shutil.rmtree(PLUGIN_PATH + '/tmp')

    fufff_file = open(home_dir + "/.fufff", 'w')
    fufff_file.write(latest_version)
    fufff_file.close()

HOME_DIR = os.environ.get('HOME')

if os.path.exists(HOME_DIR + "/.mozilla/plugins"):
    FP_URL = "https://helpx.adobe.com/jp/flash-player/kb/235703.html" # where which version of flash player is the latest is written

    htmldata = urllib.request.urlopen(FP_URL)
    parser = version_search.fpVersionHTMLParser()
    parser.feed(htmldata.read().decode('utf-8'))

    if 'Linux' in parser.latest_version():

        if os.path.exists(HOME_DIR + "/.fufff"):
            fufff_file = open(HOME_DIR + "/.fufff") # TODO: error handling
            current_version = fufff_file.read() # NOTE: this may include a newline character
            fufff_file.close()

            latest_version = parser.latest_version()['Linux']

            if current_version.replace('\n', '') != latest_version:

                install_fp(HOME_DIR, latest_version)

            else:
                if os.path.exists(HOME_DIR + "/.mozilla/plugins/libflashplayer.so"):
                    "latest!"
                    "do nothing"
                else:
                    install_fp(HOME_DIR, latest_version)

        else:
            latest_version = parser.latest_version()['Linux']
            install_fp(HOME_DIR, latest_version)

    else:
        " do nothing because of parsing error"

parser.close()
htmldata.close()
