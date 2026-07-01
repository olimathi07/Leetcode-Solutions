class Solution:
    def reformatDate(self, date: str) -> str:
        [d,m,y]=date.split(' ')
        dic= ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        return y+'-'+str(dic.index(m)+1).zfill(2)+'-'+d[:-2].zfill(2)