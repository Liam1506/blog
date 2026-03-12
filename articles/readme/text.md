## Python Blog Generator

Visit at [blog.wttg.li](https://blog.wttg.li)

A very simple (<300 lines of python code), script-based static site generator for minimalist blogging. Write in Markdown, compile to HTML, and host anywhere.

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

This automatically scaffolds a new folder at `entries/article-name/` containing `text.md` and `metadata.json` as well as an `asset` folder.

### 2. Write your Content

Navigate to your new folder and open `text.md`. This is where your post lives. Write using standard Markdown syntax.

### 3. Enable Publishing

New posts are drafts by default. To include a post in the final site build, open the `metadata.json` file in your article's folder and set the `publish` flag to `true` (usually located in `articles/article-name/metadata.json`):

```json
{
  "title": "My Article Name",
  "date": "2026-02-24",
  "publish": true
}
```

There will also be an `asset` folder created in the article folder. You can place images there and use them in Markdown. All files from the `asset` folder will be copied into the asset folder in the `docs` directory. Therefore, it is important that every asset has a unique name, also between articles. This will probably be changed in the future.

### 4. Compile the Site

Once you've finished writing and set your metadata, run the compiler:

```bash
python compile.py
```

The script will process your Markdown and templates, placing the finished website in the `docs/` folder.

## 📁 Project Structure

- **entries/**: Each sub-folder represents a post containing `text.md`, `metadata.json` and an `asset` folder.
- **template/**: Contains the HTML layouts that wrap your content.
- **docs/**: This is the final output folder ready for hosting (e.g., GitHub Pages). Never edit here. It will be overwritten
- **create_entry.py**: Creates a new artcile with required metadata
- **compile.py**: Creates requried html files
- **templates/**: Containes templates for fooder, hearder, blog etc.

## 🚀 Deployment

Since the final output is generated in the `docs/` folder, it's perfectly optimized for GitHub Pages. Just set your repository settings to serve from the `/docs` folder, and your blog is live!

> This is only a hobby project and not production ready at all. It is very likely, that bugs and parsing errors will occur. Moreover, there is and will be no text senetization implemented. Therefore, it is not recommended to use Markdown from unsafe locations.
