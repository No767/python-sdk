# The MIT License (MIT)

# Copyright (c) 2021 Norizon

# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import logging

import topgg

# import hikari


# from ..events import BotUpvoteEvent

_LOGGER = logging.getLogger("callbacks.webhook")

# this can be async too!
@topgg.endpoint("/dblwebhook", topgg.WebhookType.BOT, "youshallnotpass")
async def endpoint(
    vote_data: topgg.BotVoteData,
    # uncomment this if you want to get access to app
    # app: hikari.GatewayBot = topgg.data(hikari.GatewayBot),
):
    # this function will be called whenever someone votes for your bot.
    _LOGGER.info("Receives a vote! %s", vote_data)
    # do anything with app here.
    # app.dispatch(BotUpvoteEvent(app=app, data=vote_data))
