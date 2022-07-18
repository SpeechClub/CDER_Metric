#!/usr/bin/env python
# encoding: utf-8

# The MIT License (MIT)

# Copyright (c) 2012-2019 CNRS

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# AUTHORS
# Gaofeng Cheng     chenggaofeng@hccl.ioa.ac.cn     (Institute of Acoustics, Chinese Academy of Science)
# Yifan Chen        chenyifan@hccl.ioa.ac.cn        (Institute of Acoustics, Chinese Academy of Science)
# Runyan Yang       yangrunyan@hccl.ioa.ac.cn       (Institute of Acoustics, Chinese Academy of Science)
# Qingxuan Li       liqx20@mails.tsinghua.edu.cn    (Tsinghua University)


import os
import re
from pyannote.core import Annotation, Segment
from diarization import DiarizationErrorRate

def rttm_read(rttm_path):
    rttm_file = open(rttm_path, mode='r', encoding='utf8')
    lines = rttm_file.readlines()

    wav_name_list = {}
    for line in lines:
        line.replace("\t", " ")
        line.replace("\n", "")
        _, wav_name, _, start_time, during_time, _, _, person_id, _ , _ = line.split(" ", 9)
        if wav_name not in wav_name_list:
            wav_name_list[wav_name] = [[start_time, during_time, person_id]]
        else:
            wav_name_list[wav_name].append([start_time, during_time, person_id])


    for wav_name, val in wav_name_list.items():
        hyp = Annotation()
        for utt in val:
            start_time = float(utt[0])
            end_time = float(utt[0]) + float(utt[1])
            hyp[Segment(start_time, end_time)] = utt[2]
        wav_name_list[wav_name] = [val, hyp]

    return wav_name_list


def main():

    return 0


if __name__ == "__main__":
    main()
