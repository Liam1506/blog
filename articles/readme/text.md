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

This automatically scaffolds a new folder at `articles/article-name/` containing `text.md` and `metadata.json` as well as an `assets` folder.

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

There will also be an `assets` folder created in the article folder. You can place images there and reference them relatively in Markdown, e.g. `![Image](assets/image.jpg)`. Each article is compiled into its own folder (`docs/entries/article-name/index.html`) and its `assets` folder is copied right next to it, so asset names only have to be unique within an article.

### 4. Compile the Site

Once you've finished writing and set your metadata, run the compiler:

```bash
python compile.py
```

The script will process your Markdown and templates, placing the finished website in the `docs/` folder.

## 📁 Project Structure

- **articles/**: Each sub-folder represents a post containing `text.md`, `metadata.json` and an `assets` folder.
- **template/**: Contains the HTML layouts that wrap your content.
- **docs/**: This is the final output folder ready for hosting (e.g., GitHub Pages). Never edit here. It will be overwritten. Every article ends up in its own folder `docs/entries/article-name/` containing an `index.html` and its `assets` folder.
- **create_entry.py**: Creates a new artcile with required metadata
- **compile.py**: Creates requried html files
- **templates/**: Containes templates for fooder, hearder, blog etc.

## 🚀 Deployment

Since the final output is generated in the `docs/` folder, it's perfectly optimized for GitHub Pages. Just set your repository settings to serve from the `/docs` folder, and your blog is live!

You don't have to compile locally: on every push to `main`, the GitHub Action in `.github/workflows/compile.yml` runs `compile.py` and commits the updated `docs/` folder. It can also be triggered manually from the Actions tab.

> This is only a hobby project and not production ready at all. It is very likely, that bugs and parsing errors will occur. Moreover, there is and will be no text senetization implemented. Therefore, it is not recommended to use Markdown from unsafe locations.
