# ⚡️ Python Website Minifier & Zipper

A robust Python script designed to recursively minify HTML, CSS, and JavaScript files within a specified directory and bundle the optimized output into a single ZIP archive.

This tool guarantees reliable file reduction by using specialized community libraries for CSS/JS, making it perfect for preparing web deployment packages.

---

## Features

* **Recursive Minification:** Processes all `.html`, `.css`, and `.js` files in subdirectories.
* **External Library Use:** Leverages dedicated Python libraries (`cssmin`, `jsmin`) for professional-grade optimization.
* **Safety First:** Non-web files (images, fonts, etc.) are safely copied to the output without modification.
* **Performance Metrics:** Reports the time taken, total bytes saved, and the percentage reduction.
* **Clean Output:** Creates the final ZIP file and automatically removes all temporary folders.

---

## Installation

This script requires Python 3.6+ and a few external libraries.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/GLOXIOU/minimizer-HTML-CSS-JS
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Prepare the script:**
    Lunch and have fun !

---

## Usage

This script is designed to be run from *anywhere* on your system. It will prompt you for the directory path it needs to process.

1.  **Run the script:**

    ```bash
    python minimizer-HTML-CSS-JS.py
    ```

2.  **Input the absolute path:**
    When prompted, paste the full path to your website's main folder (e.g., `C:\Users\YourName\MyWebsite\`).

3.  **Validation:**
    Type `yes` to start the minification process.
