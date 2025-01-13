# 🎣 Phishing Page Generator (Educational Purpose Only)

## 📖 Overview
This project is a **Phishing Page Generator** designed for **educational** and **authorized penetration testing** purposes only. It automates the creation of fake login pages and allows quick deployment using **Flask** and **Ngrok**.

⚠️ **Warning:** This tool must be used strictly for **legal educational purposes** or with **explicit permission**. Misuse of this tool for malicious purposes is illegal and unethical.

## 🚀 Features
- **Automated Fake Login Page Generation**
- **Credential Capturing** and secure storage in a local file
- **Quick Deployment via Flask and Ngrok**
- **Lightweight and Easy to Use**

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/phishing-page-generator.git
cd phishing-page-generator
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Install Ngrok** (if not installed)
- Download from [Ngrok Official Website](https://ngrok.com/download)
- Authenticate Ngrok:
```bash
ngrok config add-authtoken YOUR_AUTHTOKEN
```

## 🛠️ Usage

### 1️⃣ **Set Up the Project Structure**

Ensure the following project structure:

```
phishing-page-generator/
├── phishing_page_generator.py  # Main Python script
├── captured_credentials.txt    # Stored credentials
├── requirements.txt            # Python dependencies
└── templates/                  # HTML files (Flask default folder)
    └── login.html              # Fake login page
```

🔎 **Note:** Flask requires all HTML templates to be placed inside the `templates/` folder.

### 2️⃣ **Run the Flask Server**
```bash
python phishing_page_generator.py
```

### 3️⃣ **Deploy Using Ngrok**

1. **Start Ngrok to expose Flask server**:
```bash
ngrok http 5000
```

2. **Ngrok will generate a public URL**, e.g.,
```
Forwarding  http://abcd1234.ngrok.io  ->  http://localhost:5000
```

3. **Share the public URL** (`http://abcd1234.ngrok.io`) for **authorized testing only**.

4. **Stop Ngrok Tunnel**
```bash
CTRL + C
```

### 4️⃣ **View Captured Credentials**
All submitted credentials will be saved in `captured_credentials.txt`.

---

## 📄 Example Output

```
Username: test_user, Password: test_password
Username: admin, Password: 123456
```

---

## ⚠️ Legal Disclaimer

This tool is intended for **educational** and **authorized penetration testing** purposes only.

- **Do not use** this tool on websites or systems without **explicit permission**.
- **Misuse** may result in **criminal charges** and severe consequences.

The authors are **not responsible** for any misuse of this tool.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
