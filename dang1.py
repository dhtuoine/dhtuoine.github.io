from collections import deque

def bfs_step_by_step(graph, start, target):
    """
    Thực hiện thuật toán BFS từng bước, cho phép người dùng quan sát

    Args:
        graph: Đồ thị biểu diễn dưới dạng dictionary
        start: Nút bắt đầu
        target: Tập hợp các nút đích
    """

    visited = set()  #tạo 1 tập hợp rỗng để lưu lại những nut đã thăm
    queue = deque([start]) # tạo 1 hàng đợi, thêm nút bắt đầu vào hàng đợi

    while queue: # lặp đến khi hàng đợi rỗng, đã tìm thấy đích
        print("Hàng đợi:", queue)
        node = queue.popleft() #
        print("Đang xét nút:", node)

        if node in target:
            print("Tìm thấy nút đích:", node)
            return True

        if node not in visited:
            visited.add(node)
            print("Các nút đã thăm:", visited)
            for neighbor in graph[node]:
                queue.append(neighbor)
            print()
            input("Nhấn Enter để tiếp tục...")

    return False

# Ví dụ sử dụng:
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['H', 'I'],
    'C': ['E', 'F'],
    'D': ['G'],
    'E': [],
    'F': ['J', 'K'],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}

start = 'A'
target = {'I', 'E', 'K'}

if bfs_step_by_step(graph, start, target):
    print("Tìm thấy nút đích!")
else:
    print("Không tìm thấy nút đích")
