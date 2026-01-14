<div align="center">

# 🔢 Number Machine

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=2500&pause=1000&color=FF6B6B&center=true&vCenter=true&multiline=true&width=900&height=80&lines=%F0%9F%94%A2+Transform+Numbers+Like+Magic;12391+%E2%86%92+19321+%E2%86%92+23402+%E2%9C%A8" alt="Typing SVG" />

<br/>

<p>
<img src="https://img.shields.io/badge/Python-3.8+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Number_Theory-FF4444.svg?style=for-the-badge&logo=hackthebox&logoColor=white" alt="Number Theory"/>
<img src="https://img.shields.io/badge/Complete-00C853.svg?style=for-the-badge&logo=checkmarx&logoColor=white" alt="Complete"/>
</p>

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="800">

</div>

<br/><br/>

---

<br/>

## 🎯 The Challenge

<br/>

<div align="center">

### ✨ Build a number manipulation system with **ZERO built-in reverse functions** ✨

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="50">

</div>

<br/>

<table>
<tr>
<td align="center" width="33%">

<img width="100" src="https://user-images.githubusercontent.com/74038190/235294011-b8074c31-9097-4a65-a594-4151b58743a8.gif" />

<br/><br/>

### 🔄 Reverse Number

**Flip the digits backwards**

Using pure mathematics

<br/>

`12391 → 19321`

</td>
<td align="center" width="33%">

<img width="100" src="https://user-images.githubusercontent.com/74038190/235294012-0a55e343-37ad-4b0f-924f-c8431d9d2483.gif" />

<br/><br/>

### ➕ Sum Digits

**Add all digits together**

Calculate the total

<br/>

`1+2+3+9+1 = 16`

</td>
<td align="center" width="34%">

<img width="100" src="https://user-images.githubusercontent.com/74038190/235294015-47144047-25ab-417c-af1b-6746820a20ff.gif" />

<br/><br/>

### ⬆️ Increment Each

**Add 1 with wrap-around**

9 becomes 0

<br/>

`12391 → 23402`

</td>
</tr>
</table>

<br/><br/>

<div align="center">

### 💫 Watch The Magic Happen

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212749447-bfb7e725-6987-49d9-ae85-2015e3e7cc41.gif" width="600">

</div>

<br/>

```diff
🎯 Input Number: 12391

+ 🔄 Reverse Operation:   12391 → 19321 ✨
+ ➕ Sum Operation:       1 + 2 + 3 + 9 + 1 = 16 ✨
+ ⬆️ Increment Operation: [1→2] [2→3] [3→4] [9→0] [1→2] = 23402 ✨
```

<br/><br/>

---

<br/>

## 🏗️ System Architecture

<br/>

<div align="center">

```mermaid
graph TB
    A["🎯 Input Number<br/><b>12391</b>"]
    B["⚙️ Number Machine<br/><b>Processing Hub</b>"]
    
    C["🔄 Reverse<br/><b>Modulo Magic</b>"]
    D["➕ Sum<br/><b>Digit Total</b>"]
    E["⬆️ Increment<br/><b>Wrap Around</b>"]
    
    F["✨ Output<br/><b>19321</b>"]
    G["✨ Output<br/><b>16</b>"]
    H["✨ Output<br/><b>23402</b>"]
    
    A --> B
    B --> C
    B --> D
    B --> E
    C --> F
    D --> G
    E --> H
    
    style A fill:#4CAF50,stroke:#2E7D32,stroke-width:4px,color:#fff,font-size:16px
    style B fill:#FF5722,stroke:#D84315,stroke-width:5px,color:#fff,font-size:16px
    style C fill:#2196F3,stroke:#1565C0,stroke-width:3px,color:#fff
    style D fill:#FF9800,stroke:#EF6C00,stroke-width:3px,color:#fff
    style E fill:#9C27B0,stroke:#6A1B9A,stroke-width:3px,color:#fff
    style F fill:#00BCD4,stroke:#0097A7,stroke-width:3px,color:#fff
    style G fill:#FFC107,stroke:#FFA000,stroke-width:3px,color:#fff
    style H fill:#E91E63,stroke:#C2185B,stroke-width:3px,color:#fff
```

</div>

<br/><br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="700">
</div>

<br/><br/>

---

<br/>

## 🔄 Algorithm Breakdown

<br/>

<div align="center">

### 🎬 Step-by-Step Reverse Animation

<br/>

<img src="https://user-images.githubusercontent.com/74038190/221352995-5ac18bdf-1a19-4f99-bbb6-77559b220470.gif" width="50">

</div>

<br/>

<div align="center">

| Step | Current `n` | Extract Digit<br/>`n % 10` | Build Reversed<br/>`rev × 10 + digit` | Remove Digit<br/>`n // 10` | Status |
|:----:|:-----------:|:-------------------------:|:-------------------------------------:|:--------------------------:|:------:|
| 1️⃣ | `12391` | `1` | `0 × 10 + 1 = 1` | `1239` | 🟢 |
| 2️⃣ | `1239` | `9` | `1 × 10 + 9 = 19` | `123` | 🟢 |
| 3️⃣ | `123` | `3` | `19 × 10 + 3 = 193` | `12` | 🟡 |
| 4️⃣ | `12` | `2` | `193 × 10 + 2 = 1932` | `1` | 🟠 |
| 5️⃣ | `1` | `1` | `1932 × 10 + 1 = 19321` | `0` | 🔴 |
| ✅ | **DONE** | — | **`19321`** | — | ✨ |

</div>

<br/><br/>

<div align="center">

### ➕ Sum of Digits Visualization

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212749695-a6817c5a-a794-462b-afca-1b5ce7dd5e63.gif" width="50">

</div>

<br/>

```
╔════════════════════════════════════════════════════════════════╗
║                     NUMBER: 12391                              ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║   Convert to String: "12391"                                   ║
║                                                                ║
║   Extract Each Digit:                                          ║
║      ┌─────┬─────┬─────┬─────┬─────┐                          ║
║      │  1  │  2  │  3  │  9  │  1  │                          ║
║      └─────┴─────┴─────┴─────┴─────┘                          ║
║                                                                ║
║   Calculate Sum:                                               ║
║      1 + 2 + 3 + 9 + 1 = 16  ✨                               ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
```

<br/><br/>

<div align="center">

### ⬆️ Increment with Wrap-Around

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212749447-bfb7e725-6987-49d9-ae85-2015e3e7cc41.gif" width="50">

</div>

<br/>

<div align="center">

| Original | Operation | Result | Effect |
|:--------:|:---------:|:------:|:------:|
| `1` | `(1 + 1) % 10` | `2` | ✅ Normal |
| `2` | `(2 + 1) % 10` | `3` | ✅ Normal |
| `3` | `(3 + 1) % 10` | `4` | ✅ Normal |
| `9` | `(9 + 1) % 10` | `0` | 🔄 **WRAP!** |
| `1` | `(1 + 1) % 10` | `2` | ✅ Normal |

<br/>

### ✨ Final Result: `23402`

</div>

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

### 📦 Installation & Running

</div>

<br/>

<table>
<tr>
<td width="50%">

**📋 Prerequisites**

```bash
Python 3.8+
```

</td>
<td width="50%">

**▶️ Execute**

```bash
cd project-4
python script.py
```

</td>
</tr>
</table>

<br/>

<div align="center">

### 📸 Sample Output

<br/>

![Output Screenshot](https://github.com/user-attachments/assets/bac6616f-81af-4c8f-bf2f-42c453119ca4)

</div>

<br/>

<div align="center">

**Expected Console Output:**

```python
Reversed: 19321
Digit sum: 16
Incremented: 23402
```

</div>

<br/><br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="800">
</div>

<br/><br/>

---

<br/>

## 💻 Code Examples

<br/>

<div align="center">

### 🎯 Basic Usage

</div>

<br/>

```python
from script import NumberMachine

# Create instance with your number
nm = NumberMachine(12391)

# Perform operations
print(f"🔄 Reversed: {nm.reverse_number()}")      # Output: 19321
print(f"➕ Sum: {nm.sum_of_digits()}")            # Output: 16
print(f"⬆️ Incremented: {nm.increment_digits()}")  # Output: 23402
```

<br/><br/>

<div align="center">

### 🧪 Edge Cases

</div>

<br/>

<table>
<tr>
<td width="50%">

**Single Digit**

```python
nm = NumberMachine(7)

nm.reverse_number()    # 7
nm.sum_of_digits()     # 7
nm.increment_digits()  # 8
```

</td>
<td width="50%">

**Trailing Zeros**

```python
nm = NumberMachine(1200)

nm.reverse_number()    # 21
nm.increment_digits()  # 2311
```

</td>
</tr>
<tr>
<td width="50%">

**All Nines (Wrap Test)**

```python
nm = NumberMachine(999)

nm.increment_digits()  # 0
# All digits wrap!
```

</td>
<td width="50%">

**Large Numbers**

```python
nm = NumberMachine(987654321)

nm.reverse_number()    # 123456789
nm.sum_of_digits()     # 45
```

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

## 🧠 The Mathematics Behind It

<br/>

<div align="center">

### 🔍 Understanding Modulo (`%`)

<br/>

<img src="https://user-images.githubusercontent.com/74038190/235294009-f5d9e7f6-dce8-4333-a4d7-991115b83c51.gif" width="80">

</div>

<br/>

<div align="center">

The modulo operator **extracts the rightmost digit**:

</div>

<br/>

```python
12391 % 10 = 1  ← Rightmost digit
1239 % 10  = 9  ← Next digit
123 % 10   = 3  ← Next digit
12 % 10    = 2  ← Next digit
1 % 10     = 1  ← Last digit
```

<br/><br/>

<div align="center">

### ➗ Understanding Integer Division (`//`)

<br/>

<img src="https://user-images.githubusercontent.com/74038190/235294010-ec412ef5-e3da-4efa-b1d4-0ab4d4638755.gif" width="80">

</div>

<br/>

<div align="center">

Integer division **removes the rightmost digit**:

</div>

<br/>

```python
12391 // 10 = 1239  ← Removed 1
1239 // 10  = 123   ← Removed 9
123 // 10   = 12    ← Removed 3
12 // 10    = 1     ← Removed 2
1 // 10     = 0     ← Removed 1, DONE! ✅
```

<br/><br/>

<div align="center">

### 🔄 Understanding Wrap-Around

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212749695-a6817c5a-a794-462b-afca-1b5ce7dd5e63.gif" width="80">

</div>

<br/>

<div align="center">

Modulo 10 creates **cyclic behavior**:

</div>

<br/>

```python
(0 + 1) % 10 = 1
(1 + 1) % 10 = 2
(2 + 1) % 10 = 3
   ...
(8 + 1) % 10 = 9
(9 + 1) % 10 = 0  ← Wraps back to 0! 🔄
```

<br/><br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="700">
</div>

<br/><br/>

---

<br/>

## ⏱️ Performance Analysis

<br/>

<div align="center">

### 📊 Time & Space Complexity

<br/>

<img src="https://user-images.githubusercontent.com/74038190/221352975-94759904-aa4c-4032-a8ab-b546efb9c478.gif" width="80">

</div>

<br/>

<div align="center">

| Operation | Time Complexity | Space Complexity | Method |
|:---------:|:---------------:|:----------------:|:-------|
| 🔄 **Reverse** | `O(d)` | `O(1)` | Pure integer arithmetic |
| ➕ **Sum** | `O(d)` | `O(d)` | String conversion |
| ⬆️ **Increment** | `O(d)` | `O(d)` | String iteration |

<br/>

**where `d` = number of digits**

</div>

<br/><br/>

<div align="center">

### 🎯 Why This Approach?

</div>

<br/>

<table>
<tr>
<td align="center" width="33%">

**🎨 Clean Code**

Easy to read<br/>
Easy to maintain<br/>
Pythonic style

</td>
<td align="center" width="33%">

**⚡ Efficient**

Linear time<br/>
Minimal space<br/>
Fast execution

</td>
<td align="center" width="34%">

**🧠 Educational**

Learn modulo<br/>
Learn division<br/>
Learn algorithms

</td>
</tr>
</table>

<br/><br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="500">
</div>

<br/><br/>

---

<br/>

## 🧪 Test Suite

<br/>

<div align="center">

### ✅ Comprehensive Testing

<br/>

<img src="https://user-images.githubusercontent.com/74038190/216122003-15d7e300-92e5-40bc-881a-5f2dca3f7f16.png" width="80">

</div>

<br/>

```python
def test_number_machine():
    """Complete test coverage for all operations"""
    
    # ✅ Test 1: Main Example
    nm = NumberMachine(12391)
    assert nm.reverse_number() == 19321
    assert nm.sum_of_digits() == 16
    assert nm.increment_digits() == 23402
    print("✅ Main example test passed!")
    
    # ✅ Test 2: Palindrome Number
    nm = NumberMachine(12321)
    assert nm.reverse_number() == 12321
    print("✅ Palindrome test passed!")
    
    # ✅ Test 3: All Nines (Wrap-Around)
    nm = NumberMachine(999)
    assert nm.increment_digits() == 0
    print("✅ Wrap-around test passed!")
    
    # ✅ Test 4: Single Digit
    nm = NumberMachine(5)
    assert nm.reverse_number() == 5
    assert nm.sum_of_digits() == 5
    assert nm.increment_digits() == 6
    print("✅ Single digit test passed!")
    
    # ✅ Test 5: Trailing Zeros
    nm = NumberMachine(1000)
    assert nm.reverse_number() == 1
    assert nm.increment_digits() == 2111
    print("✅ Trailing zeros test passed!")
    
    # ✅ Test 6: Large Numbers
    nm = NumberMachine(987654321)
    assert nm.reverse_number() == 123456789
    assert nm.sum_of_digits() == 45
    print("✅ Large number test passed!")
    
    print("\n🎉 All tests passed successfully! 🎉")

# Run tests
test_number_machine()
```

<br/><br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212749447-bfb7e725-6987-49d9-ae85-2015e3e7cc41.gif" width="600">
</div>

<br/><br/>

---

<br/>

## 💬 Interview Questions

<br/>

<div align="center">



<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="800">
</div>

<br/><br/>

---

<br/>

<div align="center">

## 👨‍💻 About

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="100">

<br/><br/>

**Created by Luthando Candlovu**

📅 Year: 2026<br/>
🎯 Challenge: SARAO Technical Assessment<br/>
💻 Language: Python 3.8+

<br/>

<img src="https://user-images.githubusercontent.com/74038190/213910845-af37a709-8995-40d6-be59-724526e3c3d7.gif" width="100">

<br/><br/>

### 🌟 Show Your Support

**Give a ⭐️ if this project helped you!**

<br/>

[![GitHub followers](https://img.shields.io/github/followers/LuthandoCandlovu?style=social)](https://github.com/LuthandoCandlovu)

<br/><br/>

</div>

---

<br/>

<div align="center">

### 🎲 Fun Number Facts

<br/>

```
🔢 12391 is a composite number (13 × 953)
✨ 19321 is a prime number!
➕ Digital root of 12391 = 7
🔄 Reversing twice returns original (identity property)
```

<br/><br/>

**Crafted with 🔢 Mathematics & ❤️ Python**

<br/><br/>

<img src="https://raw.githubusercontent.com/Trilokia/Trilokia/379277808c61ef204768a61bbc5d25bc7798ccf1/bottom_header.svg">

</div>
