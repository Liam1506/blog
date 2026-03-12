# Markdown Parser Test File

This is a comprehensive test file covering most standard Markdown syntax elements.

## Heading Levels

### Level 3 Heading

#### Level 4 Heading

##### Level 5 Heading

###### Level 6 Heading

## Text Formatting

This paragraph contains **bold text**, _italic text_, and **_bold italic text_**.

You can also use **bold** and _italic_ with underscores.

~~This text is struck through~~.

This has a `code snippet` inline.

## Lists

### Unordered Lists

- Item 1
- Item 2
  - Nested item 2.1
  - Nested item 2.2
    - Deep nested 2.2.1
- Item 3

### Ordered Lists

1. First item
2. Second item
   1. Nested numbered item
   2. Another nested item
3. Third item

### Mixed Lists

1. First ordered item
   - Unordered sub-item
   - Another sub-item
2. Second ordered item
   - Sub-item 1
   - Sub-item 2

### Definition-style Lists

- **Term 1**: Definition of term 1
- **Term 2**: Definition of term 2

## Code Blocks

### Inline Code

Use `const x = 42;` for variable declaration.

### Fenced Code Block - JavaScript

```javascript
function fibonacci(n) {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

const result = fibonacci(10);
console.log(result);
```

### Fenced Code Block - Python

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print(result)
```

### Fenced Code Block - SQL

```sql
SELECT users.name, COUNT(orders.id) as order_count
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.name
HAVING COUNT(orders.id) > 5
ORDER BY order_count DESC;
```

### Indented Code Block

    This is an indented code block
    Lines must be indented by 4 spaces
    Or one tab character

## Blockquotes

> This is a single line blockquote.

> This is a multi-line blockquote.
> It can span multiple lines.
> And continues here.

> **Blockquote with formatting**
>
> It can contain other Markdown elements like:
>
> - Lists
> - _Italic text_
> - `code`

> Nested blockquotes:
>
> > This is a nested blockquote
> >
> > > And this is doubly nested
> > > Back to single nesting

## Links

[This is a link to Google](https://www.google.com)

[Link with title](https://example.com "Example Site")

[Reference-style link][1]

[1]: https://reference-example.com

### Automatic Links

<https://example.com>

<user@example.com>

## Images

![Alt text for image](https://via.placeholder.com/200x150)

![Another image with title](https://via.placeholder.com/300x200 "Image Title")

## Horizontal Rules

---

---

---

## Tables

| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

| Left Aligned | Center Aligned | Right Aligned |
| :----------- | :------------: | ------------: |
| L1           |       C1       |            R1 |
| L2           |       C2       |            R2 |
| L3           |       C3       |            R3 |

| Feature       | Supported | Notes          |
| ------------- | --------- | -------------- |
| Bold          | Yes       | Use `**text**` |
| Italic        | Yes       | Use `*text*`   |
| Tables        | Yes       | GFM extension  |
| Strikethrough | Yes       | Use `~~text~~` |

## Line Breaks

This is a line.  
This is the next line with two spaces before.

This is a paragraph.

This is another paragraph (blank line between).

## Escape Characters

You can escape special characters like \* \_ \[ \] \( \) \# \+ \- \. \!

## Special Elements

### Mentions and Tags

This mentions @username.

This uses #hashtag for organization.

### Emoji Support

😀 🎉 ✨ 🚀 💻 🌟

## HTML in Markdown

<div>
  <p>This is raw HTML</p>
</div>

### HTML Entity References

&nbsp; &copy; &euro; &pound; &yen; &reg; &trade;

## Footnotes

Here is a footnote reference[^1].

[^1]: This is the footnote content. Footnotes can contain **formatting** and [links](https://example.com).

## Task Lists

- [x] Completed task
- [ ] Incomplete task
- [x] Another completed task
  - [ ] Nested incomplete task
  - [x] Nested completed task

## Description Details (HTML5)

<details>
<summary>Click to expand</summary>

This content is hidden by default and can be expanded.

- Item 1
- Item 2

```javascript
console.log("This is inside details");
```

</details>

## Mixed Complex Content

### Section with Multiple Elements

This section contains a **bold statement** followed by a [link to resources](https://example.com).

Here's a code example:

```python
class Parser:
    def __init__(self):
        self.tokens = []

    def parse(self, text):
        # Parse markdown text
        return self.tokens
```

> **Important Note**: Always escape special characters when needed.

| Type  | Example        | Notes         |
| ----- | -------------- | ------------- |
| Code  | `` `inline` `` | Use backticks |
| Block | `code`         | Use fences    |

## Special Markdown Extensions

### Strikethrough (GFM)

~~This text is deleted~~

### Autolinks (GFM)

<https://github.com>

### Superscript and Subscript

This is H<sub>2</sub>O and E=mc<sup>2</sup>

## Unicode and Special Characters

• Bullet point
– En dash
— Em dash
… Ellipsis
‚ „ " " ' ' « » ‹ › « »

## Edge Cases

Empty list item:

-

Multiple paragraphs in list:

1. Item with multiple paragraphs

   This is another paragraph in the list item.

   And a third one.

2. Second item

Inline code with special chars: `` ` ` `` and `` ` ` ``

## Document End

This is the end of the test document. Thank you for using this comprehensive Markdown test file!
