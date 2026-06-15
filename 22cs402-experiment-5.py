class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def build(self, index, start, end):
        if start == end:
            self.tree[index] = self.arr[start]
            return

        mid = (start + end) // 2

        self.build(2 * index + 1, start, mid)
        self.build(2 * index + 2, mid + 1, end)

        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def query_range_sum(self, left, right):
        return self.query(0, 0, self.n - 1, left, right)

    def query(self, index, start, end, left, right):
        # Complete overlap
        if left <= start and right >= end:
            return self.tree[index]

        # No overlap
        if right < start or left > end:
            return 0

        # Partial overlap
        mid = (start + end) // 2

        return self.query(2 * index + 1, start, mid, left, right) + \
               self.query(2 * index + 2, mid + 1, end, left, right)

    def update_value(self, pos, new_value):
        self.arr[pos] = new_value
        self.update(0, 0, self.n - 1, pos, new_value)

    def update(self, index, start, end, pos, value):
        if start == end:
            self.tree[index] = value
            return

        mid = (start + end) // 2

        if pos <= mid:
            self.update(2 * index + 1, start, mid, pos, value)
        else:
            self.update(2 * index + 2, mid + 1, end, pos, value)

        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]


# Main Program
arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))

segment_tree = SegmentTree(arr)

print("Initial segment tree:", segment_tree.tree[:2 * len(arr)])

query_start, query_end = map(
    int,
    input("Enter the query range (start end) separated by spaces: ").split()
)

print(
    f"Sum of elements in range [{query_start}, {query_end}]:",
    segment_tree.query_range_sum(query_start, query_end)
)

student_index, new_value = map(
    int,
    input("Enter the student index and new value separated by spaces: ").split()
)

segment_tree.update_value(student_index, new_value)

print(
    f"Segment tree after updating value of student {student_index}:",
    segment_tree.tree[:2 * len(arr)]
)

print(
    f"Sum of elements in range [{query_start}, {query_end}]:",
    segment_tree.query_range_sum(query_start, query_end)
)