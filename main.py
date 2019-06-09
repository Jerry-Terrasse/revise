#coding=utf-8

# Split a sentense by JieBa:
#   https://github.com/fxsjy/jieba

import jieba as jb
import random as rdm


file=open("materials.txt",'r',encoding='utf-8')
data=file.read().split('\n')
file.close()
cnt=int()
scr=int()


if __name__=='__main__':
    while True:
        ln=rdm.sample(data,1)[0]
        ln=jb.lcut(ln)
        blk=''
        while len(blk)<2:
            blk=rdm.sample(ln,1)[0]
        ln[ln.index(blk)]='？'*len(blk)
        ans=input(''.join(ln)+"\n-->")
        if ans=='exit':
            print("You win %d of %d" % (scr,cnt))
            exit()
        if ans==blk:
            print("RIGHT")
            scr+=1
        else:
            print("WRONG  the answer is",blk)
        cnt+=1
