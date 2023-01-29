import os
import sys
import json
import numpy
import argparse
import datetime


def editDistance(r, h):

    d = numpy.zeros((len(r)+1)*(len(h)+1), dtype=numpy.uint8).reshape((len(r)+1, len(h)+1))
    for i in range(len(r)+1):
        d[i][0] = i
    for j in range(len(h)+1):
        d[0][j] = j
    for i in range(1, len(r)+1):
        for j in range(1, len(h)+1):
            if r[i-1] == h[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                substitute = d[i-1][j-1] + 1
                insert = d[i][j-1] + 1
                delete = d[i-1][j] + 1
                d[i][j] = min(substitute, insert, delete)
    return d

def wer(r, h):

    # build the matrix
    d = editDistance(r, h)

    # print the result in aligned way
    result = float(d[len(r)][len(h)]) / len(r) * 100
    return result
    
def evaluate(label_path, prediction_path) :
    
    import pandas as pd
    
    pred_df = pd.read_csv(prediction_path)
    gt_df = pd.read_csv(label_path)

    total_wer = 0
    pub_cnt = 0
    p_total_wer = 0
    pri_cnt = 0
   
    for i, gt in gt_df.iterrows(): # for each file
        pred = pred_df.loc[pred_df['file_name'] == gt['file_name']]
        pred = pred.iloc[0]
        
        wer_val = wer(str(gt['text']).split(), str(pred['text']).split())
        if gt['public'] == True:
            total_wer += wer_val
            pub_cnt += 1
        else:
            p_total_wer += wer_val
            pri_cnt += 1
            
    ret = total_wer / pub_cnt
    p_ret = p_total_wer / pri_cnt
    return ret, p_ret

def evaluation_metrics(label_path, prediction_path):
    return evaluate(label_path, prediction_path)


if __name__ == '__main__':
    answer = sys.argv[1]
    pred = sys.argv[2]
    
    try:
        import time
        start = time.time()
        score, pScore = evaluation_metrics(answer, pred)
        score = 0.3*score + 0.7*pScore
        print(f'score={score},pScore={pScore}')
        print(f'Elapsed Time: {time.time() - start}')

    except Exception as e:
        print(f'evaluation exception error: {e}', file=sys.stderr)
        sys.exit()
