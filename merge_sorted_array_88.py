def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    for i in range(n):
        nums1.pop(-1)
        nums1.insert(0, nums2[i])

    nums1.sort()


if __name__ == "__main__":
    nums1: list[int] = [1, 2, 3, 0, 0, 0]

    merge(nums1, 3, [2, 5, 6], 3)

    print(nums1)
