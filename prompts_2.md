**Prompt to convert PPTX → Reveal.js (Vietnamese, structured like my reference file)**

You are given two files: (1) a slide set in **.pptx**, and (2) my **reference Reveal.js HTML** file. Convert the PPTX to Reveal.js **following the exact structure, styling, and conventions of the reference HTML**.

**Hard rules**

* **Output only one big code block** containing a complete, standalone **HTML** document (not Markdown).
* **One PPTX slide = one Reveal.js `<section>`**. Preserve the PPTX order and any hierarchical grouping as nested sections.
* **Vietnamese UI text** only. **Keep original Python code** unchanged (translate comments/labels around it, not the code itself).
* Use **HTML comments** to mark slide separators: `<!-- ====================== Slide: <title> ====================== -->`.
* **Titles** use `<h2>` on normal slides. For chapter separators, create an outer `<section>` with an inner **chapter title slide** using `<h1>` that includes the chapter number and a light subtitle, exactly like the reference.
* Use `<span class="inline-code">...</span>` for inline code and `<span class="keyword">...</span>` to highlight 1–2 key terms per slide.
* Keep content **simple and concise**; prefer short bullet lists.
* **Code blocks:**

  * Write Python code in correct syntax.
  * Python scripts →
    `<pre><code class="language-python" data-trim data-line-numbers=""> … </code></pre>`
  * Python shell/REPL examples →
    `<pre><code class="language-pycon" data-trim> … </code></pre>`
* **Tables** must be real HTML tables (no Markdown). Make them readable:

  * `style="width: 100%; font-size: 0.6em"` for dense comparisons (adjust 0.6–0.85em as needed).
  * Use `<span class="inline-code">` inside cells for syntax and `✅/❌/⚠️` for quick cues.
* When a concept spans multiple consecutive slides, set `data-auto-animate` on those slides to enable smooth transitions.
* If the PPTX has major parts, group slides under an outer `<section>` per part, starting with a **chapter title** slide (big `<h1>` with number), then the content slides inside the same outer section—**exactly** like the reference.
* Preserve any **example flow**: “Motivation → Basics → Operations → Exercises → Comparison → Practice/Project → Discussion → Summary”.

**Document scaffold (match the reference file)**

* Include the same `<head>` links as the reference:

  * `revealjs/dist/reset.css`, `revealjs/dist/reveal.css`, `revealjs/dist/theme/white.css`
  * `plugin/highlight/monokai.css`
  * `lecture-style.css`
* Wrap slides in `<div class="reveal"><div class="slides"> ... </div></div>`.
* Add a footer `<div class="footer">…</div>` similar to the reference.
* Use the same Reveal initialization:

  ```js
  Reveal.initialize({
    controlsLayout: "edges",
    slideNumber: true,
    hashOneBasedIndex: true,
    hash: true,
    plugins: [RevealMarkdown, RevealHighlight, RevealNotes, RevealMath.KaTeX],
  });
  ```
* Do **not** include anything outside the single HTML code block. No explanations.

**Extra fidelity**

* Convert diagrams to simple bullet points or tables when appropriate.
* Keep iconography (✅/❌/⚠️) for quick scanning.
* For comparison slides, follow the **compact table** style from the reference (e.g., List vs Tuple vs Dictionary).

**Deliverable**

* A single **HTML** code block for the entire deck, perfectly mirroring the reference layout and styles, with all PPTX content translated to Vietnamese, code preserved, and slide-for-slide correspondence.
