#!/usr/bin/python3
import os
from flask import Flask, request, jsonify
from TOKEN import *

import sys
sys.path.append('../../custom_function')
from top_ranked_word import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename=LOG_DIR + '/log.txt',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "text"
    }

    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']

    if content == u"실검":
        for portal_site in ['Daum', 'Naver']:
            real_rank_item = get_rank_string(portal_site)

            if real_rank_item is not None:
                # update.message.reply_text(portal_site + " 실시간 검색어 1위")
                # real_rank_wo_whitespace = urllib.parse.quote_plus(real_rank_item)
                # html_tag = '<a href="' + query_address[
                #     portal_site] + real_rank_wo_whitespace + '">' + real_rank_item + '</a>'
                # bot.sendMessage(parse_mode='HTML', chat_id=update.message.chat_id, text=html_tag)
                message_text = real_rank_item
            else:
                logger.info("%s : parsing error" % portal_site)
                # update.message.reply_text(portal_site + " site가 수정되어 봇 업데이트가 필요합니다. 최대한 빨리 업데이트 하겠습니다.")
                # bot.sendMessage(chat_id=MANAGER_ID, text="실시간 검색어 봇에서 " + portal_site + "에 대한 업데이트가 필요합니다.")
                message_text = portal_site + " site가 수정되어 업데이트가 필요합니다."

        dataSend = {
            "message": {
                "text": message_text
            }
        }
    elif content == u"도움말":
        dataSend = {
            "message": {
                "text": "아직 준비되지 않았습니다."
            }
        }
    else:
        dataSend = {
            "message": {
                "text": "아직 준비되지 않았습니다."
            }
        }

    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
