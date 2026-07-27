# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.arr=nums
        return self.help(0,len(nums)-1)
    def help(self,l,r):
        if l>r:
            return
        mid=(l+r)//2
        root=TreeNode(self.arr[mid])
        root.left=self.help(l,mid-1)
        root.right=self.help(mid+1,r)
        return root 