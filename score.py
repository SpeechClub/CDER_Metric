from pyannote.core import Annotation, Segment
from diarization import CSSDErrorRate, DiarizationErrorRate
from rttm_io import rttm_read
import numpy as np
from argparse import ArgumentParser
from pre_process import rttm_read_cder

def main():
    parser = ArgumentParser(
        description='Score diarization from RTTM files.', add_help=True,
        usage='%(prog)s [options]')
    parser.add_argument('-s', dest='sys_rttm_fns', help='system RTTM files (default: %(default)s)')
    parser.add_argument('-r', dest='ref_rttm_fns', help='reference RTTM files (default: %(default)s)')
    args = parser.parse_args()

    ref = rttm_read_cder(args.ref_rttm_fns)
    hyp = rttm_read_cder(args.sys_rttm_fns)

    CSSDER = CSSDErrorRate()
    results = []

    for key, val in ref.items():
        hypothesis = val[1]
        # if b key
        reference = hyp[key][1]

        result = CSSDER(reference, hypothesis)
        print(key, "CSSDER = {0:.3f}".format(result))
        results.append(result)

    print("Avg CSSDER : {0:.3f}", np.mean(results))


if __name__ == "__main__":
    main()