<div align="center">

# 📊 Word Frequency Counter

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=4CAF50&center=true&vCenter=true&width=600&lines=Real-Time+Word+Frequency+Analysis;OOP+Design+%7C+Python+3.8%2B;Efficient+%26+Scalable+Solution" alt="Typing SVG" />

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Design-OOP-green.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-success.svg?style=for-the-badge)

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">

</div>

---

## 🎯 Problem Statement

<details open>
<summary><b>Click to expand</b></summary>

> Design an object-oriented solution that processes a **stream of words** and maintains a **real-time count** of the most frequently occurring words. The system must support configurable top-N retrieval and efficient word-by-word updates.

</details>

---

## 🏗️ Architecture

<div align="center">

```mermaid
graph TB
    A[📥 Input Text Stream] -->|Word by Word| B[🔧 WordFrequencyCounter]
    B --> C{🔄 Process Word}
    C --> D[🔤 Normalize to Lowercase]
    D --> E[➕ Update Internal Counter]
    E --> F[💾 defaultdict Storage]
    F --> G[🔍 top_n_words Method]
    G --> H[📊 Sort by Frequency]
    H --> I[✨ Return Top N Results]

    style B fill:#4CAF50,stroke:#333,stroke-width:3px,color:#fff
    style F fill:#2196F3,stroke:#333,stroke-width:2px,color:#fff
    style I fill:#FF9800,stroke:#333,stroke-width:2px,color:#fff
```

</div>

---

## 💡 Solution Overview

<table>
<tr>
<td width="50%">

### ✨ Key Features

- 🎯 **Encapsulation**: Internal word counts managed within the class
- ⚙️ **Configurability**: Customizable `n` parameter (default: 10)
- ⚡ **Efficiency**: O(1) word insertion, O(n log n) retrieval
- 📈 **Scalability**: Can process unlimited word streams

</td>
<td width="50%">

### 🧩 Key Components

| Component | Purpose | Time |
|-----------|---------|------|
| `__init__` | Initialize counter | O(1) |
| `process_word` | Count words | O(1) |
| `top_n_words` | Retrieve top N | O(n log n) |

</td>
</tr>
</table>

---

## 🔄 Data Flow Visualization

<div align="center">

```
📖 Stream: ["the", "quick", "brown", "fox", "the", "fox"]
         ↓
    🔵 process_word("the")   → {"the": 1}
         ↓
    🔵 process_word("quick") → {"the": 1, "quick": 1}
         ↓
    🔵 process_word("brown") → {"the": 1, "quick": 1, "brown": 1}
         ↓
    🔵 process_word("fox")   → {"the": 1, "quick": 1, "brown": 1, "fox": 1}
         ↓
    🔵 process_word("the")   → {"the": 2, "quick": 1, "brown": 1, "fox": 1}
         ↓
    🔵 process_word("fox")   → {"the": 2, "quick": 1, "brown": 1, "fox": 2}
         ↓
    ✅ top_n_words(2)        → [("the", 2), ("fox", 2)]
```

</div>

---

## 🚀 Quick Start

<details>
<summary><b>📋 Prerequisites</b></summary>

```bash
Python 3.8 or higher
```

</details>

<details>
<summary><b>▶️ Run the Project</b></summary>

```bash
cd project-1
python script.py
```

</details>

<details>
<summary><b>📤 Expected Output</b></summary>

```python
[('the', 3), ('fox', 2), ('quick', 2), ('brown', 1), ('jumps', 1),
 ('over', 1), ('lazy', 1), ('dog', 1), ('was', 1)]
```

</details>

---

## 💻 Usage Example

```python
from script import WordFrequencyCounter

# 🎯 Initialize with top-5 configuration
counter = WordFrequencyCounter(n=5)

# 📝 Process words from any source
text = "hello world hello python world world"
for word in text.split():
    counter.process_word(word)

# 🏆 Get top 5 most frequent words
results = counter.top_n_words()
print(results)  # [('world', 3), ('hello', 2), ('python', 1)]
```

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="600">
</div>

---

## 🔧 Technical Deep Dive

### 🤔 Why `defaultdict`?

<table>
<tr>
<td>

✅ **Automatic initialization** - No need to check if key exists

</td>
<td>

✅ **Cleaner code** - Eliminates boilerplate logic

</td>
<td>

✅ **Performance** - Constant-time operations

</td>
</tr>
</table>

### ⏱️ Algorithm Complexity

```
Space Complexity:  O(m) where m = unique words

Time Complexity:
  ├─ process_word():   O(1) average case
  └─ top_n_words():    O(m log m) for sorting
```

### 🎨 Design Principles Applied

<div align="center">

| Principle | Description |
|:---------:|:------------|
| ✅ **Single Responsibility** | Class handles only word frequency counting |
| ✅ **Encapsulation** | Internal state hidden from external access |
| ✅ **Configurability** | Flexible n parameter |
| ✅ **Extensibility** | Easy to add filtering or stemming |

</div>

---

## 🎓 Key Learnings

<table>
<tr>
<td align="center" width="25%">

### 🏛️ OOP Benefits
State management and method organization

</td>
<td align="center" width="25%">

### 📦 Data Structures
`defaultdict` for efficient counting

</td>
<td align="center" width="25%">

### 🔀 Sorting
Lambda functions for custom sort keys

</td>
<td align="center" width="25%">

### 📝 Type Hints
Better code documentation

</td>
</tr>
</table>

---

## 📊 Performance Characteristics

<div align="center">

| Operation | Best Case | Average Case | Worst Case |
|:---------:|:---------:|:------------:|:----------:|
| **Insert** | O(1) | O(1) | O(1) |
| **Retrieve Top-N** | O(n log n) | O(n log n) | O(n log n) |
| **Memory** | O(m) | O(m) | O(m) |

*where m = unique words, n = total words*

</div>

---

<div align="center">

## 📸 Sample Output

![Output Screenshot](https://github.com/user-attachments/assets/77da503b-0339-46e0-9dad-27414b5ef603)

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">

---

### 👨‍💻 Author Information

**Luthando Candlovu**  
📅 Year: 2026  
🎯 Challenge: SARAO Technical Assessment

<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="100">

---

### 🌟 Show Your Support

Give a ⭐️ if this project helped you!

[![GitHub followers](https://img.shields.io/github/followers/LuthandoCandlovu?style=social)](https://github.com/LuthandoCandlovu)

</div>

---

<div align="center">

**Made with ❤️ and Python**

<img src="https://raw.githubusercontent.com/Trilokia/Trilokia/379277808c61ef204768a61bbc5d25bc7798ccf1/bottom_header.svg">

</div>
