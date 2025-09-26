You are given two files: a slide set in pptx form, and a slide set in revealjs form. Your task is to convert the pptx slides to reveal.js slides, following the format in the given html file. 

The slides will be used in a lecture to teach Python programming to undergraduate students in the Vietnamese language. 

Follow these guidelines:

- Keep the slide structure, nested section (one pptx slide = one reveal.js slide)
- Only return one big code block for all slides
- Translate all text to Vietnamese
- Use HTML code (not markdown)
- Use comments (with slide title) to mark slide separators
- Use <h2> for slide titles
- Use <span class="inline-code"> for inline code 
- Use <span class="keyword"> to highlight representative keywords in each slide 
- Keep the content of each slide simple and concise 
- Keep the original Python code examples 
- For Python code blocks, use the attributes: <pre><code class="language-python" data-trim data-line-numbers="">
- For Python shell code blocks, use the attributes: <pre><code class="language-pycon" data-trim>
