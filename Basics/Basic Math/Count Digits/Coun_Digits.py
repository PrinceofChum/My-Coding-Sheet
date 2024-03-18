#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        c=0
        origN=N
        while N!=0:
            rem=N%10
            N-=rem
            N/=10
            if rem!=0 and origN%rem==0:
                c+=1
        return c
            

// add 
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends
