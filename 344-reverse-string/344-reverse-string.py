class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # solution 1 
        # we can do in place 
        # keep swapping thee elements on the array 
        
      #  l, r = 0, len(s) - 1
      #  while l < r:
      #      s[l], s[r] = s[r], s[l]
      #      l, r = l + 1, r - 1
        
    # Recusion O(n)
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l+1, r - 1)
        reverse(0, len(s) - 1)