def max_connected_component(t, test_cases):
    def dfs(r, c):
        if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] != '#':
            return 0
        grid[r][c] = '.'  # Mark the cell as visited
        size = 1
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            size += dfs(r + dr, c + dc)
        return size

    results = []
    for _ in range(t):
        n, m = test_cases[_]['size']
        grid = test_cases[_]['grid']
        
        row_count = [0] * n
        col_count = [0] * m
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '#':
                    row_count[i] += 1
                    col_count[j] += 1
        
        max_size = 0
        for i in range(n):
            for j in range(m):
                max_size = max(max_size, row_count[i] + col_count[j] - (grid[i][j] == '#'))
        
        results.append(max_size)
    
    return results

# Example Usage
t = 2
test_cases = [
    {'size': (3, 4), 'grid': [['#', '.', '.', '#'], ['.', '.', '#', '#'], ['#', '.', '.', '#']]},
    {'size': (2, 3), 'grid': [['#', '.', '.'], ['.', '.', '#']]}
]

results = max_connected_component(t, test_cases)
for result in results:
    print(result)
