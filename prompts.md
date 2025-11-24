You are given two files: a slide set in pptx form, and a slide set in HTML reveal.js form. Your task is to convert the pptx slides to reveal.js slides, following the format in the given HTML file. 

The slides will be used in a lecture to teach Python programming to undergraduate students in the Vietnamese language. 

Strictly follow these guidelines when converting:

- Keep the slide structure, nested sections, one pptx slide = one reveal.js slide
- Only return one big code block for all slides, following the format in the given revealjs file
- Translate all text to Vietnamese
- Use HTML format (not Markdown)
- Use comments (with slide title) to mark slide separators
- Use <h2> for slide titles
- Use <span class="inline-code"> for inline code 
- Use <span class="keyword"> to highlight representative keywords in each slide 
- Never use <span class="keyword"> for slide titles
- Keep the content of each slide simple and concise 
- Keep the original Python code examples in the pptx file
- For Python code blocks, use the following block with these attributes: <pre><code class="language-python" data-trim data-line-numbers="">
- For Python shell code blocks, use the following block with these attributes: <pre><code class="language-pycon" data-trim>