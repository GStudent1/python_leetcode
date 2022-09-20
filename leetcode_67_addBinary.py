class Solution:
    def addBinary(self, a: str, b: str):
        list_a=list("0")+list(a)
        list_b=list("0")+list(b)
        if len(list_b)-len(list_a) > 0:
            list_a=list("0") * (len(list_b)-len(list_a))+list(list_a)
        if len(list_a)-len(list_b) > 0:
            list_b=list("0") * (len(list_a)-len(list_b))+list(list_b)
        i=len(list_b)-1
        temp = 0
        list_c=["None"] * len(list_b)
        while i >= 0:
            list_c[i] = str((temp + int(list_b[i]) + int(list_a[i])) % 2)
            temp=(temp + int(list_b[i]) + int(list_a[i])) // 2
            i=i-1
        if list_c[0]=='0':
            list_c.pop(0)
        return "".join(list_c)

if __name__ == '__main__':
    a ="1010"
    b = "11"
    sol=Solution()
    list_print=sol.addBinary(a,b)
    print(list_print)