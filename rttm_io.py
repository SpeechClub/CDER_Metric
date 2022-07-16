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

def rttm_write():


    return 0

def main():
    a = rttm_read('/home/chenyifan/engineering/sd-gdga/data/nanwang/dia_part/rttm_online/20220622_144847.rttm')
    b = rttm_read('/home/chenyifan/engineering/sd-gdga/data/nanwang/dia_part/rttm_online/20220622_144847.rttm')


    print(1)

    return 0


if __name__ == "__main__":
    main()
