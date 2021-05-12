# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, CloudBlue
# All rights reserved.
#

def generate(
    client=None,
    parameters=None,
    progress_callback=None,
    renderer_type=None,
    extra_context_callback=None,
):
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
