# Python Blog Generator
Visit at [blog.wttg.li](https://blog.wttg.li)

A lean, script-based static site generator for minimalist blogging. Write in Markdown, compile to HTML, and host anywhere.

---

## 🛠️ Setup & Installation

Before you start crafting your masterpieces, make sure you have the necessary dependencies installed:

```bash
# Install required libraries from the requirements file
pip install -r requirements.txt
```

## 📝 How to Create a Post

The workflow is designed to be simple and terminal-friendly:

### 1. Generate the Entry

Run the creation script. It will prompt you in the terminal for the name of your new article:

```bash
python create_entry.py
```

This automatically scaffolds a new folder at `entries/article-name/` containing `text.md` and `metadata.json`.

### 2. Write your Content

Navigate to your new folder and open `text.md`. This is where your post lives. Write using standard Markdown syntax.

### 3. Enable Publishing

New posts are drafts by default. To include a post in the final site build, open the `metadata.json` file in your article's folder and set the `publish` flag to `true`:

```json
{
  "title": "My Article Name",
  "date": "2026-02-24",
  "publish": true
}
```

### 4. Compile the Site

Once you've finished writing and set your metadata, run the compiler:

```bash
python compile.py
```

The script will process your Markdown and templates, placing the finished website in the `docs/` folder.

## 📁 Project Structure

- **entries/**: Each sub-folder represents a post containing `text.md` and `metadata.json`.
- **template/**: Contains the HTML layouts that wrap your content.
- **docs/**: This is the final output folder ready for hosting (e.g., GitHub Pages). Never edit here. It will be overwritten
- **create_entry.py**: Creates a new artcile with required metadata
- **compile.py**: Creates requried html files
- **templates/**: Containes templates for fooder, hearder, blog etc.

## 🚀 Deployment

Since the final output is generated in the `docs/` folder, it's perfectly optimized for GitHub Pages. Just set your repository settings to serve from the `/docs` folder, and your blog is live!
