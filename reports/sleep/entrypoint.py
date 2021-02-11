from time import sleep
from datetime import datetime, timedelta

# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, CloudBlue
# All rights reserved.
#


def generate(client, parameters, progress_callback):
    try:
        sleep_secs = int(parameters['sleep'])
    except ValueError:
        raise RuntimeError("Sleep time must be a number")

    init_time = datetime.now()
    init = 0
    while datetime.now() <= (init_time + timedelta(seconds=sleep_secs)):
        sleep(10)
        init = init + 10
        progress_callback(init, sleep_secs)

    output = [
        [
            1,
        ],
        [
            2,
        ],
    ]
    progress_callback(1, 1)

    return output
