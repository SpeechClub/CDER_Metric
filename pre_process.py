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


from pyannote.core import Annotation, Segment
from diarization import DiarizationErrorRate
from rttm_io import rttm_read
import numpy as np


def rttm_read_cder(rttm_path):
    a = rttm_read(rttm_path)
    for key, val in a.items():
        annotation = Annotation(uri=key, modality='speaker')
        changepoints = {}
        changepoints_new = {}
        speakers = []
        for segment in val[0]:
            if segment[2] + '_st' in changepoints.keys():
                changepoints[segment[2] + '_st'].append(float(segment[0]))
                changepoints[segment[2] + '_end'].append(float(segment[0]) + float(segment[1]))
            else:
                changepoints[segment[2] + '_st'] = [float(segment[0])]
                changepoints[segment[2] + '_end'] = [float(segment[0]) + float(segment[1])]
                changepoints_new[segment[2] + '_st'] = []
                changepoints_new[segment[2] + '_end'] = []
                speakers.append(segment[2])

        for k, v in changepoints.items():
            v.sort()

        for spk in speakers:
            other_spk = speakers.copy()
            other_spk.remove(spk)
            pos = {}
            for spk_o in other_spk:
                pos[spk_o] = 0
            i = 0
            while i < len(changepoints[spk + '_st']):
                step = 1
                while i + step < len(changepoints[spk + '_st']):
                    flag = 0
                    for spk_o in other_spk:
                        while pos[spk_o] < len(changepoints[spk_o + '_st']):
                            if changepoints[spk_o + '_end'][pos[spk_o]] <= changepoints[spk + '_st'][i]:
                            # if changepoints[spk_o + '_end'][pos[spk_o]] <= changepoints[spk + '_end'][i]:
                                pos[spk_o] += 1
                                continue
                            if changepoints[spk_o + '_st'][pos[spk_o]] >= changepoints[spk + '_end'][i + step]:
                            # if changepoints[spk_o + '_st'][pos[spk_o]] >= changepoints[spk + '_st'][i + step]:
                                break
                            else:
                                flag = 1
                                break
                    if flag == 0:
                        step += 1
                    else:
                        break

                changepoints_new[spk + '_st'].append(changepoints[spk + '_st'][i])
                changepoints_new[spk + '_end'].append(changepoints[spk + '_end'][i + step - 1])
                annotation[Segment(changepoints[spk + '_st'][i], changepoints[spk + '_end'][i + step - 1])] = spk
                i = i + step
        a[key] = [val[0], annotation]
    return a


def main():
    a = rttm_read_cder('1.rttm')
    b = rttm_read_cder('2.rttm')

    diarization_error_rate = DiarizationErrorRate()
    result = diarization_error_rate(a, b, uem=Segment(0, 40))
    print("DER = {0:.3f}".format(result))

    return 0


if __name__ == "__main__":
    main()