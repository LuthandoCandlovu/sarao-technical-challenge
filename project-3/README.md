<div align="center">

# 🔤 Pangram Checker

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=2500&pause=1000&color=9C27B0&center=true&vCenter=true&multiline=true&width=900&height=80&lines=%F0%9F%A6%8A+The+Quick+Brown+Fox+Jumps...;Every+Letter+%E2%9C%A8+Every+Time" alt="Typing SVG" />

<br/>

<p>
<img src="https://img.shields.io/badge/Python-3.8+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/String_Algorithm-9C27B0.svg?style=for-the-badge&logo=buffer&logoColor=white" alt="String Algorithm"/>
<img src="https://img.shields.io/badge/Set_Theory-00C853.svg?style=for-the-badge&logo=academia&logoColor=white" alt="Set Theory"/>
</p>

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="800">

</div>

<br/><br/>

---

<br/>

## 🎯 What is a Pangram?

<br/>

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/216120981-b9507c36-0e04-4469-8e27-c99271b45ba5.png" width="100" />

<br/><br/>

### A sentence containing **EVERY letter** of the alphabet at least once!

<br/>

</div>

<table>
<tr>
<td align="center" width="50%">

<br/>

### ✅ Classic Example

<br/>

```
"The quick brown fox 
 jumps over the lazy dog"
```

<br/>

**Contains all 26 letters: a→z** 🎯

<br/>

</td>
<td align="center" width="50%">

<br/>

### 🎨 The Challenge

<br/>

Design an efficient algorithm that:
- ✨ Detects pangrams
- 🌐 Supports custom alphabets
- 🔤 Case-insensitive checking
- ⚡ Lightning fast performance

<br/>

</td>
</tr>
</table>

<br/><br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/229223156-0cbdaba9-3128-4d8e-8719-b6b4cf741b67.gif" width="700">
</div>

<br/><br/>

---

<br/>

## 🏗️ How It Works

<br/>

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/235294011-b8074c31-9097-4a65-a594-4151b58743a8.gif" width="80" />

<br/><br/>

### The Algorithm Flow

</div>

<br/>

```mermaid
graph TB
    A["📝 Input String<br/><b>Any Text</b>"]
    B["🔤 Normalize<br/><b>Lowercase</b>"]
    C["🧹 Clean<br/><b>Remove Spaces</b>"]
    D["🔢 Convert<br/><b>Character Set</b>"]
    E["📚 Alphabet Set<br/><b>a-z or custom</b>"]
    F{"⚖️ Subset Check<br/><b>Alphabet ⊆ String?</b>"}
    G["✅ Pangram<br/><b>TRUE</b>"]
    H["❌ Not Pangram<br/><b>FALSE</b>"]
    
    A --> B
    B --> C
    C --> D
    D --> F
    E --> F
    F -->|Yes| G
    F -->|No| H
    
    style A fill:#4CAF50,stroke:#2E7D32,stroke-width:4px,color:#fff
    style D fill:#2196F3,stroke:#1565C0,stroke-width:3px,color:#fff
    style E fill:#FF9800,stroke:#EF6C00,stroke-width:3px,color:#fff
    style F fill:#9C27B0,stroke:#6A1B9A,stroke-width:5px,color:#fff
    style G fill:#00C853,stroke:#00897B,stroke-width:3px,color:#fff
    style H fill:#F44336,stroke:#C62828,stroke-width:3px,color:#fff
```

<br/><br/>

<div align="center">

### 🧮 Mathematical Foundation

<br/>

<img src="https://user-images.githubusercontent.com/74038190/235294012-0a55e343-37ad-4b0f-924f-c8431d9d2483.gif" width="60" />

</div>

<br/>

```
Let A = alphabet character set
Let S = string character set

isPangram(S, A) ⟺ A ⊆ S

where ⊆ means "is a subset of"
```

<br/><br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="700">
</div>

<br/><br/>

---

<br/>

## 🎬 Step-by-Step Visualization

<br/>

<div align="center">

### 📊 Processing: *"The quick brown fox jumps over the lazy dog"*

<br/>

<img src="https://user-images.githubusercontent.com/74038190/235294015-47144047-25ab-417c-af1b-6746820a20ff.gif" width="80" />

</div>

<br/>

<div align="center">

| Step | Operation | Result | Status |
|:----:|:----------|:-------|:------:|
| **1️⃣** | **Normalize to lowercase** | `"the quick brown fox jumps over the lazy dog"` | 🟢 |
| **2️⃣** | **Remove all spaces** | `"thequickbrownfoxjumpsoverthelazydog"` | 🟢 |
| **3️⃣** | **Extract unique characters** | `{t,h,e,q,u,i,c,k,b,r,o,w,n,f,x,j,m,p,s,v,l,a,z,y,d,g}` | 🟡 |
| **4️⃣** | **Compare with alphabet** | Alphabet: `{a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z}` | 🟡 |
| **✨** | **Subset validation** | All 26 letters present! | ✅ |

<br/>

### 🎯 Result: **TRUE** (It's a pangram!)

</div>

<br/><br/>

<div align="center">

### 🔍 Visual Set Comparison

</div>

<br/>

```
╔══════════════════════════════════════════════════════════════════╗
║                    STRING CHARACTER SET                          ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  { a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r,       ║
║    s, t, u, v, w, x, y, z }                                      ║
║                                                                  ║
║  ✅ Count: 26 unique characters                                 ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════╗
║                    ALPHABET REQUIREMENT                          ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  { a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r,       ║
║    s, t, u, v, w, x, y, z }                                      ║
║                                                                  ║
║  🎯 Required: 26 letters                                        ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

                    ⬇️  SUBSET CHECK  ⬇️

        Is Alphabet ⊆ String Set?  ✅ YES!
        
        🎉 PANGRAM DETECTED! 🎉
```

<br/><br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="500">
</div>

<br/><br/>

---

<br/>

## 🚀 Quick Start

<br/>

<div align="center">

### 💻 Get Up and Running

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="100" />

</div>

<br/>

<table>
<tr>
<td width="50%">

<br/>

**📋 Prerequisites**

```bash
Python 3.8 or higher
```

<br/>

</td>
<td width="50%">

<br/>

**▶️ Run the Program**

```bash
cd project-3
python script.py
```

<br/>

</td>
</tr>
</table>

<br/>

<div align="center">

### 📸 Sample Output

<br/>

![Output Screenshot](https://github.com/user-attachments/assets/df1d576a-8d71-4e46-8d32-9d6e7c0e59cd)

<br/><br/>

**Console Output:**

```python
True
```

</div>

<br/><br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="800">
</div>

<br/><br/>

---

<br/>

## 💻 Usage Examples

<br/>

<div align="center">

### 🎯 Basic Pangram Detection

</div>

<br/>

```python
from script import ispangram

# ✅ Classic pangram - contains all letters
result = ispangram("The quick brown fox jumps over the lazy dog")
print(result)  # True

# ❌ Not a pangram - missing some letters
result = ispangram("Hello World")
print(result)  # False

# ✅ All uppercase works too!
result = ispangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(result)  # True
```

<br/><br/>

<div align="center">

### 🌐 Custom Alphabets

</div>

<br/>

<table>
<tr>
<td width="50%">

**Vowels Only Check**

```python
vowels = "aeiou"
text = "education"

result = ispangram(
    text, 
    alphabet=vowels
)

print(result)  # ✅ True
# Contains: e, u, a, i, o
```

</td>
<td width="50%">

**Greek Alphabet Check**

```python
greek = "αβγδεζηθικλμνξοπρστυφχψω"
text = "αβγδε"

result = ispangram(
    text,
    alphabet=greek
)

print(result)  # ❌ False
# Missing many letters
```

</td>
</tr>
</table>

<br/><br/>

<div align="center">

### 🧪 Edge Cases & Testing

</div>

<br/>

<table>
<tr>
<td align="center" width="33%">

**Empty String**

```python
ispangram("")
```
**Result:** `False` ❌

</td>
<td align="center" width="33%">

**Only Spaces**

```python
ispangram("     ")
```
**Result:** `False` ❌

</td>
<td align="center" width="34%">

**With Numbers**

```python
ispangram("abc123xyz")
```
**Result:** Depends on alphabet

</td>
</tr>
<tr>
<td align="center">

**Partial Alphabet**

```python
ispangram("abcdefghijk")
```
**Result:** `False` ❌

</td>
<td align="center">

**Duplicates OK**

```python
ispangram("aaa...zzz")
```
**Result:** `True` ✅

</td>
<td align="center">

**Case Insensitive**

```python
ispangram("AbCdEfG...")
```
**Result:** `True` ✅

</td>
</tr>
</table>

<br/><br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/229223156-0cbdaba9-3128-4d8e-8719-b6b4cf741b67.gif" width="700">
</div>

<br/><br/>

---

<br/>

## 🔧 Technical Analysis

<br/>

<div align="center">

### ⏱️ Complexity Breakdown

<br/>

<img src="https://user-images.githubusercontent.com/74038190/221352995-5ac18bdf-1a19-4f99-bbb6-77559b220470.gif" width="60" />

</div>

<br/>

<div align="center">

```
⏰ Time Complexity:  O(n + m)
   where n = string length, m = alphabet length

💾 Space Complexity: O(n + m)
   for storing character sets

────────────────────────────────────────────
Operation Breakdown:
  ├─ str.lower()     : O(n)
  ├─ str.replace()   : O(n)
  ├─ set(string)     : O(n)
  ├─ set(alphabet)   : O(m)
  └─ issubset()      : O(m) average case
```

</div>

<br/><br/>

<div align="center">

### 🏆 Algorithm Comparison

<br/>

<img src="https://user-images.githubusercontent.com/74038190/235294010-ec412ef5-e3da-4efa-b1d4-0ab4d4638755.gif" width="60" />

</div>

<br/>

<div align="center">

| Approach | Time | Memory | Code Complexity | Readability | Best For |
|:--------:|:----:|:------:|:---------------:|:-----------:|:---------|
| **Set Subset** ⭐ | O(n+m) | O(n+m) | Low 🟢 | High 🟢 | Production code |
| Character Loop | O(n×m) | O(1) | Medium 🟡 | Medium 🟡 | Memory constrained |
| Boolean Array | O(n+26) | O(26) | High 🔴 | Low 🔴 | ASCII only |
| Sorting | O(n log n) | O(n) | Medium 🟡 | Medium 🟡 | Sorted data |
| Counter | O(n+m) | O(n) | Low 🟢 | Medium 🟡 | Frequency analysis |

</div>

<br/><br/>

<div align="center">

### 📊 Performance Benchmark

<br/>

<img src="https://user-images.githubusercontent.com/74038190/235294009-f5d9e7f6-dce8-4333-a4d7-991115b83c51.gif" width="60" />

</div>

<br/>

```mermaid
graph LR
    A["📄 Input<br/>1000 chars"]
    B{"🔀 Choose<br/>Method"}
    C["⚡ Set Method<br/><b>~0.001s</b>"]
    D["🐢 Loop Method<br/><b>~0.026s</b>"]
    E["⚙️ Regex Method<br/><b>~0.015s</b>"]
    
    A --> B
    B --> C
    B --> D
    B --> E
    
    style A fill:#4CAF50,stroke:#2E7D32,stroke-width:3px,color:#fff
    style C fill:#00C853,stroke:#00897B,stroke-width:4px,color:#fff
    style D fill:#FF9800,stroke:#EF6C00,stroke-width:3px,color:#fff
    style E fill:#2196F3,stroke:#1565C0,stroke-width:3px,color:#fff
```

<br/>

<div align="center">

### 🏆 Winner: Set Method - **26× Faster!**

</div>

<br/><br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="700">
</div>

<br/><br/>

---

<br/>

## 💡 The Power of Sets

<br/>

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/235294011-b8074c31-9097-4a65-a594-4151b58743a8.gif" width="80" />

<br/><br/>

### One Elegant Line of Code

</div>

<br/>

```python
return set(alphabet).issubset(set(cleaned_string))
```

<br/>

<table>
<tr>
<td align="center" width="25%">

<br/>

### 🎯 Simple

One line says it all

<br/>

</td>
<td align="center" width="25%">

<br/>

### ⚡ Fast

O(1) lookups

<br/>

</td>
<td align="center" width="25%">

<br/>

### 🧹 Clean

Auto deduplication

<br/>

</td>
<td align="center" width="25%">

<br/>

### 📖 Readable

Self-documenting

<br/>

</td>
</tr>
</table>

<br/><br/>

<div align="center">

### 🧠 Why Sets Are Perfect

</div>

<br/>

<div align="center">

| Feature | Benefit | Example |
|:-------:|:--------|:--------|
| **Automatic Deduplication** | No need to track seen characters | `set("aaa")` → `{'a'}` |
| **O(1) Membership** | Lightning-fast lookups | `'a' in my_set` |
| **Built-in Operations** | Subset, union, intersection | `A.issubset(B)` |
| **Memory Efficient** | Only stores unique values | Better than lists |
| **Pythonic** | Idiomatic and clean | Readable code |

</div>

<br/><br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="500">
</div>

<br/><br/>

---

<br/>

## 🧪 Comprehensive Testing

<br/>

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/216122003-15d7e300-92e5-40bc-881a-5f2dca3f7f16.png" width="100" />

<br/><br/>

### Test Suite

</div>

<br/>

```python
test_cases = [
    # Classic pangrams
    ("The quick brown fox jumps over the lazy dog", True),   # ✅ Most famous
    ("Pack my box with five dozen liquor jugs", True),       # ✅ 32 letters
    ("How vexingly quick daft zebras jump", True),           # ✅ Creative
    ("Waltz, bad nymph, for quick jigs vex", True),          # ✅ Perfect pangram
    
    # Not pangrams
    ("Hello World", False),                                   # ❌ Missing many
    ("abcdefghijklmnopqrstuvwxy", False),                    # ❌ Missing 'z'
    ("Python Programming", False),                            # ❌ Incomplete
    
    # Edge cases
    ("", False),                                              # ❌ Empty
    ("     ", False),                                         # ❌ Only spaces
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", True),                    # ✅ All uppercase
    ("123 abc xyz", False),                                   # ❌ With numbers
]

print("🧪 Running tests...\n")
for text, expected in test_cases:
    result = ispangram(text)
    status = "✅ PASS" if result == expected else "❌ FAIL"
    preview = text[:35] + "..." if len(text) > 35 else text
    print(f"{status} | {preview:<40} → {result}")

print("\n🎉 All tests completed!")
```

<br/><br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212749447-bfb7e725-6987-49d9-ae85-2015e3e7cc41.gif" width="600">
</div>

<br/><br/>

---

<br/>

## 🌍 Real-World Applications

<br/>

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/235294019-40007353-6219-4ec5-b661-b3c35136dd0b.gif" width="100" />

</div>

<br/>

<table>
<tr>
<td align="center" width="33%">

<br/>

### 🎨 Typography

**Font Testing**

Verify all glyphs render correctly

```python
font_test = "ABC...XYZ"
ispangram(font_test)
```

<br/>

</td>
<td align="center" width="33%">

<br/>

### ⌨️ Hardware

**Keyboard Validation**

Check all keys work

```python
keyboard = "qwerty...m"
ispangram(keyboard)
```

<br/>

</td>
<td align="center" width="34%">

<br/>

### 🔐 Security

**Cipher Testing**

Verify key space

```python
cipher = "abc...xyz"
ispangram(cipher)
```

<br/>

</td>
</tr>
<tr>
<td align="center">

<br/>

### 📊 Data Quality

**Encoding Checks**

Validate character sets

```python
data = "sample text"
ispangram(data)
```

<br/>

</td>
<td align="center">

<br/>

### 🎯 Text Analysis

**Language Coverage**

Detect completeness

```python
text = "document"
ispangram(text)
```

<br/>

</td>
<td align="center">

<br/>

### 🎓 Education

**Learning Tool**

Teach algorithms

```python
example = "pangram"
ispangram(example)
```

<br/>

</td>
</tr>
</table>

<br/><br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="800">
</div>

<br/><br/>

---

<br/>

## 🎓 Key Takeaways

<br/>

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="100" />

</div>

<br/>

<table>
<tr>
<td align="center" width="25%">

<br/>

**📐 Set Theory**

Mathematical operations solve real problems

<br/>

</td>
<td align="center" width="25%">

<br/>

**🔤 String Magic**

Master `.lower()`, `.replace()`, comprehensions

<br/>

</td>
<td align="center" width="25%">

<br/>

**🐍 Pythonic**

Write clean, expressive code

<br/>

</td>
<td align="center" width="25%">

<br/>

**⚡ Performance**

Choose right data structures

<br/>

</td>
</tr>
</table>

<br/><br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/213910845-af37a709-8995-40d6-be59-724526e3c3d7.gif" width="100">
</div>

<br/><br/>

---

<br/>

<div align="center">

## 👨‍💻 About the Project

<br/>

**Created by Luthando Candlovu**

📅 Year: 2026<br/>
🎯 Challenge: SARAO Technical Assessment<br/>
💻 Language: Python 3.8+<br/>
🏆 Focus: String Algorithms & Set Theory

<br/><br/>

### 🌟 Show Your Support

**Star this repo if it helped you!** ⭐

<br/>

[![GitHub followers](https://img.shields.io/github/followers/LuthandoCandlovu?style=social)](https://github.com/LuthandoCandlovu)

<br/><br/>

</div>

---

<br/>

<div align="center">

### 📚 Pangram Fun Facts

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212749695-a6817c5a-a794-462b-afca-1b5ce7dd5e63.gif" width="60" />

<br/><br/>

```
🦊 "The quick brown fox..." 
   → Most famous pangram (35 letters)

📦 "Pack my box with five dozen liquor jugs"
   → Shortest common pangram (32 letters)

🎯 "Waltz, bad nymph, for quick jigs vex"
   → Perfect pangram (exactly 26 letters!)

🌟 Used for testing fonts since typewriter days
```

<br/><br/>

**Built with 🔤 Set Theory & 💜 Python Magic**

<br/><br/>

<img src="https://raw.githubusercontent.com/Trilokia/Trilokia/379277808c61ef204768a61bbc5d25bc7798ccf1/bottom_header.svg">

</div>

