# CSSD-Metric (Conversational Short-phrase Speaker Diarization Metric)

***
## Usage

Both the reference and hypothesis(system) should be saved in RTTM (Rich Transcription Time Marked) format.

```bash
python3 score.py -s hypothesis_rttm_path -r reference_rttm_path
```

***
## Reference Paper

[1] NIST. (2009). The 2009 (RT-09) Rich Transcription Meeting Recognition Evaluation Plan. https://web.archive.org/web/20100606041157if_/http://www.itl.nist.gov/iad/mig/tests/rt/2009/docs/rt09-meeting-eval-plan-v2.pdf

[2] Ryant, N., Church, K., Cieri, C., Du, J., Ganapathy, S. and Liberman, M., 2020. Third DIHARD challenge evaluation plan. arXiv preprint arXiv:2006.05815.

