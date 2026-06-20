# Data Structures Web Applications

An interactive learning platform built with **Python (Flask + Tkinter)** to demonstrate fundamental **data structures** through real-world web applications.  
Each data structure is implemented as a standalone project with a simple UI, allowing users to **interact, visualize, and understand** how these structures work.

---

## 📚 Included Projects
1. **Arrays → Student Marks Manager**
   - Manage student marks
   - Calculate average, highest, lowest, median, pass/fail counts
   - Real-world analogy: gradebook system

2. **Stacks → Stack Visualizer**
   - Push and pop operations
   - Visualize stack growth/shrink
   - Real-world analogy: undo/redo, browser history

3. **Queues → Customer Service Queue**
   - Enqueue and dequeue customers
   - Display queue in real time
   - Real-world analogy: ticket counters, call centers

4. **Linked Lists → Playlist Manager**
   - Add, play, next, previous songs
   - Traversal through linked nodes
   - Real-world analogy: Spotify/YouTube playlists

5. **Trees → Binary Search Tree Visualizer**
   - Insert nodes into BST
   - Visualize parent-child relationships
   - Real-world analogy: file systems, organizational hierarchies

6. **Graphs → Graph Explorer**
   - Add nodes and edges
   - Force-directed visualization with D3.js
   - Real-world analogy: social networks, maps, recommendation systems

---

## 📂 Project Structure
``` D_S_ALGORITHMS/
├── D_S_ALORITHMS/
├── Array/          # Student Marks Manager
├── Stack/          # Stack Visualizer
├── Queue/          # Customer Service Queue
├── linked_list/    # Playlist Manager
├── Tree/           # BST Visualizer
├── Graphs/         # Graph Explorer
└── README.md       # Documentation (this file)
└── requirements.txt #Dependencies
```
----
## ⚙️ Installation
1. Navigate to a project folder (e.g., ARRAY/):
2. cd ARRAY
3. pip install -r requirements.txt
4. python app.py
5. http://127.0.0.1:5000

---
## Running Each App Individually

Each data structure app (Arrays, Stack, Queue, Trees, Graphs, Linked List/Playlist) is implemented as a **Flask Blueprint** so they can be combined into the main hub.  
If you want to run any app **separately**, you need to add a `main` function at the bottom of its file:

```python
if __name__ == "__main__":
    app.run(debug=True)

