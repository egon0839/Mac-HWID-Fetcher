# Mac HWID Fetcher

🚀 A simple yet powerful Python script that retrieves the **Hardware ID (HWID)** of a Mac and presents it in a well-formatted, stylish terminal output.

## 📌 Features
- ✅ **Fetches the Mac HWID** (IOPlatformUUID).
- 🎨 **Beautiful terminal display** using `rich`.
- 🔗 **Lightweight & fast**—runs in seconds.
- 🖥 **No additional setup** required (other than Python 3).
- 🛠 **Useful for system identification, licensing, or security purposes**.

## 💻 How It Works
This script utilizes the `ioreg` command to extract the **IOPlatformUUID**, which serves as a unique identifier for Mac hardware. The result is then formatted using the `rich` library for a sleek terminal experience.

## 📥 Installation & Usage

### 1️⃣ Install Python (if not installed)
Ensure you have **Python 3** installed. You can check by running:
```sh
python3 --version
