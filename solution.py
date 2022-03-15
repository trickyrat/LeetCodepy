from math import inf
from typing import List
import re

from collections import Counter


class ListNode:
    """
    Definition fro singly-linked list.
    """

    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        super().__init__()

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1.Two sum
        """
        size = len(nums)
        for i in range(size):
            for j in range(i + 1, size):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        2.Add two Numbers
        """
        carry = 0
        dummy_head: ListNode = ListNode(0, None)
        curr: ListNode = dummy_head
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            curr.next = ListNode(sum % 10, None)
            curr = curr.next
            carry = sum // 10
            if carry != 0:
                curr.next = ListNode(carry, None)
        return dummy_head.next

    def longestSubstringWithoutRepeat(self, s: str) -> int:
        """
        3.Longest substring without repeat
        """
        size = len(s)
        i = ans = 0
        index = [0] * 128
        for j in range(0, size):
            i = max(index[ord(s[j])], i)
            ans = max(ans, j - i + 1)
            index[ord(s[j])] = j + 1
        return ans

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        4 Median of Two Sorted Arrays
        """

        def getKthElement(k):
            index1, index2 = 0, 0
            while True:
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (
                           getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)
                   ) / 2

    def longestPalindrome(self, s: str) -> str:
        """
        5.Longest Palindromic Substring
        """
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        begin = 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for L in range(2, n + 1):
            for i in range(n):
                j = L + i - 1
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin: begin + max_len]

    def zconvert(self, s: str, numRows: int) -> str:
        """
        6 z字形转换
        """
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 - 2
        ans = []
        for i in range(r):
            for j in range(0, n - i, t):
                ans.append(s[j + i])
                if 0 < i < r - 1 and j + t - i < n:
                    ans.append(s[j + t - i])
        return "".join(ans)

    def reverseInt(self, x: int) -> int:
        """
        7 整数反转
        """
        res = 0
        INT_MIN, INT_MAX = -(2 ** 31), 2 ** 31 - 1
        while x != 0:
            if res < INT_MIN // 10 + 1 or res > INT_MAX // 10:
                return 0
            digit = x % 10
            if x < 0 and digit > 0:
                digit -= 10
            x = (x - digit) // 10
            res = res * 10 + digit
        return res

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        27 Remove Element
        """
        slow = 0
        for item in nums:
            if item != val:
                nums[slow] = item
                slow += 1
        return slow

    def search(self, nums: List[int], target: int) -> int:
        """
        33 Search in Rotated Sorted Array
        """
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1
        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[n - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    def search_insert(self, nums: List[int], target: int):
        """
        35.Search Insert Position
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left + 1 if nums[left] < target else left

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        74 Search in 2D Matrix
        """
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1
        while l <= r:
            mid = l + (r - l) // 2
            x = matrix[mid // n][mid % n]
            if x > target:
                r = mid - 1
            elif x < target:
                l = mid + 1
            else:
                return True
        return False

    def pathSum(self, root: TreeNode, targetNum: int) -> List[List[int]]:
        """
        113 路径总和
        """
        ret = list()
        path = list()

        def dfs(root: TreeNode, targetNum: int):
            if not root:
                return
            path.append(root.val)
            targetNum -= root.val
            if not root.left and not root.right and targetNum == 0:
                ret.append(path[:])
            dfs(root.left, targetNum)
            dfs(root.right, targetNum)
            path.pop()

        dfs(root, targetNum)
        return ret

    def twoSumII(self, numbers: List[int], target: int) -> List[int]:
        """
        167 Two Sum II - Input array is sorted
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]

    def rotate(self, nums: List[int], k: int) -> None:
        """
        189 Rotate Array
        """

        # def reverse(nums: List[int], start: int, end: int):
        #     while start < end:
        #         nums[start], nums[end] = nums[end], nums[start]
        #         start += 1
        #         end -= 1

        # size = len(nums)
        # k %= size
        # reverse(nums, 0, size - 1)
        # reverse(nums, 0, k - 1)
        # reverse(nums, k, size - 1)
        def gcd(x: int, y: int) -> int:
            return gcd(y, x % y) if y else x

        n = len(nums)
        k = k % n
        count = gcd(k, n)
        for start in range(0, count):
            current = start
            prev = nums[start]
            while True:
                next = (current + k) % n
                nums[next], prev = prev, nums[next]
                current = next
                if start == current:
                    break

    def calculate(self, s: str) -> int:
        """
        224.Basic Calculator
        """
        ops = [1]
        i = 0
        n = len(s)
        ret = 0
        sign = 1
        while i < n:
            if s[i] == " ":
                i += 1
            elif s[i] == "+":
                sign = ops[-1]
                i += 1
            elif s[i] == "-":
                sign = -ops[-1]
                i += 1
            elif s[i] == "(":
                ops.append(sign)
                i += 1
            elif s[i] == ")":
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord("0")
                    i += 1
                ret += num * sign
        return ret

    def moveZeroes(self, nums: List[int]) -> None:
        """
        283 Move Zeroes
        """
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

    def search_v1(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

    def search_v2(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return -1

    def getSum(self, a: int, b: int) -> int:
        """
        371.Sum of Two Integers
        """
        MASK1 = 4294967296  # 2^32
        MASK2 = 2147483648  # 2^31
        MASK3 = 2147483647  # 2^31-1
        while b != 0:
            carry = ((a & b) << 1) % MASK1
            a = (a ^ b) % MASK1
            b = carry
        if a & MASK2:  # 负数
            return ~((a ^ MASK2) ^ MASK3)
        else:
            return a

    def validUtf8(self, data: List[int]) -> bool:
        """
        393 UTF-8编码验证
        """
        n = 0
        for i in range(0, len(data)):
            if n > 0:
                if data[i] >> 6 != 2:
                    return False;
                n -= 1
            elif data[i] >> 7 == 0:
                n = 0
            elif data[i] >> 5 == 0b110:
                n = 1
            elif data[i] >> 4 == 0b1110:
                n = 2
            elif data[i] >> 5 == 0b11110:
                n = 3
            else:
                return False
        return n == 0

    def countSegment(self, s: str) -> int:
        """
        434 Number of Segments in a String
        """
        segmentCount = 0
        for i in range(0, len(s)):
            if (i == 0 or s[i - 1] == " ") and s[i] != " ":
                segmentCount += 1
        return segmentCount

    def validIpAddress(self, IP: str) -> str:
        """
        468 Valid IP address
        """
        ipv4_chunk = r"([0-9][1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
        ipv6_chunk = r"([0-9a-fA-F]{1,4})"
        ipv4_pattern = re.compile(r"^(" + ipv4_chunk + r"\.){3}" + ipv4_chunk + r"$")
        ipv6_pattern = re.compile(r"^(" + ipv6_chunk + r"\:){7}" + ipv6_chunk + r"$")
        if "." in IP:
            return "IPv4" if ipv4_pattern.match(IP) else "Neither"
        if ":" in IP:
            return "IPv6" if ipv6_pattern.match(IP) else "Neither"
        return "Neither"

    def convertToBase7(self, num: int) -> str:
        """
        504 七进制数
        """
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        digits = []
        while num:
            digits.append(str(num % 7))
            num //= 7
        if negative:
            digits.append("-")
        return "".join(reversed(digits))

    def findLUSLength(self, a: str, b: str) -> int:
        """
        521 最长特殊序列
        """
        return -1 if a == b else max(len(a), len(b))

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """
        537 Complex Number Multiply
        """
        real1, imag1 = map(int, num1[:-1].split("+"))
        real2, imag2 = map(int, num2[:-1].split("+"))
        return f"{real1 * real2 - imag1 * imag2}+{real1 * imag2 + imag1 * real2}i"

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        547 Number of Provinces
        """

        def dfs(i: int):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        provinces = len(isConnected)
        visited: set = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circles += 1
        return circles

    def optimalDivision(self, nums: List[int]) -> str:
        """
        553 最优除法
        """
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        return str(nums[0]) + "/(" + "/".join(map(str, nums[1:])) + ")"

    def preorder(self, root: Node) -> List[int]:
        """
        589 N叉树的前序遍历
        """
        ans = []

        def dfs(node: Node):
            if node is None:
                return None
            ans.append(node.val)
            for ch in node.children:
                dfs(ch)

        dfs(root)
        return ans

    def postorder(self, root: Node) -> List[int]:
        """
        590 N叉树的后序遍历
        """
        ans = []

        def dfs(node: Node):
            if node is None:
                return
            for ch in node.children:
                dfs(ch)
            ans.append(node.val)

        dfs(root)
        return ans

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        599.两个列表的最小索引和
        """
        index = {s: i for i, s in enumerate(list1)}
        ans = []
        indexSum = inf
        for i, s in enumerate(list2):
            if s in index:
                j = index[s]
                if i + j < indexSum:
                    indexSum = i + j
                    ans = [s]
                elif i + j == indexSum:
                    ans.append(s)
        return ans


    def backspaceCompare(self, s: str, t: str) -> bool:
        """ "
        844 Backspace String Compare
        """
        i = len(s) - 1
        j = len(t) - 1
        skipS = skipT = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            else:
                if i >= 0 or j >= 0:
                    return False
            i -= 1
            j -= 1
        return True

    def middleNode(self, head: ListNode) -> ListNode:
        """
        876 Middle of the Linked List
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        977 Squares of a Sorted Array
        """
        n = len(nums)
        ans = [0] * n
        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if nums[i] * nums[i] > nums[j] * nums[j]:
                ans[pos] = nums[i] * nums[i]
                i += 1
            else:
                ans[pos] = nums[j] * nums[j]
                j -= 1
            pos -= 1
        return ans

    def modifyString(self, s: str) -> str:
        """
        1576 替换所有的问号
        """
        n = len(s)
        arr = list(s)
        for i in range(n):
            if arr[i] == "?":
                for ch in "abc":
                    if not (
                            i > 0 and arr[i - 1] == ch or i < n - 1 and arr[i + 1] == ch
                    ):
                        arr[i] = ch
                        break
        return "".join(arr)

    def pivotIndex(self, nums: List[int]) -> int:
        """
        1991 寻找数组的中间位置
        """
        total = sum(nums)
        sum_tmp = 0
        for i, num in enumerate(nums):
            if 2 * sum_tmp + num == total:
                return i
            sum_tmp += num
        return -1

    def countKDifference(self, nums: List[int], k: int) -> int:
        """
        2006 差值绝对值为k的数对数目
        """
        res = 0
        cnt = Counter()
        for num in nums:
            res += cnt[num - k] + cnt[num + k]
            cnt[num] += 1
        return res

    def maximumDifference(self, nums: List[int]) -> int:
        """
        2016 增量元素之间的最大差值
        """
        n = len(nums)
        ans, premin = -1, nums[0]
        for i in range(1, n):
            if nums[i] > premin:
                ans = max(ans, nums[i] - premin)
            else:
                premin = nums[i]
        return ans

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        """
        2044 统计按位或能得到最大值的子集数目
        """
        maxOr, cnt = 0, 0
        def dfs(pos: int, orVal: int) -> None:
            if pos == len(nums):
                nonlocal maxOr, cnt
                if orVal > maxOr:
                    maxOr, cnt = orVal, 1
                elif orVal == maxOr:
                    cnt += 1
                return
            dfs(pos + 1, orVal | nums[pos])
            dfs(pos + 1, orVal)
        dfs(0, 0)
        return cnt

    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        2055 蜡烛之间的盘子
        """
        n = len(s)
        preSum, sum = [0] * n, 0
        left, l = [0] * n, -1
        for i, ch in enumerate(s):
            if ch == "*":
                sum += 1
            else:
                l = i
            preSum[i] = sum
            left[i] = l
        right, r = [0] * n, -1
        for i in range(n - 1, -1, -1):
            if s[i] == "|":
                r = i
            right[i] = r
        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            x, y = right[x], left[y]
            if x >= 0 and y >= 0 and x < y:
                ans[i] = preSum[y] - preSum[x]
        return ans
