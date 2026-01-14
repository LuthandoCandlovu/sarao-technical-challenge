<div align="center">

# 🎯 PROJECT 1: WORD FREQUENCY COUNTER

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=28&duration=2500&pause=1000&color=00D9FF&center=true&vCenter=true&multiline=true&width=800&height=80&lines=Real-Time+Word+Frequency+Analysis+%F0%9F%9A%80;OOP+Design+%7C+Python+3.8%2B+%F0%9F%90%8D;Efficient+%26+Scalable+Solution+%E2%9A%A1" alt="Typing SVG" />

![Python](https://img.shields.io/badge/Python-3.8+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Design-OOP-00D9FF.svg?style=for-the-badge&logo=code&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-00C853.svg?style=for-the-badge&logo=checkmarx&logoColor=white)
<<<<<<< HEAD
![Performance](<https://img.shields.io/badge/Performance-O(1)_Insert-FF6B6B.svg?style=for-the-badge>)
=======
![Performance](https://img.shields.io/badge/Performance-O(1)_Insert-FF6B6B.svg?style=for-the-badge)
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="800">

**✨ A powerful, object-oriented word frequency analyzer that processes text streams in real-time ✨**

[🎯 Problem](#-problem-statement) • [🏗️ Architecture](#️-architecture) • [💡 Solution](#-solution-overview) • [🚀 Quick Start](#-quick-start) • [💻 Usage](#-usage-example)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=header" width="100%"/>

</div>

---

## 🎯 Problem Statement

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=20&pause=1000&color=F7B801&center=true&vCenter=true&width=700&lines=Design+an+Intelligent+Word+Processing+System!" alt="Challenge" />

</div>

<details open>
<summary><b>📖 Click to expand the challenge</b></summary>

<br>

> 🎯 Design an **object-oriented solution** that processes a **stream of words** and maintains a **real-time count** of the most frequently occurring words. The system must support configurable top-N retrieval and efficient word-by-word updates.

### 🔑 Key Requirements:

```diff
+ ✅ Process words one at a time (streaming capability)
+ ✅ Maintain frequency counts in real-time
+ ✅ Return top N most frequent words
+ ✅ Case-insensitive processing
+ ✅ Object-oriented design
+ ✅ Efficient memory usage
```

</details>

---

## 🏗️ Architecture

<div align="center">

### 🔄 System Flow Diagram

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&pause=1000&color=4CAF50&center=true&vCenter=true&width=500&lines=Visualizing+the+Data+Pipeline+%F0%9F%93%8A" alt="Architecture" />

</div>

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

    style B fill:#4CAF50,stroke:#fff,stroke-width:3px,color:#fff
    style F fill:#2196F3,stroke:#fff,stroke-width:2px,color:#fff
    style I fill:#FF9800,stroke:#fff,stroke-width:2px,color:#fff
<<<<<<< HEAD

    classDef inputStyle fill:#9C27B0,stroke:#fff,stroke-width:2px,color:#fff
    classDef processStyle fill:#00BCD4,stroke:#fff,stroke-width:2px,color:#fff

=======
    
    classDef inputStyle fill:#9C27B0,stroke:#fff,stroke-width:2px,color:#fff
    classDef processStyle fill:#00BCD4,stroke:#fff,stroke-width:2px,color:#fff
    
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
    class A inputStyle
    class C,D,E,G,H processStyle
```

<div align="center">

### 🎨 Class Structure

</div>

```
┌───────────────────────────────────────────────────────────┐
│           📦 WordFrequencyCounter Class                   │
├───────────────────────────────────────────────────────────┤
│                                                           │
│  🔧 Attributes:                                           │
│     └─ word_counts: defaultdict(int)                     │
│     └─ n: int (default: 10)                              │
│                                                           │
│  ⚙️ Methods:                                              │
│     ├─ __init__(n: int = 10) → None                      │
│     ├─ process_word(word: str) → None                    │
│     └─ top_n_words() → List[Tuple[str, int]]             │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

---

## 💡 Solution Overview

<table>
<tr>
<td width="50%" valign="top">

### ✨ Key Features

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="30"> **Encapsulation**
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
- Internal word counts managed within the class
- Private state protection

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="30"> **Configurability**
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
- Customizable `n` parameter (default: 10)
- Flexible retrieval options

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="30"> **Efficiency**
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
- O(1) word insertion
- O(n log n) retrieval

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="30"> **Scalability**
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
- Can process unlimited word streams
- Memory-efficient storage

</td>
<td width="50%" valign="top">

### 🧩 Core Components

<div align="center">

<<<<<<< HEAD
|     Component     | Purpose            |   Complexity   |
| :---------------: | :----------------- | :------------: |
|   🎯 `__init__`   | Initialize counter |    **O(1)**    |
| ⚡ `process_word` | Count words        |    **O(1)**    |
| 🏆 `top_n_words`  | Retrieve top N     | **O(n log n)** |
=======
| Component | Purpose | Complexity |
|:---------:|:--------|:----------:|
| 🎯 `__init__` | Initialize counter | **O(1)** |
| ⚡ `process_word` | Count words | **O(1)** |
| 🏆 `top_n_words` | Retrieve top N | **O(n log n)** |
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a

</div>

### 📊 Performance Metrics

```yaml
Memory Usage: O(m) unique words
Insert Speed: Constant time O(1)
Retrieval: Logarithmic O(n log n)
Thread Safety: Not implemented
```

</td>
</tr>
</table>

<div align="center">

![Divider](https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,20,6&height=2)

</div>

---

## 🔄 Data Flow Visualization

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&color=FF6B6B&center=true&vCenter=true&width=600&lines=Watch+the+Magic+Happen!+%F0%9F%AA%84" alt="Flow" />

</div>

```
🌊 Input Stream: ["the", "quick", "brown", "fox", "the", "fox"]
            ┃
            ┃  Step 1
            ▼
        🔵 process_word("the")
            │
            ├─ Normalize: "the" → "the"
            ├─ Update: word_counts["the"] = 1
            └─ State: {"the": 1}
            ┃
            ┃  Step 2
            ▼
        🔵 process_word("quick")
            │
            ├─ Normalize: "quick" → "quick"
            ├─ Update: word_counts["quick"] = 1
            └─ State: {"the": 1, "quick": 1}
            ┃
            ┃  Step 3
            ▼
        🔵 process_word("brown")
            │
            └─ State: {"the": 1, "quick": 1, "brown": 1}
            ┃
            ┃  Step 4
            ▼
        🔵 process_word("fox")
            │
            └─ State: {"the": 1, "quick": 1, "brown": 1, "fox": 1}
            ┃
            ┃  Step 5
            ▼
        🔵 process_word("the")
            │
            ├─ Update: word_counts["the"] = 2
            └─ State: {"the": 2, "quick": 1, "brown": 1, "fox": 1}
            ┃
            ┃  Step 6
            ▼
        🔵 process_word("fox")
            │
            ├─ Update: word_counts["fox"] = 2
            └─ State: {"the": 2, "quick": 1, "brown": 1, "fox": 2}
            ┃
            ┃  Final Step
            ▼
        ✨ top_n_words(2)
            │
            ├─ Sort by frequency (descending)
            ├─ Return top 2 results
            └─ Output: [("the", 2), ("fox", 2)]
            ┃
            ▼
        🎉 SUCCESS!
```

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="200">
</div>

---

## 🚀 Quick Start

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=20&pause=1000&color=00C853&center=true&vCenter=true&width=500&lines=Get+Started+in+3+Easy+Steps!+%F0%9F%9A%80" alt="Quick Start" />

</div>

<details>
<summary><b>📋 Step 1: Prerequisites</b></summary>

<br>

```bash
✅ Python 3.8 or higher
✅ No external dependencies needed!
```

Check your Python version:
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
```bash
python3 --version
```

</details>

<details open>
<summary><b>▶️ Step 2: Run the Project</b></summary>

<br>

Navigate to the project directory:
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
```bash
cd project-1
```

Execute the script:
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
```bash
python3 script.py
```

Or make it executable and run directly:
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
```bash
chmod +x script.py
./script.py
```

</details>

<details>
<summary><b>📤 Step 3: Expected Output</b></summary>

<br>

You should see output similar to this:

```python
<<<<<<< HEAD
[('the', 3), ('fox', 2), ('quick', 2), ('brown', 1),
=======
[('the', 3), ('fox', 2), ('quick', 2), ('brown', 1), 
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
 ('jumps', 1), ('over', 1), ('lazy', 1), ('dog', 1), ('was', 1)]
```

<div align="center">

![Success](https://img.shields.io/badge/✓-Success-00C853?style=for-the-badge&labelColor=black)

</div>

</details>

---

## 💻 Usage Example

<div align="center">

### 🎮 Interactive Code Demo

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&pause=1000&color=2196F3&center=true&vCenter=true&width=500&lines=Try+It+Yourself!+%F0%9F%92%BB" alt="Usage" />

</div>

```python
# 📦 Import the class
from script import WordFrequencyCounter

# 🎯 Initialize with top-5 configuration
counter = WordFrequencyCounter(n=5)

# 📝 Process words from any text source
text = "hello world hello python world world programming python"
for word in text.split():
    counter.process_word(word)

# 🏆 Get top 5 most frequent words
results = counter.top_n_words()
print(results)

# 📊 Output:
# [('world', 3), ('hello', 2), ('python', 2), ('programming', 1)]
```

<div align="center">

### 🌟 Real-World Example

</div>

```python
# 📚 Analyze a book excerpt
book_text = """
To be or not to be that is the question
Whether tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
"""

counter = WordFrequencyCounter(n=10)

# Process each word
for word in book_text.lower().split():
    counter.process_word(word)

# Get results
top_words = counter.top_n_words()

# Display beautifully
print("\n🏆 Top 10 Most Frequent Words:\n")
for rank, (word, count) in enumerate(top_words, 1):
    print(f"  {rank}. {word:15} → {count} occurrence(s)")
```

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="600">
</div>

---

## 🔧 Technical Deep Dive

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&color=9C27B0&center=true&vCenter=true&width=600&lines=Under+the+Hood+%F0%9F%94%A7" alt="Technical" />

</div>

### 🤔 Why `defaultdict`?

<table>
<tr>
<td align="center" width="33%">

### ✅ Auto-Initialize
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
No need to check if key exists

```python
# ❌ Without defaultdict
if word not in counts:
    counts[word] = 0
counts[word] += 1

# ✅ With defaultdict
counts[word] += 1
```

</td>
<td align="center" width="33%">

### ✅ Cleaner Code
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
Eliminates boilerplate logic

```python
from collections import defaultdict

# Initialize with int
counts = defaultdict(int)

# Auto-creates key with 0
counts["new_word"] += 1
```

</td>
<td align="center" width="34%">

### ✅ Performance
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
Constant-time O(1) operations

```python
# Hash table lookup
# Average: O(1)
# Worst: O(n)

# But practically
# always O(1)!
```

</td>
</tr>
</table>

### ⏱️ Algorithm Complexity Analysis

<div align="center">

```
┌────────────────────────────────────────────────────────────┐
│                    COMPLEXITY ANALYSIS                     │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  📊 Space Complexity:  O(m) where m = unique words        │
│                                                            │
│  ⏰ Time Complexity:                                       │
│     ├─ process_word():   O(1) average case                │
│     │                     O(n) worst case (hash collision) │
│     │                                                      │
│     └─ top_n_words():    O(m log m) for sorting           │
│                           O(n) for getting top n          │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

</div>

### 🎨 Design Principles Applied

<div align="center">

<table>
<tr>
<th>🏛️ Principle</th>
<th>📝 Description</th>
<th>✅ Implementation</th>
</tr>
<tr>
<td><b>Single Responsibility</b></td>
<td>Class handles only word frequency counting</td>
<td>One clear purpose, one class</td>
</tr>
<tr>
<td><b>Encapsulation</b></td>
<td>Internal state hidden from external access</td>
<td>Private attributes with public methods</td>
</tr>
<tr>
<td><b>Configurability</b></td>
<td>Flexible n parameter</td>
<td>Constructor parameter with default</td>
</tr>
<tr>
<td><b>Extensibility</b></td>
<td>Easy to add filtering or stemming</td>
<td>Modular method design</td>
</tr>
</table>

</div>

---

## 📊 Performance Characteristics

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=20&pause=1000&color=FF6B6B&center=true&vCenter=true&width=500&lines=Benchmarks+%26+Performance+%F0%9F%8F%8E" alt="Performance" />

</div>

<table>
<tr>
<th>Operation</th>
<th>Best Case</th>
<th>Average Case</th>
<th>Worst Case</th>
<th>Space</th>
</tr>
<tr>
<td><b>Insert Word</b></td>
<td><code>O(1)</code> ⚡</td>
<td><code>O(1)</code> ⚡</td>
<td><code>O(n)</code> 🐌</td>
<td><code>O(1)</code></td>
</tr>
<tr>
<td><b>Get Top-N</b></td>
<td><code>O(m log m)</code> 📊</td>
<td><code>O(m log m)</code> 📊</td>
<td><code>O(m log m)</code> 📊</td>
<td><code>O(m)</code></td>
</tr>
<tr>
<td><b>Total Memory</b></td>
<td colspan="3" align="center"><code>O(m)</code> where m = unique words</td>
<td>-</td>
</tr>
</table>

<div align="center">

<<<<<<< HEAD
_m = unique words, n = total words processed_
=======
*m = unique words, n = total words processed*
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a

![Performance](https://img.shields.io/badge/Performance-Optimized-00C853?style=for-the-badge&logo=speedtest&logoColor=white)

</div>

---

## 🎓 Key Learnings

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=20&pause=1000&color=F7B801&center=true&vCenter=true&width=600&lines=Skills+Demonstrated+%F0%9F%8E%93" alt="Learning" />

</div>

<table>
<tr>
<td align="center" width="25%">

<img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="100">

### 🏛️ OOP Design
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
State management through encapsulation

</td>
<td align="center" width="25%">

<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="100">

### 📦 Data Structures
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
`defaultdict` for efficient counting

</td>
<td align="center" width="25%">

<img src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="100">

### 🔀 Algorithm Design
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
Lambda functions & custom sorting

</td>
<td align="center" width="25%">

<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="100">

### 📝 Best Practices
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
Type hints & documentation

</td>
</tr>
</table>

<div align="center">

```python
# 💡 Key Takeaways
takeaways = {
    "OOP": "Encapsulation provides clean interfaces",
    "Data Structures": "Choose the right tool for the job",
    "Algorithms": "Balance between time and space complexity",
    "Code Quality": "Readability and maintainability matter"
}
```

</div>

---

## 📸 Live Output Screenshot

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&color=00D9FF&center=true&vCenter=true&width=500&lines=See+It+In+Action!+%F0%9F%8E%AC" alt="Output" />

### 🎯 Real Terminal Output

<img width="1071" alt="Word Frequency Counter Output" src="https://github.com/user-attachments/assets/39a6b216-f1e0-44a5-827f-10c8cd354676" />

</div>

<div align="center">

![Output](https://img.shields.io/badge/Output-Verified-success?style=for-the-badge&logo=checkmarx&logoColor=white)
![Tested](https://img.shields.io/badge/Tested-100%25-brightgreen?style=for-the-badge&logo=pytest&logoColor=white)

</div>

---

## 🎯 Use Cases

<div align="center">

### 💼 Real-World Applications

</div>

<table>
<tr>
<td width="50%">

### 📰 Text Analysis
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
```python
# Analyze news articles
# SEO keyword extraction
# Content categorization
```

</td>
<td width="50%">

### 🔍 Search Engines
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
```python
# Index document terms
# Relevance scoring
# Query optimization
```

</td>
</tr>
<tr>
<td width="50%">

### 📊 Social Media
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
```python
# Trending hashtags
# Sentiment analysis
# Topic modeling
```

</td>
<td width="50%">

### 🤖 NLP Pipelines
<<<<<<< HEAD

=======
>>>>>>> f21489ca56be5111a317ad324164baecc8f12c8a
```python
# Feature extraction
# Text preprocessing
# Language modeling
```

</td>
</tr>
</table>

---

## 🛠️ Possible Enhancements

<details>
<summary><b>🚀 Future Improvements</b></summary>

<br>

```python
# 1️⃣ Add stop word filtering
STOP_WORDS = {'the', 'a', 'an', 'and', 'or', 'but'}

def process_word(self, word: str) -> None:
    word = word.lower()
    if word not in STOP_WORDS:
        self.word_counts[word] += 1

# 2️⃣ Add word stemming
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

def process_word(self, word: str) -> None:
    word = stemmer.stem(word.lower())
    self.word_counts[word] += 1

# 3️⃣ Add multi-threading support
from threading import Lock

def __init__(self, n: int = 10):
    self.word_counts = defaultdict(int)
    self.n = n
    self.lock = Lock()

def process_word(self, word: str) -> None:
    with self.lock:
        self.word_counts[word.lower()] += 1
```

</details>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=150&section=footer"/>

## 👨‍💻 About the Author

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=24&pause=1000&color=F70000&center=true&vCenter=true&width=600&lines=Luthando+Candlovu;Software+Engineering+Enthusiast+%F0%9F%92%BB;Problem+Solver+%7C+Code+Craftsman+%E2%9A%A1" alt="Author" />

**📅 Year:** 2026  
**🎯 Challenge:** SARAO Technical Assessment  
**💡 Focus:** Clean Code, Best Practices, OOP Design

<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="150">

---

### 🌟 Show Your Support

Give a ⭐️ if this project helped you understand word frequency analysis better!

[![GitHub](https://img.shields.io/badge/GitHub-LuthandoCandlovu-181717?style=for-the-badge&logo=github)](https://github.com/LuthandoCandlovu)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/yourprofile)

---

**Made with ❤️, ☕, and Python**

<img src="https://raw.githubusercontent.com/Trilokia/Trilokia/379277808c61ef204768a61bbc5d25bc7798ccf1/bottom_header.svg">

</div>
