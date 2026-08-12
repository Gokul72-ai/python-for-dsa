"""
01 - Repository Structure Overview
===================================

Overview of the DSA Python repository structure and organization.

This module provides information about the repository layout and learning path.
"""


def print_repository_structure():
    """Print the complete repository structure"""
    structure = """
📁 DSA_Python/
├── basic/
│   ├── 00_repository_overview/        - Repository documentation
│   ├── 01_arrays_basic_operations/    - Array fundamentals
│   ├── 02_arrays_searching/           - Search algorithms
│   ├── 03_arrays_sorting/             - Sorting algorithms
│   ├── 04_singly_linked_list/         - Singly linked lists
│   ├── 05_doubly_linked_list/         - Doubly linked lists
│   ├── 06_circular_linked_list/       - Circular linked lists
│   ├── 07_stack_implementation/       - Stack implementations
│   ├── 08_queue_implementation/       - Queue implementations
│   ├── 09_deque_implementation/       - Deque implementations
│   ├── 10_binary_tree/                - Binary tree basics
│   ├── 11_binary_search_tree/         - BST operations
│   ├── 12_tree_traversals/            - Tree traversals
│   ├── 13_avl_tree/                   - AVL tree implementation
│   ├── 14_hash_table_implementation/  - Hash tables
│   ├── 15_heap_implementation/        - Heap data structure
│   ├── 16_graph_implementation/       - Graph algorithms
│   └── 17_dynamic_programming/        - DP techniques
└── pattrns/
    ├── 01_two_pointers.py
    ├── 02_sliding_window.py
    └── ... (algorithm patterns)
    """
    print(structure)


def main():
    """Main function to demonstrate repository structure"""
    print("=== DSA Python Repository Structure ===")
    print_repository_structure()


if __name__ == "__main__":
    main()
