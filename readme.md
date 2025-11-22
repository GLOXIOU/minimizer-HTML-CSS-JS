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
    git clone [YOUR_GITHUB_REPO_URL]
    cd [your-project-folder]
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Prepare the script:**
    Save the Python code (e.g., the last version provided) as `minify_report.py` in your project folder.

---

## Usage

This script is designed to be run from *anywhere* on your system. It will prompt you for the directory path it needs to process.

1.  **Run the script:**

    ```bash
    python minify_report.py
    ```

2.  **Input the absolute path:**
    When prompted, paste the full path to your website's main folder (e.g., `C:\Users\YourName\MyWebsite\`).

3.  **Validation:**
    Type `yes` to start the minification process.

### Example Output

After execution, the script generates a report similar to this:

============================================== 
✅ SUCCESS: Minification and zipping complete!
⏱️ Time taken: 0.15 seconds 
📦 Original Size: 35.12 KB 
🗜️ Final Minified Size: 27.75 KB 
💾 Total Saved: 7.37 KB (20.98%)
📁 Minified ZIP file location: C:\Users\...\...
---

## Technical Details

### Dependencies

The following external libraries are used for optimization:

* **CSS:** Uses `cssmin` for efficient CSS reduction.
* **JavaScript:** Uses `jsmin` for reliable JavaScript minification.
* **HTML:** Uses simple internal regular expressions (`re`) for comment and whitespace removal, ensuring cross-version compatibility with modern Python environments.

### Execution Flow

1.  The user provides the `SOURCE_DIRECTORY`.
2.  A temporary directory (`MINIFIED_TEMP_...`) is created.
3.  The script walks through `SOURCE_DIRECTORY`.
4.  HTML, CSS, and JS files are minified and saved into the temporary directory. Other files (images, fonts) are copied directly.
5.  All processed files in the temporary directory are compressed into a final `site_minified_....zip`.
6.  The temporary directory is deleted.

---

## Disclaimer

This project is intended for educational and personal use. While the CSS and JS tools are robust, be aware that automated minification can sometimes cause unexpected behavior in complex or non-standard codebases.

**The author is not responsible for any issues arising from the use of this software.** Please review the contents of the generated ZIP file before deployment.