class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = []
        for i in range(numRows):
            row = [1]
            if i > 0:
                prev_row = triangle[i - 1]
                for j in range(1, i):
                    row.append(prev_row[j - 1] + prev_row[j])
                row.append(1)
            triangle.append(row)
        return triangle
