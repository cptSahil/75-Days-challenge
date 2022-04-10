class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        flag = [False]*len(transactions)
        for i,j in enumerate(transactions):
            n,t,a,c = j.split(",")
            if int(a)>1000:
                flag[i]=True
            for ii in range(i+1,len(transactions)):
                nn,tt,aa,cc = transactions[ii].split(",")
                if n==nn and abs(int(t)-int(tt))<=60 and c!=cc: flag[i]=flag[ii]=True
        return [t for t, f in zip(transactions,flag) if f]
    